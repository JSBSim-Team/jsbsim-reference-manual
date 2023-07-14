import numpy as np
from pint import UnitRegistry;
unit = UnitRegistry()

class ACDataOut:
    
    """
    This class extracts 1d arrays from JSBSim output files,
    and manipulates them to obtain new useful data.
    
    Superclasses to this
    ----------------------
    \\
    
    
    Subclasses to this
    ----------------------
    ACDataPlots
    
    """
    
    def __init__(self,ac_name,out_path):
        
        """
        Class constructor requires:
        - name of the aircraft (the same string as in the output .csv files)
        - output folder path
        """
        
        self.name = ac_name
        self.path = out_path
        
        # Accelerations
        self.accel = np.genfromtxt(self.path+self.name+'_accelerations.csv', delimiter=',', skip_header=1)
        
        # Aerodynamics
        self.aerod = np.genfromtxt(self.path+self.name+'_aero.csv', delimiter=',', skip_header=1)
        self.t_aero      = self.aerod[:,0]
        self.alpha_deg   = self.aerod[:,3]
        self.beta_deg    = self.aerod[:,4]
        self.alpha_rad   = (self.alpha_deg*unit.deg).to(unit.rad).magnitude
        self.beta_rad    = (self.beta_deg*unit.deg).to(unit.rad).magnitude
        self.L_lbf       = self.aerod[:,21]                                # Lift in lbf
        self.L_kgf       = (self.L_lbf*unit.lbf).to(unit.kgf).magnitude    # Lift in kgf
        self.L_N         = (self.L_lbf*unit.lbf).to(unit.N).magnitude      # Lift in N
        self.h_b_cg      = self.aerod[:,42]
        self.h_b_mac     = self.aerod[:,43]
        self.ge_lift_fac = self.aerod[:,44]

        # Animations
        #self.animt = np.genfromtxt(self.path+self.name+'_animation.csv', delimiter=',', skip_header=1)
        
        # Attitude
        self.attit = np.genfromtxt(self.path+self.name+'_attitude.csv', delimiter=',', skip_header=1)
        self.t_att     = self.attit[:,0]
        self.phi_rad   = self.attit[:,1]
        self.theta_rad = self.attit[:,2]
        self.psi_rad   = self.attit[:,3]
        self.phi_deg   = ((self.phi_rad*unit.rad).to(unit.deg)).magnitude
        self.theta_deg = ((self.theta_rad*unit.rad).to(unit.deg)).magnitude
        self.psi_deg   = ((self.psi_rad*unit.rad).to(unit.deg)).magnitude
        self.gamma_rad = self.attit[:,7]
        self.gamma_deg = (self.gamma_rad*unit.rad).to(unit.deg).magnitude
        
        # Flight Control System
        self.fcsys = np.genfromtxt(self.path+self.name+'_fcs.csv', delimiter=',', skip_header=1)
        self.t_fcs   = self.fcsys[:,0]
        self.delta_a = self.fcsys[:,18]
        self.delta_e = self.fcsys[:,6] # equivalent deflection, including tab (NB tab == fcs/pitch-trim-cmd-norm)
        self.delta_r = self.fcsys[:,9]
        self.delta_t = self.fcsys[:,20]
        self.delta_e_eff_rad = self.fcsys[:,25] # effective deflection, not including tab
        self.delta_e_eff_deg = (self.delta_e_eff_rad*unit.rad).to(unit.deg).magnitude
        self.delta_tab_rad = self.fcsys[:,27]
        self.delta_tab_deg = (self.delta_tab_rad*unit.rad).to(unit.deg).magnitude
        
        # Forces
        #self.force = np.genfromtxt(self.path+self.name+'_forces.csv', delimiter=',', skip_header=1)
        
        # Position
        self.posit = np.genfromtxt(self.path+self.name+'_position.csv', delimiter=',', skip_header=1)
        self.t_pos            = self.posit[:,0]
        self.h_sl_ft          = self.posit[:,1]
        self.h_sl_m           = (self.h_sl_ft*unit.ft).to(unit.m).magnitude
        self.lat_gc_deg       = self.posit[:,7]
        self.lat_gc_rad       = (self.lat_gc_deg*unit.deg).to(unit.rad).magnitude
        self.lon_gc_deg       = self.posit[:,9]
        self.lon_gc_rad       = (self.lon_gc_deg*unit.deg).to(unit.rad).magnitude
        self.active_wp        = self.posit[:,15]
        self.active_wp_switch = np.insert(np.diff(self.active_wp)[1:],0,[0,0])
        
        # Propulsion
        self.propu = np.genfromtxt(self.path+self.name+'_propulsion.csv', delimiter=',', skip_header=1)
        self.t_prop    = self.propu[:,0]
        self.adv_ratio = self.propu[:,9]
        self.thr_coeff = self.propu[:,11]
        self.prop_rpm  = self.propu[:,12]
        self.thr_lbf   = self.propu[:,16]
        self.pow_hp    = self.propu[:,18]
        
        # Velocities
        self.veloc = np.genfromtxt(self.path+self.name+'_velocities.csv', delimiter=',', skip_header=1)
        self.t_vel = self.veloc[:,0]
        self.p_rad = self.veloc[:,4]
        self.q_rad = self.veloc[:,5]
        self.r_rad = self.veloc[:,6]
        self.p_deg = (self.p_rad*unit.rad).to(unit.deg).magnitude
        self.q_deg = (self.q_rad*unit.rad).to(unit.deg).magnitude
        self.r_deg = (self.r_rad*unit.rad).to(unit.deg).magnitude
        self.V_fts = self.veloc[:,17]
        self.V_kts = (self.V_fts*(unit.ft/unit.s)).to(unit.knots).magnitude
        
        self.plot_labels = {
            't_aero' :      (r'$t$ (s)', 'Time'), 
            't_att':        (r'$t$ (s)', 'Time'),
            't_fcs':        (r'$t$ (s)', 'Time'),
            't_pos':        (r'$t$ (s)', 'Time'),
            't_prop':       (r'$t$ (s)', 'Time'),
            't_vel':        (r'$t$ (s)', 'Time'),
            'alpha_deg':    (r'$\alpha$ (deg)', 'Angle of attack'),
            'alpha_rad':    (r'$\alpha$ (rad)', 'Angle of attack'),
            'beta_deg':     (r'$\beta$ (deg)',  'Angle of sideslip'),
            'beta_rad':     (r'$\beta$ (rad)',  'Angle of sideslip'),
            'L_lbf':        (r'$L$ (lbf)', 'Lift'),
            'L_kgf':        (r'$L$ (kgf)', 'Lift'),
            'L_N':          (r'$L$ (N)',   'Lift'),
            'h_b_cg':       (r'$h/b_{cg}$', 'Adimensional altitude of CG'),
            'h_b_mac':      (r'$h/b_{mac}$', 'Adimensional altitude of mac'),
            'ge_lift_fac':  (r'$f_{ge}$', 'Ground effect factor'),
                
            'phi_rad':      (r'$\phi$ (rad)', 'Third Euler Angle'),
            'phi_deg':      (r'$\phi$ (deg)', 'Third Euler Angle'),
            'theta_rad':    (r'$\theta$ (rad)', 'Second Euler Angle'),
            'theta_deg':    (r'$\theta$ (deg)', 'Second Euler Angle'),
            'psi_rad':      (r'$\psi$ (rad)', 'First Euler Angle'),
            'psi_deg':      (r'$\psi$ (deg)', 'First Euler Angle'),
            'gamma_deg':    (r'$\gamma$ (deg)', 'Flight Path Angle'),
                
            'delta_a':          (r'$\delta_a$ (deg)', 'Aileron command'),
            'delta_e':          (r'$\delta_e$ (deg)', 'Elevator command'),
            'delta_r':          (r'$\delta_r$ (deg)', 'Rudder command'),
            'delta_t':          (r'$\delta_t$ (deg)', 'Throttle command'),
            'delta_e_eff_deg':  (r'$\delta_{e,\mathrm{eff}}$ (deg)', 'Effective elevator command'),
            'delta_tab_deg':    (r'$\delta_\mathrm{tab}$ (deg)', 'Tab deflection'),
                
            'h_sl_ft':      (r'$h_{SL}$ (ft)', 'Altitude above Sea Level'),
            'h_sl_m':       (r'$h_{SL}$ (m)', 'Altitude above Sea Level'),
            'lat_gc_deg':   (r'$\lambda$ (deg)', 'Geocentric latitude'),
            'lat_gc_rad':   (r'$\lambda$ (rad)', 'Geocentric latitude'),
            'lon_gc_deg':   (r'$L$ (deg)', 'Geocentric longitude'),
            'lon_gc_rad':   (r'$L$ (rad)', 'Geocentric longitude'),
                
            'adv_ratio':    (r'$\gamma_{p}$ (-)', 'Propeller advance ratio'),
            'thr_coeff':    (r'$C_{T}$ (-)', 'Thrust coefficient'),
            'prop_rpm':     (r'$N$ (rpm)', 'Propeller rounds per minute'),
            'thr_lbf':      (r'$T$ (lbf)', 'Thrust'),
            'pow_hp':       (r'$\Pi$ (hp)', 'Power'),
                
            'p_rad':        (r'$p$ (rad/s)', 'Roll angular velocity'),
            'p_deg':        (r'$p$ (deg/s)', 'Roll angular velocity'),
            'q_rad':        (r'$q$ (rad/s)', 'Pitch angular velocity'),
            'q_deg':        (r'$q$ (deg/s)', 'Pitch angular velocity'),
            'r_rad':        (r'$r$ (rad/s)', 'Yaw angular velocity'),
            'r_deg':        (r'$r$ (deg/s)', 'Yaw angular velocity'),
            'V_fts':        (r'$V$ (ft/s)', 'Velocity'),
            'V_kts':        (r'$V$ (kts)', 'Velocity'),
            
            'Rnea_m':       (r'$R_{NEA}$ (m)', 'Vector position in NEA ref.'),
            'Rnea_ft':      (r'$R_{NEA}$ (ft)', 'Vector position in NEA ref.'),
            'Xnea_m':       (r'$X_{NEA}$ (m)', 'North coordinate'),
            'Xnea_ft':      (r'$X_{NEA}$ (ft)', 'North coordinate'),
            'Ynea_m':       (r'$Y_{NEA}$ (m)', 'East coordinate'),
            'Ynea_ft':      (r'$Y_{NEA}$ (ft)', 'East coordinate'),
            'Znea_m':       (r'$Z_{NEA}$ (m)', 'Altitude'),
            'Znea_ft':      (r'$Z_{NEA}$ (ft)', 'Altitude'),
            }
            
            
    def __str__(self):
        return 'Aircraft: %s \nData at : %s' %(self.name, self.path)
    
    
    def get_groundtrack_in_ECEF(self):
        
        """
        Converts latitude and longitude time histories (in radians) to the time histories of postion vector 
        components in the ECEF reference frame. Doesn't need altitude.
        """
        
        from numpy import array, cos, sin
        
        # Earth radius (assumed to be equal to MSL)
        R_E = 6371e3 # m
        
        # Variables' name abbreviations
        lat = self.lat_gc_rad
        lon = self.lon_gc_rad
        
        # Time history of the A/C position in ECEF system
        R = R_E * array([cos(lat)*cos(lon),  # X ECEF
                         cos(lat)*sin(lon),  # Y ECEF
                         sin(lat)])          # Z ECEF
        
        self.Recef_m  = R
        self.Recef_ft = (R*unit.m).to(unit.ft).magnitude
        
    
    def get_traj_in_NEA(self, lat0=None, lon0=None, flat=1):
        
        """
        Converts the time histories of geocentric latitude, longitude and altitude above Sea Level
        to the time histories of North, East and altitude. The latter are expressed in a reference 
        frame whose origin is in the initial position (L,l) of the simulation, but at Mean Sea Level altitude.
        Earth is considered flat unless specified.

        Inputs
        -----------
        self.lat_gc_rad  = 1d array, rad
        self.lon_gc_rad  = 1d array, rad
        self.h_sl_m      = 1d array, m
        
        Arguments
        -----------
        flat = bool (default is: 1)

        Outputs
        -----------
        self.Rnea_m,  self.Xnea_m,  self.Ynea_m,  self.Znea_m
        self.Rnea_ft, self.Xnea_ft, self.Ynea_ft, self.Znea_ft
        
        
        Returns
        -----------
        //

        Notes
        -----------
        Suppose h_sl is constant due to A/C altitude hold.
        With flat-Earth model implemented, like it is done here by default, altitude will actually remain constant
        also in the NED reference frame. If Earth were considered round, altitude would be expected to remain constant 
        with respect to Earth surface: therefore, actual altitude in the NED reference frame (which is fixed to the initial
        position of the aircraft) would clearly decrease because of Earth's curvature.

        """
        
        from numpy import array, cos, sin, arcsin, arctan2
        
        self.get_groundtrack_in_ECEF()
        
        # Earth radius (assumed to be equal to MSL)
        R_E = 6371e3 # m
        
        # Variables' name abbreviations
        lat = self.lat_gc_rad
        lon = self.lon_gc_rad
        R   = self.Recef_m
        
        if lat0 is None and lon0 is None:
            lat0 = self.lat_gc_rad[0]
            lon0 = self.lon_gc_rad[0]
        else:
            pass
        
        R0 = R_E * array([cos(lat0)*cos(lon0),  # X ECEF
                          cos(lat0)*sin(lon0),  # Y ECEF
                          sin(lat0)])           # Z ECEF
        
        DR = array([R[i,:]-R0[i] for i in range(len(R0))])

        # Transformation matrix
        A = array([
            [-sin(lat0)*cos(lon0), -sin(lat0)*sin(lon0), +cos(lon0)],
            [-sin(lon0),              cos(lon0),             0     ],
            [-cos(lat0)*cos(lon0), -cos(lat0)*sin(lon0), -sin(lat0)]
        ])

        r = A.dot(DR)

        # Check Earth model to set correct altitude time history
        if    flat == 1: r[-1] = self.h_sl_m          # flat Earth
        else           : r[-1] = -r[-1]+self.h_sl_m   # non-flat Earth
        
        self.Rnea_m = r
        self.Xnea_m = r[0]
        self.Ynea_m = r[1]
        self.Znea_m = r[2]
        
        self.Rnea_ft = (self.Rnea_m*unit.m).to(unit.ft).magnitude
        self.Xnea_ft = self.Rnea_ft[0]
        self.Ynea_ft = self.Rnea_ft[1]
        self.Znea_ft = self.Rnea_ft[2]