from ACDataOut import ACDataOut
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plttick

class ACDataPlots(ACDataOut):
    
    """
    This class provides a collection of methods for plotting
    data coming from JSBSim output files.
    
    Superclasses to this
    ----------------------
    ACDataOut
    
    
    Subclasses to this
    ----------------------
    \\
    
    """
    
    def plot_var(self, var, grid='on', y_lim=(None,None)):
                
        # Notation simplification
        t = self.t_pos
        y = self.__dict__[var]

        fig = plt.figure(figsize=(12.3,5))
        ax = fig.add_subplot(1,1,1)
        ax.plot(t, y, ls='solid')
        ax.set_ylabel(self.plot_labels[var][0])
        ax.set_title(self.plot_labels[var][1])   
        
        if grid == 'on':
            plt.minorticks_on()
            plt.grid(True)
            ax.xaxis.grid(True, which='minor')
            
        ax.set_ylim(
            ymin = y_lim[0], 
            ymax = y_lim[1])
        
        plt.tight_layout()
    
    
    def plot_Commands(self, y_lim_sx=(None,None), y_lim_dx=(None,None),  show_grid=False, legend_loc='best', export_pdf=True):        
        fig = plt.figure(figsize=(12.3,5))
        
        # Surface commands, left y axis
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_fcs, self.delta_a, ls='solid', color='r', label=r'$\delta_a$')
        ax1a.plot(self.t_fcs, self.delta_e, ls='solid', color='g', label=r'$\delta_e$')
        ax1a.plot(self.t_fcs, self.delta_r, ls='solid', color='b', label=r'$\delta_r$')

        ax1a.set_title("Commands")    
        ax1a.set_xlabel(r'$t$ (s)')
        ax1a.set_ylabel(r'$\delta_a$ , $\delta_e$ , $\delta_r$ (°)')
        
        ax1a.set_ylim(
            ymin = -1 + np.floor(min(list(self.delta_a)+
                                     list(self.delta_e)+
                                     list(self.delta_r))
                                ) if y_lim_sx[0] == None 
                                  else y_lim_sx[0],
            ymax = +1 + np.ceil(max(list(self.delta_a)+
                                    list(self.delta_e)+
                                    list(self.delta_r))
                                ) if y_lim_sx[1] == None 
                                  else y_lim_sx[1]
        )
        
        ax1a.grid(show_grid, which='both')
        
        # Throttle command, right y axis
        ax1b = ax1a.twinx()
        ax1b.plot(self.t_fcs, self.delta_t, ls='solid', color='0.65', label=r'$\delta_t$')

        ax1b.set_ylabel(r'$\delta_t$ (-)')
        ax1b.set_ylim(
            ymin = -0.05 if y_lim_dx[0] == None else y_lim_dx[0],
            ymax = 1     if y_lim_dx[1] == None else y_lim_dx[1])

        handlesa, labelsa = ax1a.get_legend_handles_labels()
        handlesb, labelsb = ax1b.get_legend_handles_labels()
        ax1a.legend(handlesa+handlesb, labelsa+labelsb, 
                    ncol=4, 
                    loc=legend_loc)
                
        plt.tight_layout()
        
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_Commands.pdf')
        
        
    def plot_AngularVel(self, y_lim_sx=(None,None),   show_grid=False, legend_loc='best', export_pdf=True):
        fig = plt.figure(figsize=(12.3,5))

        # Angular velocities
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_vel, self.p_deg, color='r', label=r'$p$')
        ax1a.plot(self.t_vel, self.q_deg, color='g', label=r'$q$')
        ax1a.plot(self.t_vel, self.r_deg, color='b', label=r'$r$')

        ax1a.set_title("Angular velocities")    
        ax1a.set_xlabel(r'$t$ (s)')
        ax1a.set_ylabel(r'$p$ , $q$ , $r$ (°/s)')

        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
            
        ax1a.grid(show_grid, which='both')

        handles, labels = ax1a.get_legend_handles_labels()
        ax1a.legend(handles, labels, 
                    ncol=3, loc=legend_loc)

        plt.tight_layout()
        
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_AngularVel.pdf')
        
        
    def plot_EulerAng(self, y_lim_sx=(None,None), y_lim_dx=(None,None),   show_grid=False, legend_loc='best', export_pdf=True):
        fig = plt.figure(figsize=(12.3,5))

        # Euler Angles Phi and Theta, left y axis
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_att, self.phi_deg,   color='r', label=r"$\phi$")
        ax1a.plot(self.t_att, self.theta_deg, color='g', label=r"$\theta$")

        ax1a.set_title("Euler angles")    
        ax1a.set_xlabel(r'$t$ (s)')
        ax1a.set_ylabel(r'$\phi$ , $\theta$ (°)')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        # Euler Angle Psi, right y axis
        ax1b = ax1a.twinx()
        ax1b.plot(self.t_att, self.psi_deg, color='b', label=r"$\psi$")

        ax1b.set_ylabel(r'$\psi$ (°)')
        ax1b.set_ylim(
            ymin = y_lim_dx[0], 
            ymax = y_lim_dx[1])

        handlesa, labelsa = ax1a.get_legend_handles_labels()
        handlesb, labelsb = ax1b.get_legend_handles_labels()
        ax1a.legend(handlesa+handlesb, labelsa+labelsb,
                    ncol=3, loc=legend_loc)

        plt.tight_layout()
        
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_EulerAng.pdf')
            
        
    def plot_AlphaBetaV(self, y_lim_sx=(None,None), y_lim_dx=(None,None),   show_grid=False, legend_loc='best', export_pdf=True):
        fig = plt.figure(figsize=(12.3,5))

        # Alpha and Beta, left y axis
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_aero, self.alpha_deg,   color='g', label=r'$\alpha$')
        ax1a.plot(self.t_aero, self.beta_deg,    color='b', label=r'$\beta$')
        
        ax1a.set_title("Angles of attack and sideslip, velocity")    
        ax1a.set_xlabel('$t$ (s)')
        ax1a.set_ylabel(r'$\alpha$ , $\beta$ (°)')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        # Velocity along the trajectory, right y axis
        ax1b = ax1a.twinx()
        ax1b.plot(self.t_vel, self.V_kts, color='k', label="$V$")

        ax1b.set_ylabel('$V$ (kts)')
        ax1b.set_ylim(
            ymin = y_lim_dx[0], 
            ymax = y_lim_dx[1])

        handlesa, labelsa = ax1a.get_legend_handles_labels()
        handlesb, labelsb = ax1b.get_legend_handles_labels()
        ax1a.legend(handlesa+handlesb, labelsa+labelsb, 
                    ncol=3, loc=legend_loc)

        plt.tight_layout()
        
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_AlphaBetaV.pdf')
            
            
    def plot_gamma(self, y_lim_sx=(None,None), show_grid=False, export_pdf=True):
        
        fig = plt.figure(figsize=(12.3,5))
                
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_aero, self.gamma_deg, ls='solid', color='g', label=r'$\gamma$')

        ax1a.set_title("Flight path angle")
        ax1a.set_xlabel(r'$t$ (s)')
        ax1a.set_ylabel(r'$\gamma$ (°)')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        plt.tight_layout()

        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_gamma.pdf')
            
        
    def plot_AltitudeVelocity(self, y_lim_sx=(None,None), y_lim_dx=(None,None), show_grid=False, legend_loc='best', export_pdf=True):
        fig = plt.figure(figsize=(12.3,5))
        
        # Altitude, left y axis
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_pos, self.h_sl_ft, ls='solid', color='b', label='$h_{\mathrm{SL}}$')
    
        ax1a.set_title("Altitude above Sea Level and velocity")    
        ax1a.set_xlabel('$t$ (s)')
        ax1a.set_ylabel('$h_{\mathrm{SL}}$ (ft)')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        # Velocity, right y axis
        ax1b = ax1a.twinx()
        ax1b.plot(self.t_vel, self.V_kts, ls='solid', color='k', label='$V$')
        
        ax1b.set_ylabel('$V$ (kts)')
        ax1b.set_ylim(
            ymin = y_lim_dx[0], 
            ymax = y_lim_dx[1])
    
        handlesa, labelsa = ax1a.get_legend_handles_labels()
        handlesb, labelsb = ax1b.get_legend_handles_labels()
        ax1a.legend(handlesa+handlesb, labelsa+labelsb, 
                    ncol=3, loc=legend_loc)

        plt.tight_layout()
        
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_AltitudeVelocity.pdf')
            
    
    def plot_LatitLongit(self, y_lim_sx=(None,None), y_lim_dx=(None,None),   show_grid=False, legend_loc='best', export_pdf=True):
        fig = plt.figure(figsize=(12.3,5))
        
        # Latitude, left y axis
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_pos, self.lat_gc_deg, color='r', label='Lat, $\lambda$')
    
        ax1a.set_title("Geocentric Coordinates")    
        ax1a.set_xlabel('$t$ (s)')
        ax1a.set_ylabel('$\lambda$ (°)')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        ax1a.yaxis.set_major_formatter(plttick.FormatStrFormatter('%.3f'))
        
        # Longitude, right y axis
        ax1b = ax1a.twinx()
        ax1b.plot(self.t_pos, self.lon_gc_deg, color='g', label='Lon, $L$')
        
        ax1b.set_ylabel('$L$ (°)')
        
        ax1b.set_ylim(
            ymin = y_lim_dx[0], 
            ymax = y_lim_dx[1])
    
        ax1b.yaxis.set_major_formatter(plttick.FormatStrFormatter('%.3f'))
        
        handlesa, labelsa = ax1a.get_legend_handles_labels()
        handlesb, labelsb = ax1b.get_legend_handles_labels()
        ax1a.legend(handlesa+handlesb, labelsa+labelsb, 
                    ncol=3, loc=legend_loc)

        plt.tight_layout()
        
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_LatitLongit.pdf')
            
 
    def plot_AdvRatioCT(self, y_lim_sx=(None,None), y_lim_dx=(None,None),   show_grid=False, legend_loc='best', export_pdf=True):
        fig = plt.figure(figsize=(12.3,5))
    
        # Advance ratio, left y axis
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_prop, self.adv_ratio, ls='solid', color='m', label='$\gamma$')

        ax1a.set_title("Advance ratio and thrust coefficient")    
        ax1a.set_xlabel('$t$ (s)')
        ax1a.set_ylabel('$\gamma$')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        # Thrust coefficient, right y axis
        ax1b = ax1a.twinx()
        ax1b.plot(self.t_prop, self.thr_coeff, ls='solid', color='0.65', label='$C_{T}$')
        ax1b.set_ylabel('$C_{T}$')
        
        ax1b.set_ylim(
            ymin = y_lim_dx[0], 
            ymax = y_lim_dx[1])
        
        handlesa, labelsa = ax1a.get_legend_handles_labels()
        handlesb, labelsb = ax1b.get_legend_handles_labels()
        ax1b.legend(handlesa+handlesb, labelsa+labelsb, 
                    ncol=2, loc=legend_loc)
        
        plt.tight_layout()
        
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_AdvRatioCT.pdf')


    def plot_PropRPMV(self, y_lim_sx=(None,None), y_lim_dx=(None,None),   show_grid=False, legend_loc='best', export_pdf=True):
        fig = plt.figure(figsize=(12.3,5))
        
        # Propeller rounds-per-minute, left y axis
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_prop, self.prop_rpm, color='b', label='$N$')

        ax1a.set_title("Propeller rounds-per-minute")    
        ax1a.set_xlabel('$t$ (s)')
        ax1a.set_ylabel('$N$ (rpm)')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        # Velocity, right y axis
        ax1b = ax1a.twinx()
        ax1b.plot(self.t_vel, self.V_kts, color='k', label='$V$')
        ax1b.set_ylabel('$V$ (kts)')
        
        ax1b.set_ylim(ymin = y_lim_dx[0], 
                      ymax = y_lim_dx[1])

        handlesa, labelsa = ax1a.get_legend_handles_labels()
        handlesb, labelsb = ax1b.get_legend_handles_labels()
        ax1b.legend(handlesa+handlesb, labelsa+labelsb, 
                    ncol=2, loc=legend_loc)
        
        plt.tight_layout()
        
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_PropRPMV.pdf')


    def plot_ThrustPow(self, y_lim_sx=(None,None), y_lim_dx=(None,None),   show_grid=False, legend_loc='best', export_pdf=True):
        fig = plt.figure(figsize=(12.3,5))
        
        # Thrust, left y axis
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_prop, self.thr_lbf, color='0.65', label='$T$')

        ax1a.set_title("Thrust and power")    
        ax1a.set_xlabel('$t$ (s)')
        ax1a.set_ylabel('T (lbf)')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        # Power, right y axis
        ax1b = ax1a.twinx()    
        ax1b.plot(self.t_prop, self.pow_hp, color=(1,0.85,0.28), label='$\Pi$')

        ax1b.set_ylabel('$\Pi$ (hp)')
        
        ax1b.set_ylim(
            ymin = y_lim_dx[0], 
            ymax = y_lim_dx[1])

        handlesa, labelsa = ax1a.get_legend_handles_labels()
        handlesb, labelsb = ax1b.get_legend_handles_labels()
        ax1b.legend(handlesa+handlesb, labelsa+labelsb, 
                    ncol=2, loc=legend_loc)

        plt.tight_layout()

        # Export
        if dest_folder != None: plt.savefig(self.path+'plot_ThrustPow.pdf')
         
    
    def plot_Lift(self, units='N', y_lim_sx=(None,None),   show_grid=False, export_pdf=True):
        
        # Choose units of measurement
        if units == 'N':
            Lift = self.L_N
        elif units == 'lbf':
            Lift = self.L_lbf
        elif units == 'kgf':
            Lift = self.L_kgf
        
        fig = plt.figure(figsize=(12.3,5))
                
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_aero, Lift, ls='solid', color='b', label=r'$\bar{q}\, S\, C_{L}$')

        ax1a.set_title("Lift")
        ax1a.set_xlabel(r'$t$ (s)')
        ax1a.set_ylabel(r'L (%s)' % units)
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        plt.tight_layout()

        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_Lift.pdf')
            
    
    def plot_hoverb(self, y_lim_sx=(None,None),   show_grid=False, legend_loc='best', export_pdf=True):
   
        fig = plt.figure(figsize=(12.3,5))
      
        ax1a = fig.add_subplot(1,1,1)
        ax1a.plot(self.t_aero, self.h_b_cg, ls='solid', color=(0.4,0,0.8), label=r'$h_{\mathrm{cg}}/b$')
        ax1a.plot(self.t_aero, self.h_b_mac, ls='solid', color=(1,0,0.5), label=r'$h_{\mathrm{mac}}/b$')

        ax1a.set_title("Adimensional distance from the ground")
        ax1a.set_xlabel(r'$t$ (s)')
        ax1a.set_ylabel('(-)')
        
        ax1a.set_ylim(
            ymin = y_lim_sx[0], 
            ymax = y_lim_sx[1])
        
        ax1a.grid(show_grid, which='both')
        
        handles, labels = ax1a.get_legend_handles_labels()
        ax1a.legend(handles, labels, ncol=2, loc=legend_loc)

        plt.tight_layout()

        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_hoverb.pdf')
            

    def plot_GroundTrack(self,units='m', show_grid=False, n_arrows=10, arrow_size=2, export_pdf=True):
    
        import plotting_utilities as plut

        # Choose units to view data
        if units == 'm':
            East  = self.Ynea_m
            North = self.Xnea_m

        elif units == 'ft':
            East  = self.Ynea_ft
            North = self.Xnea_ft
        
        else: print('Error: invalid unit. Only "m" or "ft" allowed')

        fig = plt.figure(figsize=(12.3,12.3))

        # Ground track
        ax1 = fig.add_subplot(1,1,1)
        # Data
        traj2D = ax1.plot(East, North, ls='solid', color='#006633', label='')      
        # Start marker
        ax1.plot(East[0], North[0],   ls='solid', color='#006633',                                       
                 marker='o', markersize=4*arrow_size, markerfacecolor='#006633', markeredgecolor='#006633')   
        # End marker
        ax1.plot(East[-1], North[-1], ls='solid', color='#006633',                                       
                 marker='o', markersize=4*arrow_size, markerfacecolor='w', markeredgecolor='#006633')  
        # Add arrows along line
        plut.add_arrow_to_line2D(ax1,traj2D,                                                                  
                                 arrow_locs=np.linspace(1/(n_arrows+1),n_arrows/(n_arrows+1),n_arrows),
                                 arrowsize=arrow_size) 

        ax1.set_title("Ground Track, to scale")   
        ax1.set_xlabel('East ('+units+')')
        ax1.set_ylabel('North ('+units+')')
        ax1.minorticks_on()
        
        ax1.grid(show_grid, which='both')

        plt.axis('equal')
        plt.axis([1.02*min(East), 1.02*max(East), 1.02*min(North), 1.02*max(North)])
               
        plt.tight_layout()
                
        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_GroundTrack.pdf')
            
        
    def plot_traj3D_in_NEA(self, units='m', X_proj='N', Y_proj='E', from_ground=True, view=(45,-45),
                            to_scale='XY', mrk_size=80, export_pdf=True):

        """
        Arguments
        ---------------------------
        X_proj     = string,              'N' or 'S': indicates the direction where to project the trajectory
        Y_proj     = string,              'E' or 'W': indicates the direction where to project the trajectory
        view       = 2x1 tuple,           sets the view point in terms of Elevation and Azimuth
        to_scale   = string,              'XYZ' or 'XY': set the Z axis scale
        mrk_size   = int                  set marker size
        export_pdf = bool                 True or False: export a pdf file in the default output folder
        """

        from mpl_toolkits.mplot3d import Axes3D
        import plotting_utilities as plut
        
        # Choose units to view data
        if units == 'm':
            East  = self.Ynea_m
            North = self.Xnea_m
            Altit = self.Znea_m

        elif units == 'ft':
            East  = self.Ynea_ft
            North = self.Xnea_ft
            Altit = self.Znea_ft
        
        else: print('Error: invalid unit. Only "m" or "ft" allowed')
            
        fig = plt.figure(figsize=(12.3,10))
        ax  = fig.add_subplot(1,1,1,projection='3d')

        # 3D trajectory
        ax.plot(   North,     East,     Altit,     color='#006633', ls='solid', linewidth=2)
        ax.scatter(North[0],  East[0],  Altit[0],  marker='o',      s=mrk_size, c='#006633', label='Start')
        ax.scatter(North[-1], East[-1], Altit[-1], marker=(5,0),    s=mrk_size, c='#006633', label='End')

                
        # Axis limits through escamotage
        # Create cubic bounding box to simulate equal aspect ratio
        max_range = np.array([North.max()-North.min(), East.max()-East.min(), Altit.max()-Altit.min()]).max()
        Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(North.max()+North.min())
        Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(East.max()+East.min())
        Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Altit.max()+Altit.min())
        
        if from_ground == True: Zb = Zb -Zb.min() # set z_axis inferior limit to 0
            
        if to_scale == 'XYZ':
            for xb, yb, zb in zip(Xb, Yb, Zb):
                ax.plot([xb], [yb], [zb], 'w')
        elif to_scale == 'XY':
            for xb, yb in zip(Xb, Yb):
                ax.plot([xb], [yb], 'w')
        
        XMIN, YMIN, ZMIN = ax.get_xlim().min(), ax.get_ylim().min(), ax.get_zlim().min()
        XMAX, YMAX, ZMAX = ax.get_xlim().max(), ax.get_ylim().max(), ax.get_zlim().max()
        
        if from_ground == True: ZMIN = 0 # set z_axis inferior limit to 0

        ax.set_xlim3d([XMIN, XMAX])
        ax.set_ylim3d([YMIN, YMAX])
        ax.set_zlim3d([ZMIN, ZMAX])

        # Ground track
        ax.plot(   North,     East,     np.ones(len(Altit))*ZMIN,    color='k', ls='dashed',  linewidth=1) 
        ax.scatter(North[0],  East[0],  ZMIN,                        c='w',     marker='o',   s=0.8*mrk_size)
        ax.scatter(North[-1], East[-1], ZMIN,                        c='w',     marker=(5,0), s=0.8*mrk_size)

        # altitude on plane parallel to YZ, Northern or Southern wall of plot
        if X_proj == 'S': 
            ax.plot(   np.ones(len(North))*XMIN, East,      Altit,     color='0.65', ls='dashed',   linewidth=1)
            ax.scatter(XMIN,                     East[0] ,  Altit[0],  c='w',        marker='o',    s=0.8*mrk_size)
            ax.scatter(XMIN,                     East[-1] , Altit[-1], c='w',        marker=(5,0),  s=0.8*mrk_size)
        elif X_proj == 'N':
            ax.plot(   np.ones(len(North))*XMAX, East,      Altit,     color='0.65', ls='dashed',  linewidth=1)
            ax.scatter(XMAX,                     East[0] ,  Altit[0],  c='w',        marker='o',   s=0.8*mrk_size) 
            ax.scatter(XMAX,                     East[-1] , Altit[-1], c='w',        marker=(5,0), s=0.8*mrk_size)

        # altitude on plane parallel to XZ, Eastern or Western wall of plot
        if Y_proj == 'W': 
            ax.plot(   North,     np.ones(len(East))*YMIN, Altit,     color='0.65', ls='dashed',  linewidth=1)
            ax.scatter(North[0],  YMIN,                    Altit[0],  c='w',        marker='o',   s=0.8*mrk_size)
            ax.scatter(North[-1], YMIN,                    Altit[-1], c='w',        marker=(5,0), s=0.8*mrk_size)
        elif Y_proj == 'E':
            ax.plot(   North,     np.ones(len(East))*YMAX, Altit,     color='0.65', ls='dashed',  linewidth=1)
            ax.scatter(North[0],  YMAX,                    Altit[0],  c='w',        marker='o',   s=0.8*mrk_size)
            ax.scatter(North[-1], YMAX,                    Altit[-1], c='w',        marker=(5,0), s=0.8*mrk_size)

        # Labels and legend
        ax.set_xlabel('\n'+'North ('+units+')',            linespacing=3.5)
        ax.set_ylabel('\n'+'East ('+units+')',             linespacing=3.5)
        ax.set_zlabel('\n'+r'$h_\mathrm{SL}$ ('+units+')', linespacing=3.5)

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, 
                  ncol=1, loc='best')
        
        # Axis visualization and scale
        ax.invert_xaxis()
        ax.view_init(view[0],view[1]) # Elevation, Azimuth
        ax.set_title("Trajectory, to scale" if to_scale == 'XYZ' else "Trajectory, altitude not to scale")
        
        plt.tight_layout()

        # Export
        if export_pdf == True: plt.savefig(self.path+'plot_traj3D_NEA.pdf')