pmap = {

    't': {'property'     : 'Time',
          'axis_label'   : r'$t$ (s)',
          'figure_title' : 'Time'},

    's': {'property'     : 'NONE',
          'axis_label'   : r'$s$ (ft)',
          'figure_title' : 'Trajectory length'},

    'alpha_deg': {'property'     : '/fdm/jsbsim/aero/alpha-deg',
                  'axis_label'   : r'$\alpha$ (deg)',
                  'figure_title' : 'Angle of attack'},

    'alpha_rad': {'property'     : '/fdm/jsbsim/aero/alpha-rad',
                  'axis_label'   : r'$\alpha$ (rad)',
                  'figure_title' : 'Angle of attack'},

    'beta_deg':  {'property': '/fdm/jsbsim/aero/beta-deg',
                  'axis_label': r'$\beta$ (deg)',
                  'figure_title' :'Angle of sideslip'},

    'beta_rad':  {'property': '/fdm/jsbsim/aero/beta-rad',
                  'axis_label': r'$\beta$ (rad)',
                  'figure_title' :'Angle of sideslip'},

    'phi_rad':      {'property': '/fdm/jsbsim/attitude/phi-rad',
                     'axis_label': r'$\phi$ (rad)',
                     'figure_title' :'Third Euler Angle'},

    'phi_deg':      {'property': '/fdm/jsbsim/attitude/phi-deg',
                     'axis_label': r'$\phi$ (deg)',
                     'figure_title' :'Third Euler Angle'},

    'theta_rad':    {'property': '/fdm/jsbsim/attitude/theta-rad',
                     'axis_label': r'$\theta$ (rad)',
                     'figure_title' :'Second Euler Angle'},

    'theta_deg':    {'property': '/fdm/jsbsim/attitude/theta-deg',
                     'axis_label': r'$\theta$ (deg)',
                     'figure_title' : 'Second Euler Angle'},

    'psi_rad':      {'property': '/fdm/jsbsim/attitude/psi-rad',
                     'axis_label': r'$\psi$ (rad)',
                     'figure_title' : 'First Euler Angle'},

    'psi_deg':      {'property': '/fdm/jsbsim/attitude/psi-deg',
                     'axis_label': r'$\psi$ (deg)',
                     'figure_title' : 'First Euler Angle'},

    'gamma_rad':    {'property': ' /fdm/jsbsim/flight-path/gamma-rad',
                     'axis_label': r'$\gamma$ (deg)',
                     'figure_title' : 'Flight Path Angle'},

    'gamma_deg':    {'property': '/fdm/jsbsim/flight-path/gamma-deg',
                     'axis_label': r'$\gamma$ (deg)',
                     'figure_title' : 'Flight Path Angle'},


    'delta_a':       {'property': '/fdm/jsbsim/fcs/right-aileron-pos-deg',
                     'axis_label': r'$\delta_a$ (deg)',
                     'figure_title' : 'Aileron command'},

    'delta_e':          {'property': '/fdm/jsbsim/fcs/elevator-pos-deg',
                     'axis_label': r'$\delta_e$ (deg)',
                     'figure_title' : 'Elevator command'},

    'delta_r':          {'property': '/fdm/jsbsim/fcs/rudder-pos-deg',
                     'axis_label': r'$\delta_r$ (deg)',
                     'figure_title' : 'Rudder command'},

    'delta_t':          {'property': '/fdm/jsbsim/fcs/throttle-pos-norm',
                     'axis_label': r'$\delta_t$ (deg)',
                     'figure_title' : 'Throttle command'},

    'delta_e_eff_deg':  {'property': '/fdm/jsbsim/fcs/elevator-effective-pos-deg',
                     'axis_label': r'$\delta_{e,\mathrm{eff}}$ (deg)',
                     'figure_title' :'Effective elevator command'},

    'delta_tab_deg':    {'property': '/fdm/jsbsim/fcs/tab-pos-deg',
                     'axis_label': r'$\delta_\mathrm{tab}$ (deg)',
                     'figure_title' : 'Tab deflection'},


    'p_rad':        {'property': '/fdm/jsbsim/velocities/p-rad_sec',
                     'axis_label': r'$p$ (rad/s)',
                     'figure_title' : 'Roll angular velocity'},

    'p_deg':        {'property': '/fdm/jsbsim/velocities/p-deg_sec',
                     'axis_label': r'$p$ (deg/s)',
                     'figure_title' : 'Roll angular velocity'},

    'q_rad':        {'property': '/fdm/jsbsim/velocities/q-rad_sec',
                     'axis_label': r'$q$ (rad/s)',
                     'figure_title' : 'Pitch angular velocity'},

    'q_deg':        {'property': '/fdm/jsbsim/velocities/q-deg_sec',
                     'axis_label': r'$q$ (deg/s)',
                     'figure_title' : 'Pitch angular velocity'},

    'r_rad':        {'property': '/fdm/jsbsim/velocities/r-rad_sec',
                     'axis_label': r'$r$ (rad/s)',
                     'figure_title' : 'Yaw angular velocity'},

    'r_deg':        {'property': '/fdm/jsbsim/velocities/r-deg_sec',
                     'axis_label': r'$r$ (deg/s)',
                     'figure_title' : 'Yaw angular velocity'},

    'V_fts':        {'property': '/fdm/jsbsim/velocities/vtrue-fps',
                     'axis_label': r'$V_t$ (ft/s)',
                     'figure_title' : 'True Airspeed'},

    'V_kts':        {'property': '/fdm/jsbsim/velocities/vtrue-kts',
                     'axis_label': r'$V_t$ (kts)',
                     'figure_title' : 'True Airspeed'},

    'Vg_fts':        {'property': '/fdm/jsbsim/velocities/vg-fps',
                     'axis_label': r'$V_g$ (ft/s)',
                     'figure_title' : 'Ground Speed (N-E components)'},

    'Vg_kts':        {'property': '/fdm/jsbsim/velocities/vg-kts',
                     'axis_label': r'$V_g$ (kts)',
                     'figure_title' : 'Ground speed (N-E components)'},

    'h_sl_ft':      {'property': '/fdm/jsbsim/position/h-sl-ft',
                     'axis_label': r'$h_{SL}$ (ft)',
                     'figure_title' : 'Altitude above Sea Level'},

    'h_sl_m':       {'property': '/fdm/jsbsim/position/h-sl-meters',
                     'axis_label': r'$h_{SL}$ (m)',
                     'figure_title' : 'Altitude above Sea Level'},

    'h_agl_ft':      {'property': '/fdm/jsbsim/position/h-agl-ft',
                     'axis_label': r'$h_{AGL}$ (ft)',
                     'figure_title' : 'Altitude above Ground Level'},

    'h_agl_m':      {'property': '/fdm/jsbsim/position/h-agl-m',
                     'axis_label': r'$h_{AGL}$ (m)',
                     'figure_title' : 'Altitude above Ground Level'},

    'lat_gc_deg':   {'property': '/fdm/jsbsim/position/lat-gc-deg',
                     'axis_label': r'$\lambda$ (deg)',
                     'figure_title' : 'Geocentric latitude'},

    'lat_gc_rad':   {'property': '/fdm/jsbsim/position/lat-gc-rad',
                     'axis_label': r'$\lambda$ (rad)',
                     'figure_title' : 'Geocentric latitude'},

    'lon_gc_deg':   {'property': '/fdm/jsbsim/position/long-gc-deg',
                     'axis_label': r'$L$ (deg)',
                     'figure_title' : 'Geocentric longitude'},

    'lon_gc_rad':   {'property': '/fdm/jsbsim/position/long-gc-rad',
                     'axis_label': r'$L$ (rad)',
                     'figure_title' : 'Geocentric longitude'},

    'lat_WPf':       {'property': '/fdm/jsbsim/guidance/target-field-wp-latitude-rad',
                     'axis_label': r'$\lambda_{WP_f}$ (rad)',
                     'figure_title' : 'Field Waypoint latitude'},

    'lon_WPf':       {'property': '/fdm/jsbsim/guidance/target-field-wp-longitude-rad',
                     'axis_label': r'$L_{WP_f}$ (rad)',
                     'figure_title' : 'Field Waypoint longitude'},

    'lat_WP1':       {'property': '/fdm/jsbsim/guidance/target-wp-latitude-rad-ONE',
                     'axis_label': r'$\lambda_{WP_1}$ (rad)',
                     'figure_title' : 'First Waypoint latitude'},

    'lon_WP1':       {'property': '/fdm/jsbsim/guidance/target-wp-longitude-rad-ONE',
                     'axis_label': r'$L_{WP_1}$ (rad)',
                     'figure_title' : 'First Waypoint longitude'},

    'Xned_rel_m':       {'property': '/fdm/jsbsim/position/ned-x-relto-field-wp-m',
                     'axis_label': r'$X_{N}$ (m)',
                     'figure_title' : 'North coordinate'},

    'Xned_rel_ft':      {'property': '/fdm/jsbsim/position/ned-x-relto-field-wp-ft',
                     'axis_label': r'$X_{N}$ (ft)',
                     'figure_title' : 'North coordinate'},

    'Yned_rel_m':       {'property': '/fdm/jsbsim/position/ned-y-relto-field-wp-m',
                     'axis_label': r'$Y_{E}$ (m)',
                     'figure_title' : 'East coordinate'},

    'Yned_rel_ft':      {'property': '/fdm/jsbsim/position/ned-y-relto-field-wp-ft',
                     'axis_label': r'$Y_{E}$ (ft)',
                     'figure_title' : 'East coordinate'},

    'Zned_rel_m':       {'property': '/fdm/jsbsim/position/ned-z-relto-field-wp-m',
                     'axis_label': r'$Z_{D}$ (m)',
                     'figure_title' : 'Altitude'},

    'Zned_rel_ft':      {'property': '/fdm/jsbsim/position/ned-z-relto-field-wp-ft',
                     'axis_label': r'$Z_{D}$ (ft)',
                     'figure_title' : 'Altitude'},

    'Hned_rel_m':       {'property': '/fdm/jsbsim/position/ned-h-relto-field-wp-m',
                     'axis_label': r'$Z_{D}$ (ft)',
                     'figure_title' : 'Altitude'},

    'Hned_rel_ft':      {'property': '/fdm/jsbsim/position/ned-h-relto-field-wp-ft',
                     'axis_label': r'$Z_{D}$ (ft)',
                     'figure_title' : 'Altitude'},

    'active_wp':    {'property': '/fdm/jsbsim/ap/active-waypoint',
                     'axis_label': r'Active Waypoint ID',
                     'figure_title' : 'Active Waypoint ID'},

    # Body reference frame accelerations (dimensional and normalized) at pilot position
    'a_x_pilot_fts':    {'property': '/fdm/jsbsim/accelerations/a-pilot-x-ft_sec2',
                        'axis_label': r'$\{a_{x}\}_B$ (ft/s$^2$) at pilot pos.',
                        'figure_title' : 'Acceleration at pilot position, in Body ref. frame'},

    'a_y_pilot_fts':    {'property': '/fdm/jsbsim/accelerations/a-pilot-y-ft_sec2',
                        'axis_label': r'$\{a_{y}\}_B$ (ft/s$^2$) at pilot pos.',
                        'figure_title' : 'Acceleration at pilot position, in Body ref. frame'},

    'a_z_pilot_fts':    {'property': '/fdm/jsbsim/accelerations/a-pilot-z-ft_sec2',
                        'axis_label': r'$\{a_{z}\}_B$ (ft/s$^2$) at pilot pos.',
                        'figure_title' : 'Acceleration at pilot position, in Body ref. frame'},

    'n_x_pilot':    {'property': '/fdm/jsbsim/accelerations/n-pilot-x-norm',
                    'axis_label': r'$\{n_{x}\}_B$ at pilot pos.',
                    'figure_title' : 'Adimensional acceleration at pilot position, in Body ref. frame'},

    'n_y_pilot':    {'property': '/fdm/jsbsim/accelerations/n-pilot-y-norm',
                    'axis_label': r'$\{n_{y}\}_B$ at pilot pos.',
                    'figure_title' : 'Adimensional acceleration at pilot position, in Body ref. frame'},

    'n_z_pilot':    {'property': '/fdm/jsbsim/accelerations/n-pilot-z-norm',
                    'axis_label': r'$\{n_{z}\}_B$ at pilot pos.',
                    'figure_title' : 'Adimensional acceleration at pilot position, in Body ref. frame'},

    'n_x':    {'property': '/fdm/jsbsim/accelerations/Nx',
                'axis_label': r'$n_{x_\mathrm{B}}$ at CG',
                'figure_title' : 'Load factor at CG, in Body ref. frame'},

    'n_y':    {'property': '/fdm/jsbsim/accelerations/Ny',
                'axis_label': r'$n_{y_\mathrm{B}}$ at CG.',
                'figure_title' : 'Load factor at CG, in Body ref. frame'},

    'n_z':    {'property': '/fdm/jsbsim/accelerations/Nz',
                'axis_label': r'$n_{z_\mathrm{B}}$ at CG',
                'figure_title' : 'Load factor at CG, in Body ref. frame'},

    # Winds
    'Vw_N_fps':    {'property': '/fdm/jsbsim/atmosphere/wind-north-fps',
                    'axis_label': r'$V_{\mathrm{W}_N}$ (ft/s) at CG',
                    'figure_title' : 'Wind speed at CG, north component'},

    'Vw_E_fps':    {'property': '/fdm/jsbsim/atmosphere/wind-east-fps',
                    'axis_label': r'$V_{\mathrm{W}_E}$ (ft/s) at CG',
                    'figure_title' : 'Wind speed at CG, east component'},

    'Vw_D_fps':    {'property': '/fdm/jsbsim/atmosphere/wind-down-fps',
                    'axis_label': r'$V_{\mathrm{W}_D}$ (ft/s) at CG',
                    'figure_title' : 'Wind speed at CG, down component'},

    'Vw_N_kts':    {'property': '/fdm/jsbsim/atmosphere/wind-north-kts',
                    'axis_label': r'$V_{\mathrm{W}_N}$ (kts) at CG',
                    'figure_title' : 'Wind speed at CG, north component'},

    'Vw_E_kts':    {'property': '/fdm/jsbsim/atmosphere/wind-east-kts',
                    'axis_label': r'$V_{\mathrm{W}_E}$ (kts) at CG',
                    'figure_title' : 'Wind speed at CG, east component'},

    'Vw_D_kts':    {'property': '/fdm/jsbsim/atmosphere/wind-down-kts',
                    'axis_label': r'$V_{\mathrm{W}_D}$ (kts) at CG',
                    'figure_title' : 'Wind speed at CG, down component'},

    'Vw_x_fps':    {'property': '/fdm/jsbsim/atmosphere/wind-x-fps',
                    'axis_label': r'$V_{\mathrm{W}_x}$ (ft/s) at CG',
                    'figure_title' : 'Wind speed at CG, in BODY ref. frame'},

    'Vw_y_fps':    {'property': '/fdm/jsbsim/atmosphere/wind-y-fps',
                    'axis_label': r'$V_{\mathrm{W}_y}$ (ft/s) at CG',
                    'figure_title' : 'Wind speed at CG, in BODY ref. frame'},

    'Vw_z_fps':    {'property': '/fdm/jsbsim/atmosphere/wind-z-fps',
                    'axis_label': r'$V_{\mathrm{W}_z}$ (ft/s) at CG',
                    'figure_title' : 'Wind speed at CG, in BODY ref. frame'},

    'Vw_x_kts':    {'property': '/fdm/jsbsim/atmosphere/wind-x-kts',
                    'axis_label': r'$V_{\mathrm{W}_x}$ (kts) at CG',
                    'figure_title' : 'Wind speed at CG, in BODY ref. frame'},

    'Vw_y_kts':    {'property': '/fdm/jsbsim/atmosphere/wind-y-kts',
                    'axis_label': r'$V_{\mathrm{W}_y}$ (kts) at CG',
                    'figure_title' : 'Wind speed at CG, in BODY ref. frame'},

    'Vw_z_kts':    {'property': '/fdm/jsbsim/atmosphere/wind-z-kts',
                    'axis_label': r'$V_{\mathrm{W}_z}$ (kts) at CG',
                    'figure_title' : 'Wind speed at CG, in BODY ref. frame'},


    # Engine stats
    'adv_ratio':    {'property': '/fdm/jsbsim/propulsion/engine/advance-ratio',
                     'axis_label': r'$\gamma_{p}$ (-)',
                     'figure_title' : 'Propeller advance ratio'},

    'thr_coeff':    {'property': '/fdm/jsbsim/propulsion/engine/thrust-coefficient',
                     'axis_label': r'$C_{T}$ (-)',
                     'figure_title' : 'Thrust coefficient'},

    'prop_rpm':     {'property': '/fdm/jsbsim/propulsion/engine/propeller-rpm',
                     'axis_label': r'$N$ (rpm)',
                     'figure_title' : 'Propeller rounds per minute'},

    'thr_lbf':      {'property': '/fdm/jsbsim/propulsion/engine/thrust-lbs',
                     'axis_label': r'$T$ (lbf)',
                     'figure_title' : 'Thrust'},

    'pow_hp':       {'property': '/fdm/jsbsim/propulsion/engine/power-hp',
                     'axis_label': r'$\Pi$ (hp)',
                     'figure_title' : 'Power'},

}
