def geoc_to_NEA(lat, lon, h_sl, lat0=None, lon0=None, flat=1):

    """
    Converts the time histories of geocentric latitude, longitude and altitude above Sea Level
    to the time histories of North, East and altitude. The latter are expressed in a reference 
    frame whose origin is in the initial position (L,l) of the simulation, but at Mean Sea Level altitude.
    Earth is considered flat.

    Arguments
    -----------
    lat  = 1d array, rad
    lon  = 1d array, rad
    h_sl = 1d array, m
    flat = bool (default is 1)

    Output
    -----------
    3x1 array of arrays = [X_north, Y_east, h_sl], m

    Notes
    -----------
    Suppose h_sl is constant due to A/C altitude hold.
    With flat-Earth model implemented, like it is done here by default, altitude will actually remain constant
    also in the NED reference frame. If Earth were considered round, altitude would be expected to remain constant 
    with respect to Earth surface: therefore, actual altitude in the NED reference frame (which is fixed to the initial
    position of the aircraft) would clearly decrease because of Earth's curvature.

    """
    
    from numpy import array, cos, sin, arcsin, arctan2

    # Earth radius (assumed to be equal to MSL)
    R_E = 6371e3 # m

    # Time history of the A/C position in ECEF system
    R = (R_E+h_sl)*array([cos(lat)*cos(lon),  # X ECEF
                          cos(lat)*sin(lon),  # Y ECEF
                          sin(lat)])          # Z ECEF
    
    if lat0 is None and lon0 is None:
        lat0 = lat[0]
        lon0 = lon[0]
    
    R0 = R_E * array([cos(lat0)*cos(lon0),  # X ECEF
                      cos(lat0)*sin(lon0),  # Y ECEF
                      sin(lat0)])           # Z ECEF
    
    if isinstance(lat, float):
        DR = array([R[i]-R0[i] for i in range(len(R0))])
    else:
        DR = array([R[i,:]-R0[i] for i in range(len(R0))])
        
    # Transformation matrix
    A = array([[-sin(lat0)*cos(lon0), -sin(lat0)*sin(lon0), +cos(lon0)],
               [-sin(lon0),              cos(lon0),             0     ],
               [-cos(lat0)*cos(lon0), -cos(lat0)*sin(lon0), -sin(lat0)]
              ])

    r = A.dot(DR)
    
    # Check Earth model to set correct altitude time history
    if    flat == 1: r[-1] = h_sl          # flat Earth
    else           : r[-1] = -r[-1]+h_sl   # non-flat Earth
    
    return r



def get_destination_from_start_distance_bearing(lat0, lon0, d, theta, flat=True):
    
    """
    Obtain latitude and longitude of a target location on Earth, if travelling
    along a great circle, for a certain distance, from the starting point with the
    given bearing. Earth is conseidered a perfect sphere.
    
    Arguments
    -----------
    lat0     = initial latitude,  1d array, deg
    lon0     = initial longitude, 1d array, deg
    d        = distance,          float,    m
    theta    = bearing,           1d array, deg

    Output
    -----------
    lat_f = final latitude,  1d array, deg
    lon_f = final longitude, 1d array, deg
    """
    
    from numpy import radians, degrees, cos, sin, arcsin, arctan2
    
    # Earth radius
    R = 6371e3
    
    lat0, lon0 = radians((lat0, lon0)) 
    theta      = radians(theta)
    
    if flat == True:
        lat_f = lat0 + (d/R)*cos(theta)
        lon_f = lon0 + (d/R)*sin(theta)/cos(lat0)
    elif flat == False:
        lat_f = arcsin(sin(lat0)*cos(d/R) + cos(lat0)*sin(d/R)*cos(theta))
        lon_f = lon0 + arctan2(sin(theta)*sin(d/R)*cos(lat0), cos(d/R) - sin(lat0)*sin(lat_f))

    lat_f, lon_f = degrees((lat_f, lon_f))

    return [lat_f, lon_f]
    