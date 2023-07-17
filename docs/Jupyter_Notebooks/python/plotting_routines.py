import matplotlib.pyplot as plt
import matplotlib.ticker as plttick
import numpy as np

#
#=======================================================================================================================
#

def plot_Cmd_AngVel_EulerAng(data_fcs, data_vel, data_att, dest_folder=None):
    
    """
    Input units of measurement
    ---------------------------
    Time                = s
    Surface deflections = deg
    Throttle            = 1
    Angular velocities  = rad/s
    Euler angles        = rad
    """
    
    # Variables assignment
    t_fcs   = data_fcs[:,0]
    delta_a = data_fcs[:,18]
    delta_e = data_fcs[:,6]
    delta_r = data_fcs[:,9]
    delta_t = data_fcs[:,20]
    
    t_vel   = data_vel[:,0]
    p_rad   = data_vel[:,4]
    q_rad   = data_vel[:,5]
    r_rad   = data_vel[:,6]
    
    t_att   = data_att[:,0]
    phi_rad = data_att[:,1]
    the_rad = data_att[:,2]
    psi_rad = data_att[:,3]
    
    fig = plt.figure(figsize=(12.3,15))
    
    
    # Commands
    ax1a = fig.add_subplot(3,1,1)
    ax1a.plot(t_fcs, delta_a,  ls='solid', color='r', label=r'$\delta_a$')
    ax1a.plot(t_fcs, delta_e,  ls='solid', color='g', label=r'$\delta_e$')
    ax1a.plot(t_fcs, delta_r,  ls='solid', color='b', label=r'$\delta_r$')
    
    ax1a.set_title("Commands")    
    ax1a.set_xlabel(r'$t$ (s)')
    ax1a.set_ylabel(r'$\delta_a$ , $\delta_e$ , $\delta_r$ (°)')
    ax1a.set_ylim(ymin=-1+np.floor(min(list(delta_a)+list(delta_e)+list(delta_r))),
                  ymax=1+np.ceil(max(list(delta_a)+list(delta_e)+list(delta_r))))
    
    
    ax1b = ax1a.twinx()
    ax1b.plot(t_fcs, delta_t, ls='solid', color='0.65', label=r'$\delta_t$')
    
    ax1b.set_ylabel(r'$\delta_t$')
    ax1b.set_ylim(ymax=1, ymin=-0.05)
    
    handlesa, labelsa = ax1a.get_legend_handles_labels()
    handlesb, labelsb = ax1b.get_legend_handles_labels()
    ax1a.legend(handlesa+handlesb, labelsa+labelsb, ncol=4, loc='best')
    

    # Angular velocities
    ax2 = fig.add_subplot(3,1,2)
    
    ax2.plot(t_vel, (180/np.pi)*p_rad, color='r', label=r'$p$')
    ax2.plot(t_vel, (180/np.pi)*q_rad, color='g', label=r'$q$')
    ax2.plot(t_vel, (180/np.pi)*r_rad, color='b', label=r'$r$')
    
    ax2.set_title("Angular velocities")    
    ax2.set_xlabel(r'$t$ (s)')
    ax2.set_ylabel(r'$p$ , $q$ , $r$ (°/s)')
  
    handles, labels = ax2.get_legend_handles_labels()
    ax2.legend(handles, labels, ncol=3, loc='best')
    
    
    # Euler angles
    ax3a = fig.add_subplot(3,1,3)
    
    ax3a.plot(t_att, (180/np.pi)*phi_rad, color='r', label=r"$\phi$")
    ax3a.plot(t_att, (180/np.pi)*the_rad, color='g', label=r"$\theta$")
    
    ax3a.set_title("Euler angles")    
    ax3a.set_xlabel(r'$t$ (s)')
    ax3a.set_ylabel(r'$\phi$ , $\theta$ (°)')
    
    
    ax3b = ax3a.twinx()
    ax3b.plot(t_att, (180/np.pi)*psi_rad, color='b', label=r"$\psi$")
    
    ax3b.set_ylabel(r'$\psi$ (°)')
    
    handlesa, labelsa = ax3a.get_legend_handles_labels()
    handlesb, labelsb = ax3b.get_legend_handles_labels()
    ax3b.legend(handlesa+handlesb, labelsa+labelsb, ncol=3, loc='best')
    
    plt.tight_layout()
    
    
    # Export
    if dest_folder != None:
        plt.savefig(dest_folder+'plot_Cmd_AngVel_EulerAng.pdf')
                       

            
def plot_Alfa_Beta_V(data_aero, data_vel, dest_folder=None):
    
    """
    Input units of measurement
    ---------------------------
    Time                = s
    Alfa, Beta          = deg
    Velocity            = ft/s
    """
    
    # Variables assignment
    t_aero   = data_aero[:,0]
    alfa_deg = data_aero[:,3]
    beta_deg = data_aero[:,4]
    
    t_vel    = data_vel[:,0]
    V_fts    = data_vel[:,17]
    V_kts    = 0.592484*V_fts
    
    fig = plt.figure(figsize=(12.3,5))
    
    
    # Alpha and beta
    ax1a = fig.add_subplot(1,1,1)
    
    ax1a.plot(t_aero, alfa_deg, ls='solid', color='g', label=r'$\alpha$')
    ax1a.plot(t_aero, beta_deg, ls='solid', color='b', label=r'$\beta$')
    
    ax1a.set_title("Angles of attack and sideslip, velocity")    
    ax1a.set_xlabel('$t$ (s)')
    ax1a.set_ylabel(r'$\alpha$ , $\beta$ (°)')
        
    # Velocity
    ax1b = ax1a.twinx()
    
    ax1b.plot(t_vel, V_kts, color='k', label="$V$")
    
    ax1b.set_ylabel('$V$ (kts)')
    
    handlesa, labelsa = ax1a.get_legend_handles_labels()
    handlesb, labelsb = ax1b.get_legend_handles_labels()
    ax1a.legend(handlesa+handlesb, labelsa+labelsb, ncol=3, loc='best')
    
    plt.tight_layout()
    
    # Export
    if dest_folder != None:
        plt.savefig(dest_folder+'plot_Alfa_Beta_V.pdf')
    
    
    
def plot_PosGeoc(data_pos, data_vel, dest_folder=None):
    
    """
    Input units of measurement
    ---------------------------
    Time                = s
    altitude            = ft
    Latitude, longitude = deg
    Velocity            = ft/s
    """
    
    # Variables assignment
    t_pos     = data_pos[:,0]
    hSL_ft    = data_pos[:,1]
    LatGC_deg = data_pos[:,7]
    LonGC_deg = data_pos[:,9]
    
    t_vel     = data_vel[:,0]
    V_fts     = data_vel[:,17]
    V_kts     = 0.592484*V_fts
    
    fig = plt.figure(figsize=(12.3,10))
    
    
    # Altitude and velocity
    ax1a = fig.add_subplot(2,1,1)
    ax1a.plot(t_pos, hSL_ft, ls='solid', color='b', label='$h_{\mathrm{SL}}$')
    
    ax1a.set_title("Altitude above Sea Level and velocity")    
    ax1a.set_xlabel('$t$ (s)')
    ax1a.set_ylabel('$h_{\mathrm{SL}}$ (ft)')
    
    ax1b = ax1a.twinx()
    ax1b.plot(t_vel, V_kts, ls='solid', color='k', label='$V$')
    ax1b.set_ylabel('$V$ (kts)')
    
    handlesa, labelsa = ax1a.get_legend_handles_labels()
    handlesb, labelsb = ax1b.get_legend_handles_labels()
    ax1b.legend(handlesa+handlesb, labelsa+labelsb, ncol=2, loc='best')
    
    
    # Latitude and longitude
    ax2a = fig.add_subplot(2,1,2)
    ax2a.plot(t_pos, LatGC_deg, color='r', label='Lat, $\lambda$')
    
    ax2a.set_title("Geocentric Coordinates")    
    ax2a.set_xlabel('$t$ (s)')
    ax2a.set_ylabel('$\lambda$ (°)')
    
    ax2a.yaxis.set_major_formatter(plttick.FormatStrFormatter('%.3f'))
    
    ax2b = ax2a.twinx() 
    ax2b.plot(t_pos, LonGC_deg, color='g', label='Lon, $L$')
    ax2b.set_ylabel('$L$ (°)')
    ax2b.yaxis.set_major_formatter(plttick.FormatStrFormatter('%.3f'))
    
    handlesa, labelsa = ax2a.get_legend_handles_labels()
    handlesb, labelsb = ax2b.get_legend_handles_labels()
    ax2b.legend(handlesa+handlesb, labelsa+labelsb, ncol=2, loc='best')

    plt.tight_layout()
    
    # Export
    if dest_folder != None:
        plt.savefig(dest_folder+'plot_PosGeoc.pdf')

        
    
def plot_EngineStatus(data_engine, data_vel, dest_folder=None):
    
    """
    Input units of measurement
    ---------------------------
    Time                        = s
    Advance ratio               = 1
    Thrust coefficient          = 1
    Propeller angular velocity  = rpm
    Thrust                      = lbf
    Power                       = hp
    Velocity                    = ft/s
    """
    
    # Variables assignment
    t_eng     = data_engine[:,0]
    adv_ratio = data_engine[:,9]
    thr_coeff = data_engine[:,11]
    prop_rpm  = data_engine[:,12]
    thr_lbf   = data_engine[:,16]
    pow_hp    = data_engine[:,18]
    
    t_vel     = data_vel[:,0]
    V_fts     = data_vel[:,17]
    V_kts     = 0.592484*V_fts
    
    fig = plt.figure(figsize=(12.3,15))
    
    
    # Advance ratio and thrust coefficient
    ax1a = fig.add_subplot(3,1,1)
    
    ax1a.plot(t_eng, adv_ratio, ls='solid', color='m', label='$\gamma$')
    
    ax1a.set_title("Advance ratio and thrust coefficient")    
    ax1a.set_xlabel('$t$ (s)')
    ax1a.set_ylabel('$\gamma$')
    
    ax1b = ax1a.twinx()
    ax1b.plot(t_eng, thr_coeff, ls='solid', color='0.65', label='$C_{T}$')
    ax1b.set_ylabel('$C_{T}$')
    
    handlesa, labelsa = ax1a.get_legend_handles_labels()
    handlesb, labelsb = ax1b.get_legend_handles_labels()
    ax1b.legend(handlesa+handlesb, labelsa+labelsb, ncol=2, loc='best')
    
    
    # Propeller rounds-er-minute
    ax2a = fig.add_subplot(3,1,2)
    ax2a.plot(t_eng, prop_rpm, color='b', label='$N$')
    
    ax2a.set_title("Propeller rounds-per-minute")    
    ax2a.set_xlabel('$t$ (s)')
    ax2a.set_ylabel('$N$ (rpm)')
    
    ax2b = ax2a.twinx()
    ax2b.plot(t_vel, V_kts, color='k', label='$V$')
    ax2b.set_ylabel('$V$ (kts)')
    
    handlesa, labelsa = ax2a.get_legend_handles_labels()
    handlesb, labelsb = ax2b.get_legend_handles_labels()
    ax2b.legend(handlesa+handlesb, labelsa+labelsb, ncol=2, loc='best')
    
    
    # Thrust and power
    ax3a = fig.add_subplot(3,1,3)
    ax3a.plot(t_eng, thr_lbf, color='0.65', label='$T$')
    
    ax3a.set_title("Thrust and power")    
    ax3a.set_xlabel('$t$ (s)')
    ax3a.set_ylabel('T (lbf)')
    
    ax3b = ax3a.twinx()    
    ax3b.plot(t_eng, pow_hp, color=(1,0.85,0.28), label='$\Pi$')
    
    ax3b.set_ylabel('$\Pi$ (hp)')
    
    handlesa, labelsa = ax3a.get_legend_handles_labels()
    handlesb, labelsb = ax3b.get_legend_handles_labels()
    ax3b.legend(handlesa+handlesb, labelsa+labelsb, ncol=2, loc='best')

    plt.tight_layout()
    
    # Export
    if dest_folder != None:
        plt.savefig(dest_folder+'plot_EngineStatus.pdf')

        
        
#
#=======================================================================================================================
#    


def plot_traj2D_NEA(r_NEA,t_pos,n_arrows,arrow_size,dest_folder=None):
    
    """
    Input units of measurement
    ---------------------------
    r_NEA      = 3x array of arryas
    r_NEA[0]   = 1x array, X_North, m  
    r_NEA[0]   = 1x array, Y_East, m
    r_NEA[0]   = 1x array, h_sl, m
    t_pos      = 1
    n_arrows   = int
    arrow_size = int
    """
    
    import plotting_utilities as plut

    fig = plt.figure(figsize=(12.3,10))

    # View from above
    ax1 = fig.add_subplot(2,1,1)
    traj2D = ax1.plot(r_NEA[1,:], r_NEA[0,:], ls='solid', color='#006633', label='')                      # trajectory
    ax1.plot(r_NEA[1,0], r_NEA[0,0],   ls='solid', color='#006633',                                       # start marker
             marker='o', markersize=4*arrow_size, markerfacecolor='#006633', markeredgecolor='#006633')   
    ax1.plot(r_NEA[1,-1], r_NEA[0,-1], ls='solid', color='#006633',                                       # end marker
             marker='o', markersize=4*arrow_size, markerfacecolor='w', markeredgecolor='#006633')         
    plut.add_arrow_to_line2D(ax1,traj2D,                                                                  # arrows
                             arrow_locs=np.linspace(1/(n_arrows+1),n_arrows/(n_arrows+1),n_arrows),
                             arrowsize=arrow_size) 

    ax1.set_title("Ground Track, to scale")    
    ax1.set_xlabel('East (m)')
    ax1.set_ylabel('North (m)')
    ax1.minorticks_on()

    plt.axis('equal')
    plt.axis([1.02*min(r_NEA[1,:]), 1.02*max(r_NEA[1,:]), 1.02*min(r_NEA[0,:]), 1.02*max(r_NEA[0,:])])
    plt.tight_layout()

    # Altitude
    ax2 = fig.add_subplot(2,1,2)
    hhist = ax2.plot(t_pos, r_NEA[2,:], ls='solid', color='#006633', label='')                          # altitude history
    ax2.plot(t_pos[0], r_NEA[2,0],   ls='solid', color='#006633',                                       # start marker
             marker='o', markersize=4*arrow_size, markerfacecolor='#006633', markeredgecolor='#006633')   
    ax2.plot(t_pos[-1], r_NEA[2,-1], ls='solid', color='#006633',                                       # end marker
             marker='o', markersize=4*arrow_size, markerfacecolor='w', markeredgecolor='#006633')         
    plut.add_arrow_to_line2D(ax2,hhist,                                                                 # arrows
                             arrow_locs=np.linspace(1/(n_arrows+1),n_arrows/(n_arrows+1),n_arrows),
                             arrowsize=arrow_size) 

    ax2.set_title("Altitude history")    
    ax2.set_xlabel(r'$t$ (s)')
    ax2.set_ylabel(r'$h_\mathrm{SL}$ (m)')
    ax2.minorticks_on()

    ax2.set_xlim([1.02*min(t_pos), 1.02*max(t_pos)])
    plt.tight_layout()
    
    # Export
    if dest_folder != None:
        plt.savefig(dest_folder+'plot_Traj2D_NEA.pdf')
    

def plot_traj3D_NEA(r_NEA,X_proj='N',Y_proj='E',view=(45,-45),to_scale='XYZ',mrk_size=80,dest_folder=None):
    
    """
    Input
    ---------------------------
    r_NEA      = 3x array of arryas
    r_NEA[0]   = 1x array, X_North, m  
    r_NEA[0]   = 1x array, Y_East, m
    r_NEA[0]   = 1x array, h_sl, m
    X_proj     = string,              'N' or 'S': indicates the direction where to project the trajectory
    Y_proj     = string,              'E' or 'W': indicates the direction where to project the trajectory
    view       = 2x1 tuple,           sets the view point in terms of Elevation and Azimuth
    equal      = bool,                set the axis scale to equal or not
    mrk_size   = int                  set marker size
    """
    
    from mpl_toolkits.mplot3d import Axes3D
    import plotting_utilities as plut
    
    fig = plt.figure(figsize=(12.3,10))
    ax = fig.add_subplot(1,1,1,projection='3d')
        
    # 3D trajectory
    ax.plot(   r_NEA[0],    r_NEA[1],    r_NEA[2],    color='#006633', ls='solid', linewidth=2)
    ax.scatter(r_NEA[0,0],  r_NEA[1,0],  r_NEA[2,0],  marker='o',      s=mrk_size, c='#006633', label='Start')
    ax.scatter(r_NEA[0,-1], r_NEA[1,-1], r_NEA[2,-1], marker=(5,0),    s=mrk_size, c='#006633', label='End')
    
    if to_scale=='XYZ': 
        plut.make_axis_equal_3d(r_NEA[0],r_NEA[1],r_NEA[2],ax,to_scale='XYZ')
        ax.set_title("Trajectory, to scale")
    elif to_scale=='XY': 
        plut.make_axis_equal_3d(r_NEA[0],r_NEA[1],r_NEA[2],ax,to_scale='XY')
        ax.set_title(r"Trajectory, altitude not to scale")
    else:
        ax.set_title("Trajectory, not to scale")
    
    XMIN, YMIN, ZMIN = ax.get_xlim().min(), ax.get_ylim().min(), ax.get_zlim().min()
    XMAX, YMAX, ZMAX = ax.get_xlim().max(), ax.get_ylim().max(), ax.get_zlim().max()
    
    ax.set_xlim3d([XMIN, XMAX])
    ax.set_ylim3d([YMIN, YMAX])
    ax.set_zlim3d([ZMIN, ZMAX])
    
    # Ground track
    ax.plot(   r_NEA[0],    r_NEA[1],    np.ones(len(r_NEA[2]))*ZMIN, color='k', ls='dashed',  linewidth=1) 
    ax.scatter(r_NEA[0,0],  r_NEA[1,0],  ZMIN,                        c='w',     marker='o',   s=0.8*mrk_size)
    ax.scatter(r_NEA[0,-1], r_NEA[1,-1], ZMIN,                        c='w',     marker=(5,0), s=0.8*mrk_size)
    
    # altitude on plane parallel to YZ, Northern or Southern wall of plot
    if X_proj == 'S': 
        ax.plot(np.ones(len(r_NEA[0]))*XMIN, r_NEA[1],     r_NEA[2],    color='0.65', ls='dashed',   linewidth=1)
        ax.scatter(XMIN,                     r_NEA[1,0] ,  r_NEA[2,0],  c='w',        marker='o',    s=0.8*mrk_size)
        ax.scatter(XMIN,                     r_NEA[1,-1] , r_NEA[2,-1], c='w',        marker=(5,0),  s=0.8*mrk_size)
    elif X_proj == 'N':
        ax.plot(np.ones(len(r_NEA[0]))*XMAX, r_NEA[1],     r_NEA[2],    color='0.65', ls='dashed',  linewidth=1)
        ax.scatter(XMAX,                     r_NEA[1,0] ,  r_NEA[2,0],  c='w',        marker='o',   s=0.8*mrk_size) 
        ax.scatter(XMAX,                     r_NEA[1,-1] , r_NEA[2,-1], c='w',        marker=(5,0), s=0.8*mrk_size)
        
    # altitude on plane parallel to XZ, Eastern or Western wall of plot
    if Y_proj == 'W': 
        ax.plot(   r_NEA[0],    np.ones(len(r_NEA[1]))*YMIN, r_NEA[2],    color='0.65', ls='dashed',  linewidth=1)
        ax.scatter(r_NEA[0,0],  YMIN,                        r_NEA[2,0],  c='w',        marker='o',   s=0.8*mrk_size)
        ax.scatter(r_NEA[0,-1], YMIN,                        r_NEA[2,-1], c='w',        marker=(5,0), s=0.8*mrk_size)
    elif Y_proj == 'E':
        ax.plot(   r_NEA[0],    np.ones(len(r_NEA[1]))*YMAX, r_NEA[2],    color='0.65', ls='dashed',  linewidth=1)
        ax.scatter(r_NEA[0,0],  YMAX,                        r_NEA[2,0],  c='w',        marker='o',   s=0.8*mrk_size)
        ax.scatter(r_NEA[0,-1], YMAX,                        r_NEA[2,-1], c='w',        marker=(5,0), s=0.8*mrk_size)
    
    # Labels and legend
    ax.set_xlabel('\n'+"North (m)", linespacing=3.5)
    ax.set_ylabel('\n'+"East (m)", linespacing=3.5)
    ax.set_zlabel('\n'+r'$h_\mathrm{SL}$', linespacing=3.5)
    
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, ncol=1, loc='best')
    
    # Axis visualization and scale
    ax.invert_xaxis()
    ax.view_init(view[0],view[1]) # Elevation, Azimuth
    
    plt.tight_layout()
    
    # Export
    if dest_folder != None:
        plt.savefig(dest_folder+'plot_traj3D_NEA.pdf')
        
        
def plot_Ground_Effect(data_aer, dest_folder=None):
    
    """
    Input units of measurement
    ---------------------------
    Time                      = s
    CLwbh                     = lb
    h_b_cg_ft                 = 1
    h_b_mac_ft                = 1
    ground_effect_factor_lift = 1
    """
    
    # Variables assignment
    t_aer   = data_aer[:,0]
    CLwbh = data_aer[:,21]
    h_b_cg_ft = data_aer[:,42]
    h_b_mac_ft = data_aer[:,43]
    ground_effect_factor_lift = data_aer[:,44]
    
    fig = plt.figure(figsize=(12.3,15))
    
    
    # Lift (total) in lb
    ax1a = fig.add_subplot(3,1,1)
    ax1a.plot(t_aer, CLwbh, ls='solid', color='b', label=r'$\bar{q}\, S\, C_{L}$')

    ax1a.set_title("Lift")
    ax1a.set_xlabel(r'$t$ (s)')
    ax1a.set_ylabel(r'L (lb)')
    ax1a.set_ylim(ymin=min(list(CLwbh)),
                  ymax=max(list(CLwbh)))
                 

    ax2a = fig.add_subplot(3,1,2)
    ax2a.plot(t_aer, ground_effect_factor_lift, ls='solid', color='b', label=r'$f_{ge,L}$')

    ax2a.set_title("Ground effect lift factor")
    ax2a.set_xlabel(r'$t$ (s)')
    ax2a.set_ylabel(r'$f_{ge,L}$')
    ax2a.set_ylim(ymin=min(list(ground_effect_factor_lift)),
                  ymax=1.2 #max(list(ground_effect_factor_lift))
                 )

    ax3a = fig.add_subplot(3,1,3)
    ax3a.plot(t_aer, h_b_mac_ft, ls='solid', color='r', label=r'$h_{\mathrm{mac}}/b$')
    ax3a.plot(t_aer, h_b_cg_ft, ls='solid', color='g', label=r'$h_{\mathrm{cg}}/b$')

    ax3a.set_title("Height above ground ratio")
    ax3a.set_xlabel(r'$t$ (s)')
    ax3a.set_ylabel(r'(-)')
    ax3a.set_ylim(ymin=0, #min(list(ground_effect_factor_lift)),
                  ymax=2.5 #max(list(ground_effect_factor_lift))
                 )
    
    handlesa, labelsa = ax3a.get_legend_handles_labels()
    ax3a.legend(handlesa, labelsa, ncol=2, loc='best')

    plt.tight_layout()
    
    
    # Export
    if dest_folder != None:
        plt.savefig(dest_folder+'plot_Ground_Effect.pdf')