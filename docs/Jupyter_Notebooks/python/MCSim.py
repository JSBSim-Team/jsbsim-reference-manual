# MCSim.py
#
# Author: Carmine Varriale, Agostino De Marco
# Date:   May 2018
#
# A collection of Python classes for running random flight dynamics simulations with JSBSim and OpenFOAM
# Classes include data handling, running simulatoins, postprocessing
# SimFamily class is intended to implement montecarlo simulation in still air
# WRSimFamily class is intended for coupling JSBSim with OpenFOAM

# Custom modules
from property_map import pmap
import data_handling as dh
import geography as geo

# Standard modules
import numpy as np
from numpy import ceil, cos, sin, asarray, radians, linspace
import random, shutil, os, threading, time, csv, utm
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt

from pint import UnitRegistry
unit = UnitRegistry()

#=======================================================================================================
#=======================================================================================================

class ScriptFile():

    def __init__(self, name):
        self.name       = name
        self.namext     = self.name + '.xml'
        self.folderpath = './JSBSim/scripts/'
        self.path       = self.folderpath + self.namext

        self.xmltree = et.parse(self.path)
        self.xmlroot = self.xmltree.getroot()          # XML Root element: <runscript>

        self.acname       = self.xmlroot.find('use').get('aircraft')
        self.acfolderpath = './JSBSim/aircraft/' + self.acname + '/'
        self.acpath       = './JSBSim/aircraft/' + self.acname + '/' + self.acname + '.xml'

        icname = self.xmlroot.find('use').get('initialize')
        self.ic = InitFile(self.acname,icname)


#=======================================================================================================
#=======================================================================================================

class InitFile():

    def __init__(self,acname,name):
        self.name       = name
        self.namext     = self.name + '.xml'
        self.folderpath = './JSBSim/aircraft/' + acname + '/'
        self.path       = self.folderpath + self.namext

        self.xmltree = et.parse(self.path)
        self.xmlroot = self.xmltree.getroot()          # XML Root element: <initialize>

        self.acname = acname


#=======================================================================================================
#=======================================================================================================

class OutFolder():

    def __init__(self,name):
        self.name       = name
        self.folderpath = './output/'
        self.path       = self.folderpath + self.name + '/'


#=======================================================================================================
#=======================================================================================================

class AutopilotFile():

    def __init__(self, acname, name):
        self.name       = name
        self.namext     = self.name + '.xml'
        self.folderpath = './JSBSim/aircraft/' + acname + '/'
        self.path       = self.folderpath + self.namext


#=======================================================================================================
#=======================================================================================================

class ConfigFile():

    def __init__(self, name):
        self.name       = name
        self.namext     = self.name + '.xml'
        self.folderpath = './JSBSim/aircraft/' + name + '/'
        self.path       = self.folderpath + self.namext

        self.xmltree = et.parse(self.path)
        self.xmlroot = self.xmltree.getroot()          # XML Root element: <fdm_config>


#=======================================================================================================
#=======================================================================================================


class SimFamily():

    def __init__(self, N, seed_name, autopilot_name, out_foldername):

        self.N = N

        self.script = ScriptFile(seed_name)
        self.config = ConfigFile(self.script.acname)
        self.ap     = AutopilotFile(self.script.acname, autopilot_name)
        self.out    = OutFolder(out_foldername)

        self.mc_stack    = {}
        self.value_stack = {}
        self.test_property  = None


    def generate_series(self, name_of_property, distribution, params):
        if distribution == 'uniform':
            series = [random.uniform(params[0], params[1]) for i in range(0, self.N)]
        elif distribution == 'gaussian':
            series = [random.gauss(params[0], params[1]) for i in range(0, self.N)]
        elif distribution == 'from_list':
            # Check that length of list is the same as number of simulations
            if len(params) == self.N:
                series = params
            else:
                print("ERROR: Length of list is not equal to number of simulations in the family")
                return 0
        self.mc_stack[name_of_property] = series
        return series


    def set_value(self, name_of_property, value):
        self.value_stack[name_of_property] = [value]
        return value


    def set_test_property(self, xml_address_of_property, limits):
        values = list(linspace(limits[0], limits[1], self.N))
        self.test_property = [xml_address_of_property, values]
        return values


    def update_script_global_params(self):

        # Properties
        for p_elem in self.script.xmlroot.find('run').findall('property'):
            if p_elem.text in list(self.value_stack.keys()):
                p_elem.set('value', str(self.value_stack[p_elem.text][0]))
                self.script.xmltree.write(self.script.path)

        # Triggering condition based on distance to field
        for event_elem in self.script.xmlroot.findall(".//event/condition/condition[@logic='AND']"):
            event_elem.text = 'guidance/field-wp-distance le '+str(self.value_stack['ext/initial-distance-to-field-trigger-ft'][0])
        self.script.xmltree.write(self.script.path)


    def update_init_global_elements(self):
        for elem in self.script.ic.xmlroot:
            if elem.tag in list(self.value_stack.keys()):
                elem.text = str(self.value_stack[elem.tag][0])
                self.script.ic.xmltree.write(self.script.ic.path)
                
       
    def update_script_actual_elements(self, script, i):
        for p_elem in script.xmlroot.find('run').findall('property'):
            if p_elem.text in list(self.mc_stack.keys()):
                p_elem.set('value', str(self.mc_stack[p_elem.text][i]))
                script.xmltree.write(script.path)


    def update_init_actual_elements(self, ic, i):
        for elem in ic.xmlroot:
            if elem.tag in list(self.mc_stack.keys()):
                elem.text = str(self.mc_stack[elem.tag][i])
                ic.xmltree.write(ic.path)


    def update_test_properties(self, script, i):
        script.xmlroot.find(self.test_property[0]).set('value','{:.9f}'.format(self.test_property[1][i]))
        script.xmltree.write(script.path)


    def run_i_sim(self, i, log='off', system='linux'):

        if log == 'on':
            print(threading.currentThread().getName(),
                'starting at '+time.strftime("%H:%M:%S",time.gmtime())+'. Current number of active threads: ', threading.activeCount()
                 )

        idx_str = '_' + '{:04}'.format(i)

        # Define actual configuration file path
        ac_config_folderpath = './JSBSim/aircraft/' + self.script.acname + idx_str + '/'
        ac_config_path = ac_config_folderpath + self.script.acname + idx_str + '.xml'
        ap_path = ac_config_folderpath + self.ap.namext

        # Define actual script and init paths
        script_path      = self.script.folderpath + self.script.name + idx_str + '.xml'
        script_ic_path   = ac_config_folderpath + self.script.ic.name + idx_str + '.xml'

        # Create actual configuration folder and copy actual config, autopilot and init into it
        # Copy actual script in its same folder
        dh.mkdir_p(ac_config_folderpath)
        shutil.copyfile(self.script.acpath, ac_config_path) # aircraft config
        shutil.copyfile(self.ap.path, ap_path) # autopilot
        shutil.copyfile(self.script.ic.path, script_ic_path)
        shutil.copyfile(self.script.path,    script_path)

        # Create actual config object and modify output elements' attirbute "name"
        config = ConfigFile(self.script.acname + idx_str)
        for elem in config.xmlroot.findall('output'):
            elem.set('name', # change attribute name with next line
                     './aircraft/' + self.script.acname + idx_str + '/' + elem.get('name'))
        config.xmltree.write(config.path)

        # Create actual script object and actual folder object
        script = ScriptFile(self.script.name + idx_str)
        out_folder    = OutFolder(self.out.name + '/' + self.out.name + idx_str)

        # Initialize field is obsolete in actual script (it's referring to template init)
        # In the actual script, set correct reference to actual init and configurations files and recreate object
        script.xmlroot.find('use').set('initialize', script.ic.name + idx_str)
        script.xmlroot.find('use').set('aircraft', script.acname + idx_str)
        script.xmltree.write(script.path)
        script = ScriptFile(self.script.name + idx_str)

        # Substitute property(i) from each key of the mc_stack in the init and script
        self.update_init_actual_elements(script.ic, i-1)
        self.update_script_actual_elements(script, i-1)

        # Update selected property for testing its trends
        if self.test_property != None:
            self.update_test_properties(script, i-1)

        # Execute JSBSim with actual script
        if system == 'linux':
            os.system('./JSBSim/JSBSim --root=./JSBSim/ ' +
                            '--script=' + script.path + ' > ' + ac_config_folderpath + 'log' + idx_str + '.txt')
        elif system == 'windows':
            os.system('..\JSBSim\JSBSim.exe --root=./JSBSim/ ' +
                            '--script=' + script.path + ' > ' + ac_config_folderpath + 'log' + idx_str + '.txt')
        else:
            print('Only Linux and Windows supported')


        # Move files to output directories
        exprs      = [script.ic.namext,     '*.csv',              '*.txt',              script.namext         ]
        from_folds = [ac_config_folderpath, ac_config_folderpath, ac_config_folderpath, self.script.folderpath]
        for expr, ffold in list(zip(exprs, from_folds)):
            dh.move_files_to_folder(expr,
                                    to_folder   = out_folder.path,
                                    from_folder = ffold)

        # Remove aircraft folder
        shutil.rmtree(ac_config_folderpath)

        if log == 'on':
            print(threading.currentThread().getName(),
              'exiting at '+time.strftime("%H:%M:%S",time.gmtime())+'.  Current number of active threads: ', threading.activeCount()-1
                 )


    def launch_mc_sim(self, log='off', system='linux'):

        # Create main output directory
        dh.mkdir_p(self.out.path)

        # Execute JSBSim for a/c catalog and move it to output directory
        if system == 'linux':
            os.system('./JSBSim/JSBSim --root=./JSBSim/ ' +
                              '--catalog=' + self.script.acname + ' > ./JSBSim/catalog_' + self.script.acname + '.txt')
        elif system == 'windows':
            os.system('..\JSBSim\JSBSim.exe --root=./JSBSim/ ' +
                              '--catalog=' + self.script.acname + ' > ./JSBSim/catalog_' + self.script.acname + '.txt')

        dh.move_files_to_folder('*.txt', to_folder  = self.out.path, from_folder = './JSBSim')


        # Create .csv file and write contents mc_stack
        dh.dict_to_csv_col(self.mc_stack, self.out.path + self.out.name + '_mc_stack.csv')
        dh.dict_to_csv_col(self.value_stack, self.out.path + self.out.name + '_value_stack.csv')

        # In the template script, search for global properties and update them according to Python values
        self.update_script_global_params()

        # In the template init, search for properties and update them according to Python values
        self.update_init_global_elements()

        # Launch MC simulation
        if log == 'on': print('Number of active threads before MC launch: ', threading.activeCount())
        start = time.time()
        thr = [ ]
        for i in range(1, self.N+1):
                thr.append(
                    threading.Thread(
                        name = 'Thread for Sim_{:04}'.format(i),
                        target = self.run_i_sim,
                        args   = (i,log)
                    )
                )
        for t in thr: t.start()
        for t in thr: t.join()

        if log == 'on':
            print('Number of active threads after MC launch: ', threading.activeCount())
        print('Total time required: {0:.2f}'.format(time.time() - start), 's')


    def extract_post_group(self, list_of_indexes, group_label):
        return PostGroup(self.out.name, self.script.acname, list_of_indexes, group_label)


#=======================================================================================================
#=======================================================================================================


class WRSimFamily(SimFamily):
    
    def __init__(self, N, seed_name, autopilot_name, out_foldername, port_num=1025):

        self.N = N

        self.script = ScriptFile(seed_name)
        self.config = ConfigFile(self.script.acname)
        self.ap     = AutopilotFile(self.script.acname, autopilot_name)
        self.out    = OutFolder(out_foldername)
        self.port   = port_num

        self.mc_stack    = {}
        self.value_stack = {}
        self.test_property  = None
        
    
    def prepare_sim(self, i, log='off', system='linux'):

        if log == 'on':
            print(threading.currentThread().getName(),
                'starting at '+time.strftime("%H:%M:%S",time.gmtime())+'. Current number of active threads: ', threading.activeCount()
                 )

        idx_str = '_port{:}'.format(self.port) + '_' + '{:04}'.format(i) 

        # Define actual configuration file path
        ac_config_folderpath = './JSBSim/aircraft/' + self.script.acname + idx_str + '/'
        ac_config_path = ac_config_folderpath + self.script.acname + idx_str + '.xml'
        ap_path = ac_config_folderpath + self.ap.namext

        # Define actual script and init paths
        script_path      = self.script.folderpath + self.script.name + idx_str + '.xml'
        script_ic_path   = ac_config_folderpath + self.script.ic.name + idx_str + '.xml'

        # Create actual configuration folder and copy actual config, autopilot and init into it
        # Copy actual script in its same folder
        dh.mkdir_p(ac_config_folderpath)
        shutil.copyfile(self.script.acpath, ac_config_path) # aircraft config
        shutil.copyfile(self.ap.path, ap_path) # autopilot
        shutil.copyfile(self.script.ic.path, script_ic_path)
        shutil.copyfile(self.script.path,    script_path)

        # Create actual config object and modify CSV output elements' attribute "name"
        config = ConfigFile(self.script.acname + idx_str)
        for elem in config.xmlroot.findall(".//output[@type='CSV']"):
            elem.set('name', # change attribute name with next line
                     './aircraft/' + self.script.acname + idx_str + '/' + elem.get('name'))
        config.xmltree.write(config.path)

        # Create actual script object and actual folder object
        script        = ScriptFile(self.script.name + idx_str)
        out_folder    = OutFolder(self.out.name + '/' + self.out.name + idx_str)

        # Initialize field is obsolete in actual script (it's referring to template init)
        # In the actual script, set correct reference to actual init and configurations files and recreate object
        script.xmlroot.find('use').set('initialize', script.ic.name + idx_str)
        script.xmlroot.find('use').set('aircraft', script.acname + idx_str)
        script.xmltree.write(script.path)
        script = ScriptFile(self.script.name + idx_str)

        # Substitute property(i) from each key of the mc_stack in the init
        self.update_init_actual_elements(script.ic, i-1)
        self.update_script_actual_elements(script, i-1)

        # Update selected property for testing its trends
        if self.test_property != None:
            self.update_test_properties(script, i-1)
    
    
    def launch_mc_sim(self, log='off', system='linux'):
        
        cmd_linux = './JSBSim/JSBSim --root=./JSBSim/ '
        cmd_windows = '.\JSBSim\JSBSim.exe --root=./JSBSim/ '

        # Create main output directory
        dh.mkdir_p(self.out.path)

        # Execute JSBSim for a/c catalog and move it to output directory
        if system == 'linux':
            os.system(cmd_linux + '--catalog=' + self.script.acname + ' > ./JSBSim/catalog_' + self.script.acname + '.txt')
        elif system == 'windows':
            os.system(cmd_windows + '--catalog=' + self.script.acname + ' > ./JSBSim/catalog_' + self.script.acname + '.txt')

        dh.move_files_to_folder('*.txt', to_folder  = self.out.path, from_folder = './JSBSim')

        # Create .csv file and write contents of mc_stack
        dh.dict_to_csv_col(self.mc_stack, self.out.path + self.out.name + '_mc_stack.csv')
        dh.dict_to_csv_col(self.value_stack, self.out.path + self.out.name + '_value_stack.csv')
 
        # In the template configuration file, change port number for WRServer
        for elem in self.config.xmlroot.findall(".//output[@type='WR']"):
            elem.set('port', str(self.port))
        self.config.xmltree.write(self.config.path)
  
        # In the template script, search for global properties and update them according to Python values
        self.update_script_global_params()

        # In the template init, search for properties and update them according to Python values
        self.update_init_global_elements()
        
        # Generate all simulations folders
        if log == 'on': print('Number of active threads before simulation setup: ', threading.activeCount())
        start = time.time()
        thr = [ ]
        launch_cmd_linux = ""
        launch_cmd_windows = ""
        
        for i in range(1, self.N+1):
            thr.append(
                threading.Thread(
                    name = 'Thread for Sim_{:04}'.format(i),
                    target = self.prepare_sim,
                    args   = (i,log)
                )
            )

            # Create launch command for Linux terminal
            idx_str = '_port{:}'.format(self.port) + '_' + '{:04}'.format(i)
            script_path = 'scripts/' + self.script.name + idx_str + '.xml'
            ac_config_folderpath = './JSBSim/aircraft/' + self.script.acname + idx_str + '/'
            ac_config_path = ac_config_folderpath + self.script.acname + idx_str + '.xml'
            launch_cmd_linux += cmd_linux + '--script=' + script_path + ' > ' + ac_config_folderpath + 'log' + idx_str + '.txt & '
            launch_cmd_windows += cmd_windows + '--script=' + script_path + ' > ' + ac_config_folderpath + 'log' + idx_str + '.txt & '
                
        for t in thr: t.start()
        for t in thr: t.join()

        if log == 'on':
            print('Number of active threads after simulation setup: ', threading.activeCount())
        
        
        # Execute all JSBSim scripts at the same time
        if system == 'linux':
            print("[Linux] Running all instances in background...")
            os.system(launch_cmd_linux + 'wait')
        elif system == 'windows':
            print("[Windows] Running all instances (in background???)...")
            print("[Windows] cmd: " + launch_cmd_windows)
            os.system(launch_cmd_windows)
        
        # Move results to output folder
        print("Organizing files and folders...")
        for i in range(1,self.N+1):
            idx_str = '_' + '{:04}'.format(i)
            #script_path          = self.script.folderpath + self.script.name  + '_port{:}'.format(self.port) + idx_str + '.xml'
            ac_config_folderpath = './JSBSim/aircraft/' + self.script.acname + '_port{:}'.format(self.port) + idx_str + '/'
            ac_config_path       =  ac_config_folderpath + self.script.acname + '_port{:}'.format(self.port) + idx_str + '.xml'
            #script_ic_path      = ac_config_folderpath + self.script.ic.name + idx_str + '.xml'
            out_folder           = OutFolder(self.out.name + '/' + self.out.name + idx_str)

            script_namext = self.script.name + '_port{:}'.format(self.port) + idx_str + '.xml'
            script_ic_namext = self.script.ic.name + idx_str + '.xml'


            exprs      = ['*.*',              script_namext         ]
            from_folds = [ac_config_folderpath, self.script.folderpath]
            for expr, ffold in list(zip(exprs, from_folds)):
                dh.move_files_to_folder(expr,
                                        to_folder   = out_folder.path,
                                        from_folder = ffold)
            
            # Remove aircraft folder
            shutil.rmtree(ac_config_folderpath)
            
        print('Total time required: {0:.2f}'.format(time.time() - start), 's')
        
        


#=======================================================================================================
#=======================================================================================================


class PostData():
    def __init__(self, output_folder_path, aircraft_name):

        self.name = aircraft_name
        self.path = output_folder_path

        # JSBSim data dictionary
        self.J = {}
        self.J.update(dh.csv_col_to_dict(self.path+self.name+'_fcs.csv'))
        self.J.update(dh.csv_col_to_dict(self.path+self.name+'_accelerations.csv'))
        self.J.update(dh.csv_col_to_dict(self.path+self.name+'_aero.csv'))
        self.J.update(dh.csv_col_to_dict(self.path+self.name+'_attitude.csv'))
        self.J.update(dh.csv_col_to_dict(self.path+self.name+'_position.csv'))
        self.J.update(dh.csv_col_to_dict(self.path+self.name+'_propulsion.csv'))
        self.J.update(dh.csv_col_to_dict(self.path+self.name+'_velocities.csv'))
        self.J.update(dh.csv_col_to_dict(self.path+self.name+'_winds.csv'))
        #self.J.update(dh.csv_col_to_dict(self.path+self.name+'_test_analysis.csv'))

        # Python data dictionary, for quantities that cannot be calculated in JSBSim
        self.P = {}
        
        # Final results dictionary (most likely to read high frequency output data)
        self.F = {}
        self.F.update(dh.csv_col_to_dict(self.path+self.name+'_finalresults.csv'))

        # active_wp_switch is 1 when 'ap/active-waypoint' is updated
        # t_over_wp_indexes are the indexes of the time array when this happens
        # These variables are used to mark a flyby over a waypoint in all time history charts
        self.P['active_wp_switch'] = list(np.insert(np.diff(self.J[pmap['active_wp']['property']])[1:],0,[0,0]))
        self.P['t_over_wp_indexes'] = [i for i,x in enumerate(self.P['active_wp_switch']) if x != 0]


    def show_JSBSim_output_properties(self):
        print(*list(sorted(self.J.keys())), sep='\n')


    def get_traj_in_NEA(self, lat0=None, lon0=None, flat=True):

        # Variables' name abbreviations
        lat = np.asarray(self.J[pmap['lat_gc_rad']['property']])
        lon = np.asarray(self.J[pmap['lon_gc_rad']['property']])
        h   = np.asarray(self.J[pmap['h_sl_m']['property']])

        # Call transformation function in geography module
        Rnea_m = geo.geoc_to_NEA(lat, lon, 0, lat0, lon0, flat)

        # Save result to local dictionary
        self.P['Xnea_m'] = list(Rnea_m[0])
        self.P['Ynea_m'] = list(Rnea_m[1])
        self.P['Znea_m'] = list(Rnea_m[2])

        Rnea_ft = (Rnea_m*unit.m).to(unit.ft).magnitude
        self.P['Xnea_ft'] = list(Rnea_ft[0])
        self.P['Ynea_ft'] = list(Rnea_ft[1])
        self.P['Znea_ft'] = list(Rnea_ft[2])

        # Trajectory length
        dX2_m = [0, *list(np.diff(np.asarray(self.P['Xnea_m']))**2)]
        dY2_m = [0, *list(np.diff(np.asarray(self.P['Ynea_m']))**2)]
        dZ2_m = [0, *list(np.diff(np.asarray(self.P['Znea_m']))**2)]
        dX2_ft = [0, *list(np.diff(np.asarray(self.P['Xnea_ft']))**2)]
        dY2_ft = [0, *list(np.diff(np.asarray(self.P['Ynea_ft']))**2)]
        dZ2_ft = [0, *list(np.diff(np.asarray(self.P['Znea_ft']))**2)]
        
        self.P['s_traj_m']  = list(np.cumsum(np.sqrt(np.asarray(dX2_m)+np.asarray(dY2_m)+np.asarray(dZ2_m))))
        self.P['s_traj_ft'] = list(np.cumsum(np.sqrt(np.asarray(dX2_ft)+np.asarray(dY2_ft)+np.asarray(dZ2_ft))))
        
        subP = {key: self.P[key] for key in ('Xnea_m','Ynea_m','Znea_m','Xnea_ft','Ynea_ft','Znea_ft','s_traj_m','s_traj_ft')} 
        dh.dict_to_csv_col(subP, self.path+self.name+'_trajNEA.csv')
        
        
    def load_traj_in_NEA(self):
        subP = dh.csv_col_to_dict(self.path+self.name+'_trajNEA.csv')
        self.P.update(subP)
    
    
    def get_traj_in_UTM(self):
        
        # Variables' name abbreviations
        lat = np.asarray(self.J[pmap['lat_gc_deg']['property']])
        lon = np.asarray(self.J[pmap['lon_gc_deg']['property']])
        
        z = list(zip(lat,lon))
        
        # Call transformation function in utm module
        Rutm_m = [utm.from_latlon(*z[i])[0:2] for i in range(len(lat))]

        # Save result to local dictionary
        self.P['Eutm_m'] = [Rutm_m[i][0] for i in range(len(Rutm_m))]
        self.P['Nutm_m'] = [Rutm_m[i][1] for i in range(len(Rutm_m))]

        Rutm_ft = (Rutm_m*unit.m).to(unit.ft).magnitude
        self.P['Eutm_ft'] = [Rutm_ft[i][0] for i in range(len(Rutm_ft))]
        self.P['Nutm_ft'] = [Rutm_ft[i][1] for i in range(len(Rutm_ft))]

        # Trajectory length
        dE2_m = [0, *list(np.diff(np.asarray(self.P['Eutm_m']))**2)]
        dN2_m = [0, *list(np.diff(np.asarray(self.P['Nutm_m']))**2)]
        dH2_m = [0, *list(np.diff(np.asarray(self.J[pmap['h_sl_m']['property']]))**2)]
        dE2_ft = [0, *list(np.diff(np.asarray(self.P['Eutm_ft']))**2)]
        dN2_ft = [0, *list(np.diff(np.asarray(self.P['Nutm_ft']))**2)]
        dH2_ft = [0, *list(np.diff(np.asarray(self.J[pmap['h_sl_ft']['property']]))**2)]

        self.P['s_traj_m'] = list(np.cumsum(np.sqrt(np.asarray(dE2_m)+np.asarray(dN2_m)+np.asarray(dH2_m))))
        self.P['s_traj_ft'] = list(np.cumsum(np.sqrt(np.asarray(dE2_ft)+np.asarray(dN2_ft)+np.asarray(dH2_ft))))
        
        subP = {key: self.P[key] for key in ('Eutm_m','Nutm_m','Eutm_ft','Nutm_ft','s_traj_m','s_traj_ft')} 
        dh.dict_to_csv_col(subP, self.path+self.name+'_trajUTM.csv')
        

    def load_traj_in_UTM(self):
        subP = dh.csv_col_to_dict(self.path+self.name+'_trajUTM.csv')
        self.P.update(subP)
 

    def plot_vars(self, *variables, grid='on', y_lim=(None,None)):

        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.0, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):

            for var in variables:

                fig = plt.figure(figsize=(12.3,5))
                ax = fig.add_subplot(1,1,1)

                # Notation simplification
                t = self.J[pmap['t']['property']]
                y = self.J[pmap[var]['property']]

                ax.plot(t, y, marker='.', markevery=self.P['t_over_wp_indexes'])

                ax.set_xlabel(pmap['t']['axis_label'])
                ax.set_ylabel(pmap[var]['axis_label'])
                ax.set_title(pmap[var]['figure_title'])

                if grid == 'on':
                    plt.minorticks_on()
                    plt.grid(True)
                    ax.xaxis.grid(True, which='minor')

                ax.set_ylim(
                    ymin = y_lim[0],
                    ymax = y_lim[1])

                plt.tight_layout()
                plt.savefig(self.path+'plot_'+var+'.pdf')


    def plot_vars_vs_s(self, *variables, grid='on', y_lim=(None,None)):

        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.0, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):
            for var in variables:

                fig = plt.figure(figsize=(12.3,5))
                ax = fig.add_subplot(1,1,1)

                # Notation simplification
                s = self.P['s_traj_ft']
                y = self.J[pmap[var]['property']]

                ax.plot(s, y, marker='.', markevery=self.P['t_over_wp_indexes'])
                ax.set_xlabel(pmap['s']['axis_label'])
                ax.set_ylabel(pmap[var]['axis_label'])
                ax.set_title(pmap[var]['figure_title'])

                if grid == 'on':
                    plt.minorticks_on()
                    plt.grid(True)
                    ax.xaxis.grid(True, which='minor')

                ax.set_ylim(
                    ymin = y_lim[0],
                    ymax = y_lim[1])

                plt.tight_layout()
                plt.savefig(self.path+'plot_'+var+'_vs_s.pdf')


    def plot_ground_track(self, ax_lim = [ ], grid='on'):

        # Calculate WP1 relative position to WP2
        lat_WP1_rad = self.J[pmap['lat_WP1']['property']][0]
        lon_WP1_rad = self.J[pmap['lon_WP1']['property']][0]
        lat_WPf_rad = self.J[pmap['lat_WPf']['property']][0]
        lon_WPf_rad = self.J[pmap['lon_WPf']['property']][0]

        RneaWP1_m = geo.geoc_to_NEA(lat_WP1_rad, lon_WP1_rad, 0, lat0=lat_WPf_rad, lon0=lon_WPf_rad, flat=1)
        XneaWP1_ft = (RneaWP1_m[0]*unit.m).to(unit.ft).magnitude
        YneaWP1_ft = (RneaWP1_m[1]*unit.m).to(unit.ft).magnitude

        # Plot
        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.0, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):

            fig = plt.figure(figsize=(12.3,12.3))
            ax  = fig.add_subplot(1,1,1)

            ax.plot(self.P['Ynea_ft'], self.P['Xnea_ft'])

            # Marker on WPf
            ax.scatter(0,0, c=1, s=50, alpha=0.5)

            # Marker on WP1
            ax.scatter(YneaWP1_ft, XneaWP1_ft, c=1, s=50, alpha=0.5)

            # Set title and axes labels
            ax.set_xlabel(r'$Y_E$ (ft)')
            ax.set_ylabel(r'$X_N$ (ft)')
            ax.set_title('Ground track')

            plt.axis('equal')
            plt.axis(ax_lim)
            plt.minorticks_on()
            if grid == 'on': plt.grid(True, which='both')
            plt.tight_layout()
            plt.savefig(self.path+'plot_ground_track.pdf')


#=======================================================================================================
#=======================================================================================================


class PostGroup():

    def __init__(self, main_output_folder_name, aircraft_name, list_of_indexes, group_label, log='off'):
        self.out     = OutFolder(main_output_folder_name)
        self.acname  = aircraft_name
        self.indexes = list_of_indexes
        self.label   = group_label

        def prg_str(i):
            return '_{:04}'.format(i)

        def prg_num(i):
            return prg_str(i).replace('_','')

        # Show confirmation message
        if log == 'on':
            print('Extracting data from simulations: \n', *['{:04}'.format(i) for i in self.indexes], sep=' -', end='\n\n')

        # Create a dictionary whose keys are selected indexes (ex: 0001, 0023) and values are PostData objects
        if log == 'on': print('Number of active threads before output extraction: ', threading.activeCount())
        start = time.time()
        self.group   = { }      # reference dictionary
        thr = [ ]
        for i in self.indexes:

            subfolder_path = self.out.path+self.out.name+prg_str(i)+'/'

            thr.append(
              threading.Thread(
                name   = 'Thread for PostData'+prg_str(i),
                target = self.group.update,
                args   = ({prg_num(i): PostData(subfolder_path , aircraft_name)},
                )
              )
            )
        for t in thr: t.start()
        for t in thr: t.join()

        # Extract mc values corresponding to selected indexes
        self.mc_stack = dh.csv_col_to_dict(self.out.path + self.out.name + '_mc_stack.csv')
        for key in sorted(self.mc_stack.keys()):
            self.mc_stack[key] = [self.mc_stack[key][i-1] for i in self.indexes]

        # Extract global values corresponding to selected indexes
        self.value_stack = dh.csv_col_to_dict(self.out.path + self.out.name + '_value_stack.csv')

        if log == 'on': print('Number of active threads after output extraction:  ', threading.activeCount())
        print('Total time required: {0:.2f}'.format(time.time() - start), 's')


    def get_traj_in_NEA(self,lat0=None,lon0=None,flat=1):

        thr = [ ]
        for i in sorted(self.group):
            thr.append(
                    threading.Thread(
                        name   = 'Thread for output data "' + str(i) + '"',
                        target = self.group[i].get_traj_in_NEA,
                        args   = (lat0,lon0,flat,)
                    )
            )
        for t in thr: t.start()
        for t in thr: t.join()
            
     
    def load_traj_in_NEA(self):

        thr = [ ]
        for i in sorted(self.group):
            thr.append(
                threading.Thread(
                    name   = 'Thread for output data "' + str(i) + '"',
                    target = self.group[i].load_traj_in_NEA,
                    args   = ()
                )
            )
        for t in thr: t.start()
        for t in thr: t.join()
            
         
    def get_traj_in_UTM(self):

        thr = [ ]
        for i in sorted(self.group):
            thr.append(
                    threading.Thread(
                        name   = 'Thread for output data "' + str(i) + '"',
                        target = self.group[i].get_traj_in_UTM,
                        args   = ()
                    )
            )
        for t in thr: t.start()
        for t in thr: t.join()
            
            
    def load_traj_in_UTM(self):

        thr = [ ]
        for i in sorted(self.group):
            thr.append(
                threading.Thread(
                    name   = 'Thread for output data "' + str(i) + '"',
                    target = self.group[i].load_traj_in_UTM,
                    args   = ()
                )
            )
        for t in thr: t.start()
        for t in thr: t.join()


    def plot_vars(self,*variables, grid='on', legend='off', lbl_idx=None, ax_lim= [None, None, None, None]):

        start = time.time()

        # Set number of legend columns, 30 entries per column
        n_legend_cols = int(ceil(len(self.group.keys()) // 31) + 1)

        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.5, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):

            for var in variables:
                fig = plt.figure(figsize=(12.3,5))
                ax  = fig.add_subplot(1,1,1)


                for i in sorted(self.group):
                    # Notation simplification
                    data = self.group[i]
                    t = data.J[pmap['t']['property']]
                    y = data.J[pmap[var]['property']]

                    # Color rotation settings and plot
                    line = ax.plot(t, y, label=i, marker='.', markevery=data.P['t_over_wp_indexes'])
                    if lbl_idx != None:
                        plt.text(t[lbl_idx], y[lbl_idx], str(i), fontsize=6, color=plt.getp(line[0], 'color'))

                # Legend
                if legend == 'on':
                    lgd = ax.legend(bbox_to_anchor=(1.005, 1), loc='upper left', ncol=n_legend_cols)

                # Set title and axes params
                ax.set_xlabel(pmap['t']['axis_label'])
                ax.set_ylabel(pmap[var]['axis_label'])
                ax.set_title(pmap[var]['figure_title'])
                if grid == 'on':
                    plt.minorticks_on()
                    plt.grid(True)
                    ax.xaxis.grid(True, which='minor')

                plt.axis(ax_lim)
                plt.tight_layout()

                # Export
                if legend == 'on':
                    plt.savefig(self.out.path + 'Group_' + self.label + '_plot_' + var + '.pdf',
                            bbox_extra_artists=(lgd,), bbox_inches='tight')
                else:
                    plt.savefig(self.out.path + 'Group_' + self.label + '_plot_' + var + '.pdf')

        print('Total time required: {0:.2f}'.format(time.time() - start), 's')


    def plot_vars_vs_s(self,*variables, grid='on', legend='off', lbl_idx=None, ax_lim= [None, None, None, None]):

        start = time.time()

        # Set number of legend columns, 30 entries per column
        n_legend_cols = int(ceil(len(self.group.keys()) // 31) + 1)

        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.5, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):

            for var in variables:
                fig = plt.figure(figsize=(12.3,5))
                ax  = fig.add_subplot(1,1,1)


                for i in sorted(self.group):
                    # Notation simplification
                    data = self.group[i]
                    s = data.P['s_traj_ft']
                    y = data.J[pmap[var]['property']]

                    # Color rotation settings and plot
                    line = ax.plot(s, y, label=i, marker='.', markevery=data.P['t_over_wp_indexes'])
                    if lbl_idx != None:
                        plt.text(t[lbl_idx], y[lbl_idx], str(i), fontsize=6, color=plt.getp(line[0], 'color'))

                # Legend
                if legend == 'on':
                    lgd = ax.legend(bbox_to_anchor=(1.005, 1), loc='upper left', ncol=n_legend_cols)

                # Set title and axes params
                ax.set_xlabel(pmap['s']['axis_label'])
                ax.set_ylabel(pmap[var]['axis_label'])
                ax.set_title(pmap[var]['figure_title'])
                if grid == 'on':
                    plt.minorticks_on()
                    plt.grid(True)
                    ax.xaxis.grid(True, which='minor')

                plt.axis(ax_lim)
                plt.tight_layout()

                # Export
                if legend == 'on':
                    plt.savefig(self.out.path + 'Group_' + self.label + '_plot_' + var + '_vs_s.pdf',
                            bbox_extra_artists=(lgd,), bbox_inches='tight')
                else:
                    plt.savefig(self.out.path + 'Group_' + self.label + '_plot_' + var + '_vs_s.pdf')


        print('Total time required: {0:.2f}'.format(time.time() - start), 's')


    def plot_ground_track(self, ax_lim = [ ], grid='on', legend='off', lbl_idx=None,):

        import geography as geo

        start = time.time()

        # Set number of legend columns, 50 entries per column
        n_legend_cols = int(ceil(len(self.group.keys()) // 51) + 1)

        # Calculate WP1 relative position to WP2
        lat_WP1_rad = self.group[list(self.group.keys())[0]].J[pmap['lat_WP1']['property']][0]
        lon_WP1_rad = self.group[list(self.group.keys())[0]].J[pmap['lon_WP1']['property']][0]
        lat_WPf_rad = self.group[list(self.group.keys())[0]].J[pmap['lat_WPf']['property']][0]
        lon_WPf_rad = self.group[list(self.group.keys())[0]].J[pmap['lon_WPf']['property']][0]

        RneaWP1_m = geo.geoc_to_NEA(lat_WP1_rad, lon_WP1_rad, 0, lat0=lat_WPf_rad, lon0=lon_WPf_rad, flat=1)
        XneaWP1_ft = (RneaWP1_m[0]*unit.m).to(unit.ft).magnitude
        YneaWP1_ft = (RneaWP1_m[1]*unit.m).to(unit.ft).magnitude

        # Plot
        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.5, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):
            fig = plt.figure(figsize=(12.3,12.3))
            ax  = fig.add_subplot(1,1,1)

            # Trajectories
            for i in sorted(self.group):
                line = ax.plot(self.group[i].P['Ynea_ft'], self.group[i].P['Xnea_ft'], label=i)
                if lbl_idx != None:
                        plt.text(self.group[i].P['Ynea_ft'][lbl_idx], self.group[i].P['Xnea_ft'][lbl_idx], str(i),
                                 fontsize=6, color=plt.getp(line[0], 'color'))

            # Marker on WPf
            ax.scatter(0,0, c=1, s=50, alpha=0.5)

            # Marker on WP1
            ax.scatter(YneaWP1_ft, XneaWP1_ft, c=1, s=50, alpha=0.5)

            # Legend
            if legend == 'on':
                lgd = ax.legend(bbox_to_anchor=(1.005, 1), loc='upper left', ncol=n_legend_cols)

            # Set title and axes labels
            ax.set_xlabel(r'$Y_{E}$ (ft)')
            ax.set_ylabel(r'$X_{N}$ (ft)')
            ax.set_title('Ground track')

            plt.axis('equal')
            plt.axis(ax_lim)
            if grid == 'on':
                plt.minorticks_on()
                plt.grid(True, which='both')

            plt.tight_layout()

            # Export
            if legend == 'on':
                plt.savefig(self.out.path+'Group_'+self.label+'_plot_groundtrack.pdf',
                            bbox_extra_artists=(lgd,), bbox_inches='tight')
            else:
                plt.savefig(self.out.path+'Group_'+self.label+'_plot_groundtrack.pdf')

        print('Total time required: {0:.2f}'.format(time.time() - start), 's')
     
    
    def plot_ground_track_UTM(self, origin=[ ], ax_lim=[ ], grid='on', legend='off', lbl_idx=None,):

        start = time.time()

        # Set number of legend columns, 50 entries per column
        n_legend_cols = int(ceil(len(self.group.keys()) // 51) + 1)

        # Plot
        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.5, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):
            
            fig = plt.figure(figsize=(12.3,12.3))
            ax  = fig.add_subplot(1,1,1)

            # Trajectories
            for i in sorted(self.group):
                X = np.array(self.group[i].P['Eutm_m']) - origin[0]
                Y = np.array(self.group[i].P['Nutm_m']) - origin[1]
                line = ax.plot(X, Y, label=i)
                orig = ax.scatter(0,0, c=1, s=50, alpha=0.5)
                if lbl_idx != None:
                        plt.text(X[lbl_idx], Y[lbl_idx], str(i), fontsize=6, color=plt.getp(line[0], 'color'))

            # Legend
            if legend == 'on':
                lgd = ax.legend(bbox_to_anchor=(1.005, 1), loc='upper left', ncol=n_legend_cols)

            # Set title and axes labels
            ax.set_xlabel(r'$X_{E}$ (m)')
            ax.set_ylabel(r'$Y_{N}$ (m)')
            ax.set_title('Ground track in UTM')

            plt.axis('equal')
            plt.axis(ax_lim)
            if grid == 'on':
                plt.minorticks_on()
                plt.grid(True, which='both')

            plt.tight_layout()

            # Export
            if legend == 'on':
                plt.savefig(self.out.path+'Group_'+self.label+'_plot_groundtrack_UTM.pdf',
                            bbox_extra_artists=(lgd,), bbox_inches='tight')
            else:
                plt.savefig(self.out.path+'Group_'+self.label+'_plot_groundtrack_UTM.pdf')

        print('Total time required: {0:.2f}'.format(time.time() - start), 's')
        
        
    def plot_traj3D_UTM(self,origin=[ ], Hdisk=120, ax_lim=None, nticks=[11,11,11], view=(45,-45), to_scale='XYZ', mrk_size=80, legend='off'):

        from mpl_toolkits.mplot3d import Axes3D
        import plotting_utilities as plut

        start = time.time()

        # Set number of legend columns, 50 entries per column
        n_legend_cols = int(ceil(len(self.group.keys()) // 51) + 1)

        # Plot
        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.5, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):
            
            fig = plt.figure(figsize=(12.3,12.3))
            ax  = fig.add_subplot(1,1,1,projection='3d')

            # Trajectories
            for i in sorted(self.group):
                X = np.array(self.group[i].P['Eutm_m']) - origin[0]
                Y = np.array(self.group[i].P['Nutm_m']) - origin[1]
                Z = np.array(self.group[i].J[pmap['h_sl_m']['property']])
                line = ax.plot(X, Y, Z, label=i)
                #turb = ax.plot([0,0],[0,0],[0,120], color='#D8D8D8', linewidth=5)
                disk = ax.scatter(0,0,Hdisk, c=1, s=50, alpha=1)

            if to_scale=='XYZ': 
                plut.make_axis_equal_3d(X,Y,Z,ax,to_scale='XYZ')
                ax.set_title("Trajectory, to scale")
            elif to_scale=='XY': 
                plut.make_axis_equal_3d(X,Y,Z,ax,to_scale='XY')
                ax.set_title(r"Trajectory, not to scale")
            else:
                ax.set_title("Trajectory, not to scale")
            
            if ax_lim == None:
                XMIN, YMIN, ZMIN = ax.get_xlim().min(), ax.get_ylim().min(), ax.get_zlim().min()
                XMAX, YMAX, ZMAX = ax.get_xlim().max(), ax.get_ylim().max(), ax.get_zlim().max()
            else:
                XMIN, YMIN, ZMIN = ax_lim[0], ax_lim[2], ax_lim[4],
                XMAX, YMAX, ZMAX = ax_lim[1], ax_lim[3], ax_lim[5]
                
            ax.set_xlim3d([XMIN, XMAX])
            ax.set_ylim3d([YMIN, YMAX])
            ax.set_zlim3d([ZMIN, ZMAX])
            
            # Ticks
            ax.set_xticks(np.linspace(XMIN, XMAX, nticks[0]))
            ax.set_yticks(np.linspace(YMIN, YMAX, nticks[1]))
            ax.set_zticks(np.linspace(ZMIN, ZMAX, nticks[2]))
            
            # Labels and legend
            ax.set_xlabel('\n'+r'$X_{E}$ (m)', linespacing=3.5)
            ax.set_ylabel('\n'+r'$Y_{N}$ (m)', linespacing=3.5)
            ax.set_zlabel('\n'+r'$h_\mathrm{SL}$ (m)', linespacing=3.5)

            if legend == 'on':
                lgd = ax.legend(bbox_to_anchor=(1.005, 1), loc='upper left', ncol=n_legend_cols)

            # Axis visualization and scale
            #ax.invert_xaxis()
            ax.view_init(view[0],view[1]) # Elevation, Azimuth

            plt.tight_layout()

        # Export
        if legend == 'on':
            plt.savefig(self.out.path+'Group_'+self.label+'_plot_traj3D_UTM.pdf',
                        bbox_extra_artists=(lgd,), bbox_inches='tight')
        else:
            plt.savefig(self.out.path+'Group_'+self.label+'_plot_traj3D_UTM.pdf')

        print('Total time required: {0:.2f}'.format(time.time() - start), 's')
        
 
    def results(self, XY_turb, D_turb, windDir, t_lim=[None, None], linestyle='-'):
        
        # Initialization
        D = {'d_cross': [ ], 'h_cross': [ ], 
             'nz_max': [ ], 'nz_min': [ ], 'nz_avg': [ ], 'nz_std': [ ], 
             'Vwz_max': [ ], 'Vwz_min': [ ], 'Vwz_avg': [ ], 'Vwz_std': [ ],}
        
        print('Index ','Altit.','dist/D','nz_max','nz_min','nz_avg','nz_std','Ww_max','Ww_min','Ww_avg','Ww_std', sep='    ')
        print('---------------------------------------------------------------------------------------------------------------')

        for i in sorted(self.group):
            
            # Notation simplification
            Xt = XY_turb[0]  ; Yt = XY_turb[1] 
            data = self.group[i]
            
            # Data extraction in time domain
            i1 = dh.takeClosest(data.F[pmap['t']['property']], t_lim[0])[0]
            i2 = dh.takeClosest(data.F[pmap['t']['property']], t_lim[1])[0]

            t   = data.F[pmap['t']['property']][i1:i2+1]
            nz  = data.F[pmap['n_z']['property']][i1:i2+1]
            Vwz = data.F[pmap['Vw_z_kts']['property']][i1:i2+1]
            
            # Data extraction in space domain
            # Create line passing through turbine, and aligned with the wind direction
            if windDir == 90 or windDir == 270:
                deltaY = list(np.asarray(data.P['Nutm_m']) - Yt)
                index, delta = dh.takeClosest(deltaY, 0)            
            else:
                Xw = Xt + np.tan(np.radians(windDir))*(np.asarray(data.P['Nutm_m']) - Yt)
                print(Xw, np.asarray(data.P['Eutm_m']), sep='\n')

                # Find intersection point with trajectory
                deltaX = list(np.asarray(data.P['Eutm_m']) - Xw)
                index, delta = dh.takeClosest(deltaX, 0)

            # Calculate height at intersection
            h = data.J[pmap['h_agl_m']['property']][index]

            # Calculate distance at intersection
            X = data.P['Eutm_m'][index]
            Y = data.P['Nutm_m'][index]
            d = np.sqrt((X-Xt)**2+(Y-Yt)**2)
            
            # Results calculation
            D['h_cross'].append(h) ;            D['d_cross'].append(d)
            D['nz_max'].append(max(nz)) ;       D['nz_min'].append(min(nz)) 
            D['nz_avg'].append(np.mean(nz)) ;   D['nz_std'].append(np.std(nz))
            D['Vwz_max'].append(max(Vwz)) ;     D['Vwz_min'].append(min(Vwz)) 
            D['Vwz_avg'].append(np.mean(Vwz)) ; D['Vwz_std'].append(np.std(Vwz))
            
            print(i, "{:7.2f}".format(h), 
                     "{:7.2f}".format(d/D_turb), 
                     "{:7.2f}".format(D['nz_max'][-1]),
                     "{:7.2f}".format(D['nz_min'][-1]),
                     "{:7.2f}".format(D['nz_avg'][-1]),
                     "{:7.2f}".format(D['nz_std'][-1]),
                     "{:7.2f}".format(D['Vwz_max'][-1]),
                     "{:7.2f}".format(D['Vwz_min'][-1]),
                     "{:7.2f}".format(D['Vwz_avg'][-1]),
                     "{:7.2f}".format(D['Vwz_std'][-1]),
                      sep='   ')
            
        # Sorting the arrays by increasing distance
        for key, val in D.items(): D[key] = np.array(val)
        inds = D['d_cross'].argsort()
        for key, val in D.items(): D[key] = val[inds]
            
        # Export to file
        dh.dict_to_csv_col(D, self.out.path+'Group_'+self.label+'_results.csv')
            
        # Plotting
        with plt.rc_context({'lines.linestyle': linestyle, 'lines.linewidth': 1.5, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'lines.markersize' : 6, 'lines.markeredgewidth': 0, 
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):
            
            ## Vw_z versus distance from turbine
            fig = plt.figure(figsize=(12.3,5))
            ax  = fig.add_subplot(1,1,1)
            
            ax.plot(D['d_cross']/D_turb, D['Vwz_max'], color= '#000099', marker='^', label='Max')
            ax.errorbar(D['d_cross']/D_turb, D['Vwz_avg'], D['Vwz_std'], 
                        color= '#000099', marker='o', label='$\mu \pm \sigma$')
            ax.plot(D['d_cross']/D_turb, D['Vwz_min'], color= '#000099', marker='v', label='Min')

            ax.set_xlabel(r'$x/D$')
            ax.set_ylabel(r'$\{V_{w}\}_z$ (kts) at CG')
            ax.set_title('Wind speed at CG, in BODY ref. frame')
            
            plt.minorticks_on()
            plt.grid(True)
            ax.xaxis.grid(True, which='minor')
            
            lgd = ax.legend()

            plt.tight_layout()
            
            # Export to image
            plt.savefig(self.out.path+'Group_'+self.label+'_results_Vwz.pdf')
            
            
            ## Nz versus distance from turbine
            fig = plt.figure(figsize=(12.3,5))
            ax  = fig.add_subplot(1,1,1)
            
            ax.plot(np.asarray(D['d_cross'])/D_turb, D['nz_max'], color= '#000099', marker='^', label='Max')
            ax.errorbar(np.asarray(D['d_cross'])/D_turb, D['nz_avg'], D['nz_std'], color= '#000099', marker='o', 
                        label='$\mu \pm \sigma$')
            ax.plot(np.asarray(D['d_cross'])/D_turb, D['nz_min'], color= '#000099', marker='v', label='Min')

            ax.set_xlabel(r'$x/D$')
            ax.set_ylabel(r'$\{n_{z}\}_B$ at CG')
            ax.set_title('Load factor at CG, in Body ref. frame')            
            
            plt.minorticks_on()
            plt.grid(True)
            ax.xaxis.grid(True, which='minor')
            
            lgd = ax.legend()

            plt.tight_layout()
            
            # Export to image
            plt.savefig(self.out.path+'Group_'+self.label+'_results_nz.pdf')
           
           
        
    def plot_results(self,*variables, grid='on', legend='off', lbl_idx=None, ax_lim= [None, None, None, None]):

        start = time.time()

        # Set number of legend columns, 30 entries per column
        n_legend_cols = int(ceil(len(self.group.keys()) // 31) + 1)

        with plt.rc_context({'lines.linestyle': '-', 'lines.linewidth': 1.5, 'legend.fontsize': 10,
                             'axes.labelsize': 18, 'axes.labelweight': 100,
                             'legend.labelspacing': 0.18, 'legend.handletextpad': 0.2, 'legend.borderaxespad': 0.0,
                             'legend.columnspacing': 0.2}):

            for var in variables:
                fig = plt.figure(figsize=(12.3,5))
                ax  = fig.add_subplot(1,1,1)


                for i in sorted(self.group):
                    # Notation simplification
                    data = self.group[i]
                    t = data.F[pmap['t']['property']]
                    y = data.F[pmap[var]['property']]

                    # Color rotation settings and plot
                    line = ax.plot(t, y, label=i, marker='.', markevery=data.P['t_over_wp_indexes'])
                    if lbl_idx != None:
                        plt.text(t[lbl_idx], y[lbl_idx], str(i), fontsize=6, color=plt.getp(line[0], 'color'))

                    # Legend
                    if legend == 'on':
                        lgd = ax.legend(bbox_to_anchor=(1.005, 1), loc='upper left', ncol=n_legend_cols)

                    # Set title and axes params
                    ax.set_xlabel(pmap['t']['axis_label'])
                    ax.set_ylabel(pmap[var]['axis_label'])
                    ax.set_title(pmap[var]['figure_title'])
                    if grid == 'on':
                        plt.minorticks_on()
                        plt.grid(True)
                        ax.xaxis.grid(True, which='minor')

                        plt.axis(ax_lim)
                        plt.tight_layout()

                    # Export
                    if legend == 'on':
                        plt.savefig(self.out.path + 'Group_' + self.label + '_plot_' + var + '.pdf',
                                    bbox_extra_artists=(lgd,), bbox_inches='tight')
                    else:
                        plt.savefig(self.out.path + 'Group_' + self.label + '_plot_' + var + '.pdf')

        print('Total time required: {0:.2f}'.format(time.time() - start), 's')