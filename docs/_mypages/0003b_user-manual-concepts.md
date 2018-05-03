---
layout: default
title: User manual - Concepts
categories: [menu, content, user-manual, concepts]
permalink: /mypages/concepts/
---

# Concepts

## Simulation

While the JSBSim user does not need to know some of the finer details of the flight simulator operation, it can be helpful to understand basically how JSBSim works. Some of the most important concepts are described in this section.

- Frames of reference are used to describe the placement and location of various items in a vehicle model.

- There is flexibility in how the units of measure can be specified when defining a vehicle model – both English and metric units are supported.

- The use of “Properties” permits JSBSim to be a generic simulator, providing a way to interface the various systems with parameters (or variables). Properties are used throughout the configuration files that describe aircraft and engine characteristics.

- Obviously, math plays a big part in modeling flight physics. JSBSim makes use of data tables, as flight dynamics characteristics are often stored in tables. Arbitrary algebraic functions can also be set up in JSBSim, allowing broad freedom for describing aerodynamic and flight control characteristics.

- Users have to have, at least a basic knowledge, of conventional forces and moments acting on an airplane in flight.

- The understanding of flight controls and of how system modelling can be achieved in JSBSim are the keys for successful and effective simulations.

## Frames of Reference

Before moving into a description of the configuration file syntax, one must understand some basic information about some of the frames of reference used (*i*) in describing the location of objects on the aircraft, (*ii*) in specifying conditions related to the position and orientation of the aircraft in space, or (*iii*) when assigning inputs for a given flight condition.

### Structural, or "Construction" Frame

This frame is a common manufacturer's frame of reference and is used to define points on the aircraft such as the center of gravity, the locations of all the wheels, the pilot eye-point, point masses, thrusters, and so on. Items in the JSBSim aircraft configuration file are located using this frame.

In the structural frame the X-axis runs along the fuselage length and points towards the tail, the Y-axis points from the fuselage out towards the right wing, and of course the Z-axis then is positive upwards. Typically, the origin $O_\mathrm{C}$ for this frame is near the front of the aircraft (at the tip of the nose, at the firewall for a single engine airplane, or at some distance in front of the nose). This frame is often named $$\mathcal{F}_\mathrm{C} = \{O_\mathrm{C}, x_\mathrm{C}, y_\mathrm{C}, z_\mathrm{C}\}$$.

{% include image.html
  url="/assets/img/ac_construction_axes.svg"
  width="90%"
  description="Aircraft structural (or construction) frame of reference with origin $O_\mathrm{C}$. Besides the structural frame axes $x_\mathrm{C}$, $y_\mathrm{C}$, and $z_\mathrm{C}$, the standard body frame axes $x_\mathrm{B}$, $y_\mathrm{B}$, and $z_\mathrm{B}$ are also shown with their origin at the center of mass $G$. The pilot's eye-point is located at $P_\mathrm{EP}$."
  %}

The X-axis is typically coincident with the fuselage centerline and often is coincident with the thrust axis (for instance, in single engine propeller aircraft it passes through the propeller hub). Positions along the $x_\mathrm{C}$ axis are referred to as stations. Positions along the $z_\mathrm{C}$ axis are referred to as waterline positions. Positions along the $y_\mathrm{C}$ axis are referred to as buttline positions.

{% include image.html
  url="/assets/img/c172x_blender.png"
  width="70%"
  description="A screenshot taken from the 3D modeling software Blender. The scene shows a model of Cessna 172 with its structural frame $\mathcal{F}_\mathrm{C} = \{O_\mathrm{C}, x_\mathrm{C}, y_\mathrm{C}, z_\mathrm{C}\}$. The origin $O_\mathrm{C}$ in this case is located inside the cockpit, near the dashboard."
  %}

Note that the origin can be anywhere for a JSBSim-modeled aircraft, because JSBSim internally only uses the *relative distances* between the CG and the various objects --- not the absolute locations themselves.

{% include image.html
  url="/assets/img/ac_center_of_gravity.svg"
  width="90%"
  description="Center of gravity (CG) position, point $G$, determined in a construction frame."
  %}

{% include image.html
  url="/assets/img/c172_ground_reaction.svg"
  width="90%"
  description="Definition of ground contact points in terms of construction frame locations."
  %}

{% include image.html
  url="/assets/img/c172_sideview.svg"
  width="70%"
  description="Two key point locations $P_\mathrm{ARP}$ and $P_\mathrm{CG,EW}$ in the structural frame, respectively, he pole of aerodynamic moments and the Empty Weight CG of the airframe. The shape of the wing root profile and its chord are also sketched."
  %}

{% include image.html
  url="/assets/img/c172_perspective_view_left.svg"
  width="70%"
  description="Besides point $P_\mathrm{CG,EW}$, are represented two more significant locations, $P_\mathrm{Pilot}$ and $P_\mathrm{Right\,Pass}$, where two additional masses are concentrated, respectively, of the pilot and of the right passenger."
  %}

### Body Frame

In JSBSim, the body frame is similar to the structural frame, but rotated 180 degrees about the $y_\mathrm{C}$, with the origin coincident with the CG. Typycally, the body frame is defined by knowning the position of the airplane's center of mass $G$ and the direction of the longitudinal construction axis $x_\mathrm{C}$. The axis $x_\mathrm{B}$ shall be chosen such that it originates from $G$, it is parallel to $x_\mathrm{C}$, and with a positive verse from $G$ towards the fuselage nose.

The frame of body axes is often called $$\mathcal{F}_\mathrm{B} = \{G, x_\mathrm{B}, y_\mathrm{B}, z_\mathrm{B}\}$$. The $x_\mathrm{B}$ axis is called the *roll axis* and points forward, the $y_\mathrm{B}$ axis is called *pitch axis* and points toward the right wing, the $z_\mathrm{B}$ axis is called *yaw axis* and points towards the fuselage belly.

{% include image.html
  url="/assets/img/ac_body_axes.svg"
  width="90%"
  description="Standard aircraft body axis frame, with origin at the center of gravity $G$."
  %}

In the body frame the aircraft forces and moments are summed and the resulting accelerations are integrated to get velocities.

### Stability, or "Aerodynamic" Frame

This frame is defined according to the instantaneous orientation of the relative wind vector with respect to the airframe. If, for simplicity, the air is still with respect to the Earth (no wind), and $\boldsymbol{V}$ is the aircraft center-of-mass velocity vector with respect to the Earth-fixed observer (also named $\boldsymbol{V}_\mathrm{CM/E}$ to emphasize the relative motion), then $-\boldsymbol{V}$ is the relative wind velocity and $V = \|\boldsymbol{V}\|$ is the airspeed.

The frame, named $$\mathcal{F}_\mathrm{A} = \{ G, x_\mathrm{A}, y_\mathrm{A}, z_\mathrm{A} \}$$, has the axis $x_\mathrm{A}$ that points into the relative wind vector projected onto the aircraft plane of symmetry $x_\mathrm{B} z_\mathrm{B}$. The axis $y_\mathrm{A}$ still points out the right wing and coincides with the body axis $y_\mathrm{B}$, and the axis $z_\mathrm{A}$ completes the right-hand system.

{% include image.html
  url="/assets/img/ac_aero_axes.svg"
  width="90%"
  description="Aerodynamic frame, defining the aerodynamic angles $\alpha_\mathrm{B}$ and $\beta$."
  %}

The two axes $x_\mathrm{A}$ and $z_\mathrm{A}$ belong, by definition, to the aircraft symmetry plane, but *they can rotate during flight* because the orientation of the relative wind velocity vector $\boldsymbol{V}$ might change with respect to the vehicle. The above figure shows how the aerodynamic frame is constructed. The angle between the two axes $x_\mathrm{A}$ and $x_\mathrm{B}$ is the aircraft angle of attack $\alpha_\mathrm{B}$. The angle formed by the instantaneous direction of $\boldsymbol{V}$ and its projection on the plane $x_\mathrm{B} z_\mathrm{B}$ is the sideslip angle $\beta$.

This frame, called stability frame in some manuals, is also named here 'aerodynamic frame' because the projection $Z_\mathrm{A}$ of the instantaneous aerodynamic resultant force $$\mathcal{F}_\mathrm{A}$$ onto the axis $z_\mathrm{A}$ defines the aerodynamic lift. In particular, the lift $L$ is such that $-L$ is the component of $$\mathcal{F}_\mathrm{A}$$ along $z_\mathrm{A}$, i.e. $Z_\mathrm{A}=-L$.

To visualize the above observation, consider a typical maneuver studied in flight mechanics: the zero-sideslip (or 'coordinated'), constant altitude turn at steady airspeed. In this situation the wings are banked and so is the lift. In such a turn $$\mathcal{F}_\mathrm{A}$$ is banked and $x_\mathrm{A}$ is kept horizontal. In general terms, the lift as a vector is always defined in the aircraft symmetry plane.

{% include image.html
  url="/assets/img/three_d_forces_level_turn.svg"
  width="90%"
  description="Banked lift in a steady coordinated turn at constant altitude. The bank angle $\phi_\mathrm{W}$ is a rotation around the relative wind velocity vector. The motion is freezed in time when the velocity vector is aligned with the North. Coordinated turn means that $\beta=0$ and constant altitude means that $x_\mathrm{A}$ is kept horizontal."
  %}

*Remark* --- In dynamic stability studies what is referred to as 'stability frame' is something slightly different from the aerodynamic frame introduced above: The stability frame in aircraft flight dynamics and stability conventions is nothing but a particular kind of body-fixed frame, defined with respect to an initial symmetrical, steady, wings-level, constant altitude flight condition. This conditions gives the direction of $x_\mathrm{S}$ (which coincides with $x_\mathrm{A}$ at that particular flight attitude). Therefore, in dynamic stability studies the stability frame, unlike the aerodynamic frame, is fixed with the vehicle.

In JSBSim the notion of stability frame $$\mathcal{F}_\mathrm{S} = \{ G, x_\mathrm{S}, y_\mathrm{S}, z_\mathrm{S} \}$$ is used to mean the aerodynamic frame.

### Earth-Centered Inertial Frame (ECI) and Earth-Centered Earth-Fixed Frame (ECEF)

The Earth-Centered Inertial frame (or simply 'inertial frame') $$\mathcal{F}_\mathrm{ECI} = \{ O_\mathrm{ECI}, x_\mathrm{ECI}, y_\mathrm{ECI}, z_\mathrm{ECI} \}$$ is fixed with its origin at the center of the Earth. Its cartesian axes remain fixed relative to the stars, and provide a reference frame for which the aircraft (or spacecraft) equations of motion are most simply expressed. The positive $z_\mathrm{ECI}$ axis passes through the Earth's geographic North Pole. The $x_\mathrm{ECI}$ and $y_\mathrm{ECI}$ axes lie in the equatorial plane. The axis $x_\mathrm{ECI}$ is always parallel to a line from the Sun's center of mass to Earth's position in orbit at the vernal equinox. The ECI system is shown in the next figure.

{% include image.html
  url="/assets/img/inertial_frame.svg"
  width="60%"
  description="Earth-Centered Inertial (ECI) frame and Earth-Centered Earth-Fixed (ECEF) frame."
  %}

The axes of the Earth-Centered, Earth-Fixed (ECEF) frame of reference, labeled $x_\mathrm{ECEF}$, $y_\mathrm{ECEF}$, and $z_\mathrm{ECEF}$, are also depicted in the above figure. The ECEF coordinate axes remain fixed with respect to the Earth. The origin $O_\mathrm{ECEF}$ of this cartesian system, like the inertial frame, is located at the mass center of the earth. The $z_\mathrm{ECEF}$ axis also lies along the Earth's spin axis and coincides with $z_\mathrm{ECI}$. The $x_\mathrm{ECEF}$ and $y_\mathrm{ECEF}$ axes both lie in the equatorial plane, with the positive $x_\mathrm{ECEF}$ axis passing through the prime meridian (Greenwich Meridian). The ECEF frame rotates counter-clockwise about the Inertial frames $z_\mathrm{ECI}$ axis with angular velocity $\omega_\mathrm{E}$. The Earth angular rate $\omega_\mathrm{E}$ is approximately equal to $2\pi/24$ radians/hour.

### North-Oriented Tangent Frames

**TBD**

{% include image.html
  url="/assets/img/earth_frames.svg"
  width="60%"
  description="Earth-Centered Earth-Fixed (ECEF) frame, geografic coordinates, Tangent (T) frame, and local Vertical (V) frame."
  %}

### Local-Vertical Local-Level Frame, or Local NED Frame

The local vertical frame $$\mathcal{F}_\mathrm{V} = \{ G, x_\mathrm{V}, y_\mathrm{V}, z_\mathrm{V}\}$$ is unrelated to the airplane's orientation in space but is only defined by its CG position with respect to some convenient Earth-fixed observer. If $G_\mathrm{GT}$ is the CG projected on the ground ('ground tracked'), the coordinate plane $x_\mathrm{V} y_\mathrm{V}$ is parallel to a plane locally tangent in $G_\mathrm{GT}$ to the Earth surface (a sphere or an ellipse). The axis $x_\mathrm{V}$ points towards the geographic North, The axis $y_\mathrm{V}$ points towards the East. Finally, the axis $z_\mathrm{V}$ points downwards towards the center of the Earth. For this reason the frame $$\mathcal{F}_\mathrm{V}$$ is also called *local NED* frame (North-East-Down).

{% include image.html
  url="/assets/img/ac_local_vertical_axes.svg"
  width="90%"
  description="Aircraft body frame and local vertical frame (NED frame). The aircraft Euler angles are also shown: the heading angle $\psi$ (negative in the picture), the elevation angle $\theta$, and the roll angle $\phi$."
  %}

The NED convention ensures that the aircraft weight is a force with components $(0,0,mg)$ in the frame $$\mathcal{F}_\mathrm{V}$$, where $m$ is the airplane's mass and $g$ is the gravitational acceleration.

The above figure shows an aircraft with the two frames $$\mathcal{F}_\mathrm{V}$$ and $$\mathcal{F}_\mathrm{B}$$. The Euler angles that define the body frame orientation with respect to the local NED frame are the *aircraft Euler angles*. For atmospheric flight vehicles the sequence of rotations used to define the Euler angles is '3-2-1'. This defines the *heading* angle $\psi$, the *elevation* angle $\theta$, and the *roll* angle $\phi$ with respect to an observer fixed with the Earth.

{% include image.html
  url="/assets/img/ac_euler_gimbal.svg"
  width="60%"
  description="Euler angle sequence for an aircraft. The frame $\mathcal{F}_\mathrm{E} = \{ O_\mathrm{E}, x_\mathrm{E}, y_\mathrm{E}, z_\mathrm{E}\}$ is an Earth-fixed NED coordinate system, with origin the $O_\mathrm{E}$ somewhere on the ground (or at see level) and the plane $x_\mathrm{E} y_\mathrm{E}$ tangent to the Earth surface. If the ground track point $G_\mathrm{GT}$ is not too far from $O_\mathrm{E}$, the Earth frame $\mathcal{F}_\mathrm{E}$ axes are parallel to those of the local NED frame $\mathcal{F}_\mathrm{V} = \{ G, x_\mathrm{V}, y_\mathrm{V}, z_\mathrm{V}\}$."
  %}

### Wind Frame

Besides the lift, the instantaneous aerodynamic resultant force vector $$\mathcal{F}_\mathrm{A}$$ has two more components in a frame of reference of which $z_\mathrm{A}$ is the third axis. This frame is called *wind frame* $$\mathcal{F}_\mathrm{W} = \{ G, x_\mathrm{W}, y_\mathrm{W}, z_\mathrm{W}\}$$.

The wind frame is defined by taking the $x_\mathrm{W}$ axis along the relative wind with a positive verse in the direction of motion. This means that $x_\mathrm{W}$ is superimposed to the vector $$\boldsymbol{V}$$. The third axis of $$\mathcal{F}_\mathrm{W}$$ is taken along the lift line of action, i.e. $z_\mathrm{W} \equiv z_\mathrm{A}$. Finally, the second axis $y_\mathrm{W}$ is chosen in order to complete the right-handed triad. The wind frame has its third axis constantly in the airframe plane of symmetry (also called the 'reference plane'). All the three wind axes rotate with respect to the body axes because of the changing attitude of the aircraft with respect to the relative wind $$-\boldsymbol{V}$$.

The component $X_\mathrm{W}$ of the force vector $$\mathcal{F}_\mathrm{A}$$ along the direction of $$\boldsymbol{V}$$ defines the aerodynamic drag: The drag $D$ is such that $X_\mathrm{W}=-D$. In presence of a nonzero sideslip angle $\beta$, a third nonzero component of $$\mathcal{F}_\mathrm{A}$$ arises along the lateral axis $y_\mathrm{W}$, i.e. the side force component $Y_\mathrm{W}$.

When the sideslip angle $\beta$ is zero, the wind frame and the aerodynamic frame are coincident. Only in this circumstance $y_\mathrm{W}$, being coincident with $y_\mathrm{A}$ and $y_\mathrm{B}$, is normal to the reference plane $x_\mathrm{B} z_\mathrm{B}$.

The figure below shows the standard frames of reference for an aircraft in climbing flight in calm air. The wind frame $$\mathcal{F}_\mathrm{W}$$ can be made superimposed to the aerodynamic frame $$\mathcal{F}_\mathrm{A}$$ when rotated around $z_\mathrm{W}$ of the angle $-\beta$.

{% include image.html
  url="/assets/img/three_d_definitions.svg"
  width="90%"
  description="Standard frames of reference and aircraft in climbing flight in calm air. The CG velocity vector $\boldsymbol{V}$ forms the flight path angle $\gamma$ with the horizontal plane. The standard three aerodynamic resultant force components $D$, $L$ and $Y_\mathrm{A}$ are also shown."
  %}

Consequently, the wind frame $$\mathcal{F}_\mathrm{W}$$ can be superimposed to the body frame $$\mathcal{F}_\mathrm{B}$$ when rotated first around $z_\mathrm{W}$ of the angle $-\beta$ then around the axis $y_\mathrm{A}$ of the angle $\alpha_\mathrm{B}$:

$$
\mathcal{F}_\mathrm{W} \stackrel{-\beta \, \curvearrowright \, z_\mathrm{W}}{ \longrightarrow } \mathcal{F}_\mathrm{A} \stackrel{\alpha_\mathrm{B} \, \curvearrowright \, y_\mathrm{A}}{ \longrightarrow } \mathcal{F}_\mathrm{B}
\label{eq:FW:To:FB}
$$

The components of the aerodynamic resultant force in body axes are then expressed as follows:

$$
\left\{\begin{matrix}
  X_\mathrm{B} \\ Y_\mathrm{B} \\ Z_\mathrm{B}
\end{matrix}\right\} =
\left[\begin{matrix}
  \cos\alpha_\mathrm{B} & 0 & -\sin\alpha_\mathrm{B} \\
  0 & 1 & 0 \\
  \sin\alpha_\mathrm{B} & 0 & \cos\alpha_\mathrm{B}
\end{matrix}\right]
  \left[\begin{matrix}
    \cos\beta & \sin(-\beta) & 0 \\
    -\sin(-\beta) & \cos\beta & 0 \\
    0 & 0 & 1
  \end{matrix}\right]
  \left\{\begin{matrix}
    -D \\ Y_\mathrm{W} \\ -L
  \end{matrix}\right\}
\label{eq:DYL:To:XYZB}  
$$

in terms of drag, side force and lift.

## Units

JSBSim uses English units for internal calculations almost exclusively. However, it is possible to input some parameters in the configuration file using different units. In fact, to avoid confusion, it is recommended that the unit always be specified. Units are specified using the `unit` attribute. For instance, the specification for the wingspan looks like this:

```xml
<wingspan unit="FT"> 35.8 </wingspan>
```

The above statement specifies a wingspan of 35.8 feet. The following statement specifying the wingspan in meters would result in the wingspan being converted to 35.8 feet as it was read in:

```xml
<wingspan unit="M"> 10.91 </wingspan>
```

The two statements for wingspan are effectively equivalent.

The following units are currently supported in JSBSim:

**Length**

| `unit=`  | unit   |
| ---:     | :---   |
| `FT`     | ft     |
| `IN`     | in     |
| `M`      | m      |
| `KM`     | km     |

**Area**

| `unit=`  | unit   |
| ---:     | :---   |
| `M2`     | m²     |
| `FT2`    | ft²    |

**Volume**

| `unit=`  | unit   |
| ---:     | :---   |
| `FT3`    | ft³    |
| `CC`     | cm³    |
| `M3`     | m³     |
| `LTR`    | l      |

**Mass and Weight**

| `unit=`  | unit   |
| ---:     | :---   |
| `LBS`    | lbm    |
| `KG`     | kg     |

**Moments of Inertia**

| `unit=`    | unit   |
| ---:       | :---   |
| `SLUG*FT2` | slug ft² |
| `KG*M2`    | kg m²  |

**Angles**

| `unit=`    | unit   |
| ---:       | :---   |
| `RAD`      | rad    |
| `DEG`      | deg    |

**Spring Force**

| `unit=`    | unit   |
| ---:       | :---   |
| `N/M`      | N/m    |
| `LBS/FT`   | lb/ft  |

**Damping Force**

| `unit=`    | unit   |
| ---:       | :---   |
| `N/M/SEC`  | N/(m s) |
| `LBS/FT/SEC` | lb/(ft s) |

**Power**

| `unit=`    | unit   |
| ---:       | :---   |
| `WATTS`    | W      |
| `HP`       | Hp     |

**Force**

| `unit=`    | unit   |
| ---:       | :---   |
| `LBS`      | lb     |
| `N `       | N      |

**Velocity**

| `unit=`    | unit   |
| ---:       | :---   |
| `KTS`      | kts    |
| `FT/SEC`   | ft/s   |
| `M/S`      | m/s    |

**Torque**

| `unit=`    | unit   |
| ---:       | :---   |
| `N*M`      | N m    |
| `FT*LBS`   | lb ft  |

**Pressure**

| `unit=`    | unit   |
| ---:       | :---   |
| `PSF`      | lb/ft² |
| `PSI`      | lb/in² |
| `ATM`      | atm    |
| `PA`       | N/m²   |
| `INHG`     | in HG  |

## Properties

Simulation programs need to manage a large amount of state information. With especially large programs, the data management task can cause problems:

- Contributors find it harder and harder to master the number of interfaces necessary to make any useful additions to the program, so contributions slow down.
- Runtime configurability becomes increasingly difficult, with different modules using different mechanisms (environment variables, custom specification files, command-line options, etc.).
- The order of initialization of modules is complicated and brittle, since one module's initialization routines might need to set or retrieve state information from an uninitialized module.
- Extensibility through add-on scripts, specification files, etc. is limited to the state information that the program provides, and non-code-writing developers often have to wait too long for the developers to get around to adding a new variable.

The Property Manager system provides a single interface for chosen program state information, and allows the creation of new, user-specified variables dynamically at run-time. The latter capability is especially important for the JSBSim control system model because the various control system components (PID controllers, switches, summer, gains, etc.) that make up the control law definition for an aircraft exist only in a configuration file. At runtime — after parsing the component definitions — the components are instantiated, and the property manager creates a property to store the output value of each component.

Properties themselves are like global variables with selectively limited visibility (read or read/write) that are categorized into a hierarchical, tree-like structure that is similar to the structure of a Unix file system. The structure of the property tree includes a root node, sub nodes, (like subdirectories) and end-nodes (properties). Similar to a Unix file system, properties can be
referenced relative to the current node, or to the root node. Nodes can be grafted onto other nodes similar to symbolically linking files or directories to other files or directories in a file system. Properties are used throughout JSBSim and FlightGear to refer to specific parameters in program code. Properties can be assigned from the command line, from specification files and scripts, and even via a socket interface. Property names look like: `position/h-sl-ft`, and `aero/qbar-psf`.

To illustrate the power of using properties and configuration files, consider the case of a high-performance jet aircraft model. Assume for a moment that a new switch has been added to the control panel for the example aircraft that allows the pilot to override pitch limits in the FCS. For FlightGear, the instrument panel is defined in a configuration file, and the switch is defined
there for visual display. A property name is also assigned to the switch definition. Within the flight control portion of the JSBSim aircraft specification file, that same property name assigned to the pitch override switch in the instrument panel definition file can be used to channel the control laws through the desired path as a function of the switch position. No code needs to be touched.

Specific simulation parameters are available both from within JSBSim and in configuration file specifications via properties. As mentioned earlier, “properties” are the term we use to describe parameters that we can access or set from within a configuration file, or on the command line.

Many properties are standard properties — i.e. those properties that are always present for all vehicles. The aerodynamic coefficients, engines, thrusters, and flight control/autopilot models will also have dynamically defined properties. This is because the whole set of aerodynamic coefficients, engines, etc. will not be known until after the relevant configuration file for an aircraft is read. One must know the convention used to name the properties for these parameters in order to access them. As an example, the flight control system for the X-15 model features the following components, among others:

```xml
<flight_control name="X-15">
   <channel name="Pitch">
      <summer name="fcs/pitch-trim-sum">
         <input> fcs/elevator-cmd-norm </input>
         <input> fcs/pitch-trim-cmd-norm </input>
         <clipto>
            <min> -1 </min>
            <max>  1 </max>
         </clipto>
      </summer>
      <aerosurface_scale name="fcs/pitch-command-scale">
         <input> fcs/pitch-trim-sum </input>
         <range>
            <min> -50 </min>
            <max>  50 </max>
         </range>
      </aerosurface_scale>
      <pure_gain name="fcs/pitch-gain-1">
         <input> fcs/pitch-command-scale </input>
         <gain> -0.36 </gain>
      </pure_gain>
   </channel>
</flight_control>
```

The first component above (`fcs/pitch-trim-sum`) takes input from two places, the known static properties, `fcs/elevator-cmd-norm` and `fcs/pitch-trim-cmd-norm`. The next component takes as input the output from the first component. The input property listed for the second component is `fcs/pitch-trim-sum`. Continuing with the above case shows that the last component, `fcs/pitch-gain-1`, takes as input the output from the preceding component, `fcs/pitch-command-scale`, which is given the property name, `fcs/pitch-command-scale`.

So, now we have a way to access many parameters inside JSBSim. We know how the FCS is assembled in JSBSim. The same components used in the FCS are also available to build an autopilot, or other system.

## Math

### Functions

The function specification in JSBSim is a powerful and versatile resource that allows algebraic functions to be defined in a JSBSim configuration file. The function syntax is similar in concept to MathML (Mathematical Markup Language, [http://www.w3.org/Math/](http://www.w3.org/Math/)), but it is simpler and more terse.

A function definition consists of an operation, a value, a table, or a property (which evaluates
to a value). The currently supported operations are:

- `sum` (takes n arguments)
- `difference` (takes n arguments)
- `product` (takes n arguments)
- `quotient` (takes 2 arguments)
- `pow` (takes 2 arguments)
- `exp` (takes 2 arguments)
- `abs` (takes n arguments)
- `sin` (takes 1 arguments)
- `cos` (takes 1 arguments)
- `tan` (takes 1 arguments)
- `asin` (takes 1 arguments)
- `acos` (takes 1 arguments)
- `atan` (takes 1 arguments)
- `atan2` (takes 2 arguments)
- `min` (takes n arguments)
- `max` (takes n arguments)
- `avg` (takes n arguments)
- `fraction` (takes 1 argument)
- `mod` (takes 2 arguments)
- `lt` (less than, takes 2 args)
- `le` (less equal, takes 2 args)
- `gt` (greater than, takes 2 args)
- `ge` (greater than, takes 2 args)
- `eq` (equal, takes 2 args)
- `nq` (not equal, takes 2 args)
- `and` (takes n args)
- `or` (takes n args)
- `not` (takes 1 args)
- `if-then` (takes 2-3 args)
- `switch` (takes 2 or more args)
- `random` (Gaussian random number, takes no arguments)
- `integer` (takes one argument)

An operation is defined in the configuration file as in the following example:

```xml
<sum>
   <value> 3.14159 </value>
   <property> velocities/qbar </property>
   <product>
      <value> 0.125 </value>
      <property> metrics/wingarea </property>
   </product>
</sum>
```

In the example above, the sum element contains three other items. What gets evaluated is written algebraically as:

\\[
3.14159 + \mathtt{qbar} + \big( 0.125 \cdot \mathtt{wingarea} \big)
\\]

A full function definition, such as is used in the aerodynamics section of a configuration file includes the function element, and other elements. It should be noted that there can be only one non-optional (non-documentation) element — that is, one operation element — in the top-level function definition. The <function> element cannot have more than one immediate child operation, `property`, `table`, or `value` element. Almost always, the first operation within the function element will be a product or sum. For example:

```xml
<function name="aero/moment/roll_moment_due_to_yaw_rate">
   <description> Roll moment due to yaw rate </description>
   <product>
      <property> aero/qbar-area </property>
      <property> metrics/bw-ft </property>
      <property> velocities/r-aero-rad_sec </property>
      <property> aero/bi2vel </property>
      <table>
         <independentVar> aero/alpha-rad </independentVar>
         <tableData>
            0.000 0.08
            0.094 0.19
            ...   ...
         </tableData>
      </table>
   </product>
</function>
```

The “lowest level” in a function definition is always a value or a property, which cannot itself contain another element. As shown, operations can contain values, properties, tables, or other operations.

Some operations take only a single argument. That argument, however, can be an operation (such as sum) which can contain other items. The point to keep in mind is any such contained operation evaluates to a single value — which is just what the trigonometric functions require (except atan2 , which takes two arguments).

Finally, within a function definition, there are some shorthand aliases that can be used for brevity in place of the standard element tags. Properties, values, and tables are normally referred to with the tags, `<property>`, `<value>`, and `<table>`. Within a function definition only, those elements can be referred to with the tags, `<p>`, `<v>`, and `<t>`. Thus, the previous example could be written to look like this:

```xml
<function name="aero/moment/roll_moment_due_to_yaw_rate">
   <description>Roll moment due to yaw rate</description>
   <product>
      <p> aero/qbar-area </p>
      <p> metrics/bw-ft </p>
      <p> aero/bi2vel </p>
      <p> velocities/r-aero-rad_sec </p>
      <t>
         <independentVar> aero/alpha-rad </independentVar>
         <tableData>
            0.000 0.08
            0.094 0.19
            ...   ...
         </tableData>
      </t>
   </product>
</function>
```

An example of tabular functions used in aerodynamic modeling is given by ground-effect factors affecting lift and drag. An explanation of the ground effect is given in the figure below.

{% include image.html
  url="/assets/img/ac_ground_effect.svg"
  width="100%"
  description="Explanation of ground effect."
  %}

To see how the ground effect can be modelled in JSBSim one can look at the Cessna 172 Skyhawk model. This is implemented in the file: `<JSBSim-root-dir>/aircraft/c172p/c172p.xml`. In the `<aerodynamics/>` block of this XML file two non-dimensional factors are modeled, $K_{C_D,\mathrm{ge}}$ and $K_{C_L,\mathrm{ge}}$, which are functions of the non-dimensional height above the ground and are to be thought of as multipliers of lift and drag, respectively. These factors are defined as follows:

```xml
<function name="aero/function/kCDge">
   <description>Change in drag due to ground effect</description>
   <product>
      <value>1.0</value>
      <table>
         <independentVar> aero/h_b-mac-ft </independentVar>
         <tableData>
            0.0000 0.4800
            0.1000 0.5150
            0.1500 0.6290
            0.2000 0.7090
            0.3000 0.8150
            0.4000 0.8820
            0.5000 0.9280
            0.6000 0.9620
            0.7000 0.9880
            0.8000 1.0000
            0.9000 1.0000
            1.0000 1.0000
            1.1000 1.0000
         </tableData>
      </table>
   </product>
</function>

<function name="aero/function/kCLge">
   <description>Change in lift due to ground effect</description>
   <product>
      <value>1.0</value>
      <table>
         <independentVar> aero/h_b-mac-ft </independentVar>
         <tableData>
            0.0000 1.2030
            0.1000 1.1270
            0.1500 1.0900
            0.2000 1.0730
            0.3000 1.0460
            0.4000 1.0550
            0.5000 1.0190
            0.6000 1.0130
            0.7000 1.0080
            0.8000 1.0060
            0.9000 1.0030
            1.0000 1.0020
            1.1000 1.0000
         </tableData>
      </table>
   </product>
</function>
```

The tabular functions `aero/function/kCDge and aero/function/kCLge`, representing the factors $K_{C_D,\mathrm{ge}}$ and $K_{C_L,\mathrm{ge}}$, are plotted in the figure below against the non-dimensional ground altitude $h/(b/2)$. The ground-effect is seen when the aircraft altitude above the ground is less than the wing semi-span $b/2$. For higher altitudes each of these two factors assume value 1.

{% include image.html
  url="/assets/img/c172_ground_effect_CL_CD.png"
  width="70%"
  description="Plotted functions of non-dimensional ground altitude $h/(b/2)$, defining the properties named 'aero/function/kCLge' and 'aero/function/kCDge' in the aerodynamic model of c172p."
  %}

### Tables

One, two, or three dimensional lookup tables can be defined in JSBSim for use in aerodynamics and function definitions. For a single "vector" lookup table, the format is as follows:

```xml
<table name="property_name_0">
   <independentVar lookup="row"> property_name_1 </independentVar>
   <tableData>
      key_1  value_1
      key_2  value_2
      ...    ...
      key_n  value_n
   </tableData>
</table>
```

The `lookup="row"` attribute in the `<independentVar/>` element is optional in this case; it is assumed that the `independentVar` is a row variable. A real example is as shown here:

```xml
<table>
   <independentVar lookup="row"> aero/alpha-rad </independentVar>
   <tableData>
      -1.57  1.500
      -0.26  0.033
       0.00  0.025
       0.26  0.033
       1.57  1.500
   </tableData>
</table>
```

The first column in the data table represents the lookup index (or *breakpoints*, or keys). In this case, the lookup index is `aero/alpha-rad` (angle of attack in radians). If `aero/alpha-rad` is $0.26$ radians, the value returned from the lookup table would be $0.033$.

The definition for a 2D table, is as follows:

```xml
<table name="property_name_0">
   <independentVar lookup="row">    property_name_1 </independentVar>
   <independentVar lookup="column"> property_name_2 </independentVar>
   <tableData>
                  {col_1_key   col_2_key   ...  col_n_key }
      {row_1_key} {col_1_data  col_2_data  ...  col_n_data}
      {row_2_key} {...         ...         ...  ...       }
      {   ...   } {...         ...         ...  ...       }
      {row_n_key} {...         ...         ...  ...       }
   </tableData>
</table>
```

The data is in a gridded format. A real example is as shown below. Alpha in radians is the row lookup (alpha breakpoints are arranged in the first column) and flap position in degrees is split up in columns for deflections of 0, 10, 20, and 30 degrees):

```xml
<table>
   <independentVar lookup="row">    aero/alpha-rad   </independentVar>
   <independentVar lookup="column"> fcs/flap-pos-deg </independentVar>
   <tableData>
                 0.0          10.0        20.0       30.0
     -0.0523599  8.96747e-05  0.00231942  0.0059252  0.00835082
     -0.0349066  0.000313268  0.00567451  0.0108461  0.0140545
     -0.0174533  0.00201318   0.0105059   0.0172432  0.0212346
      0.0        0.0051894    0.0168137   0.0251167  0.0298909
      0.0174533  0.00993967   0.0247521   0.0346492  0.0402205
      0.0349066  0.0162201    0.0342207   0.0457119  0.0520802
      0.0523599  0.0240308    0.0452195   0.0583047  0.0654701
      0.0698132  0.0333717    0.0577485   0.0724278  0.0803902
      0.0872664  0.0442427    0.0718077   0.088081   0.0968405
  </tableData>
</table>
```

The definition for a 3D table in a coefficient would be (for example):

```xml
<table name="property_name_0">
   <independentVar lookup="row">    property_name_1 </independentVar>
   <independentVar lookup="column"> property_name_2 </independentVar>
   <independentVar lookup="table">  property_name_3 </independentVar>
   <tableData  breakpoint="table_1_key">
                  {col_1_key   col_2_key   ...  col_n_key }
      {row_1_key} {col_1_data  col_2_data  ...  col_n_data}
      {row_2_key} {...         ...         ...  ...       }
      {   ...   } {...         ...         ...  ...       }
      {row_n_key} {...         ...         ...  ...       }
   </tableData>
   <tableData  breakpoint="table_2_key">
                  {col_1_key   col_2_key   ...  col_n_key }
      {row_1_key} {col_1_data  col_2_data  ...  col_n_data}
      {row_2_key} {...         ...         ...  ...       }
      {   ...   } {...         ...         ...  ...       }
      {row_n_key} {...         ...         ...  ...       }
   </tableData>
   ...
   <tableData  breakpoint="table_n_key">
                  {col_1_key   col_2_key   ...  col_n_key }
      {row_1_key} {col_1_data  col_2_data  ...  col_n_data}
      {row_2_key} {...         ...         ...  ...       }
      {   ...   } {...         ...         ...  ...       }
      {row_n_key} {...         ...         ...  ...       }
   </tableData>   
</table>
```

Note the breakpoint attribute in the tableData element, above. Here’s an example:

```xml
<table>
   <independentVar lookup="row">    fcs/row-value    </independentVar>
   <independentVar lookup="column"> fcs/column-value </independentVar>
   <independentVar lookup="table">  fcs/table-value  </independentVar>
   <tableData breakPoint="-1.0">
           -1.0    1.0
      0.0  1.0000  2.0000
      1.0  3.0000  4.0000
   </tableData>
   <tableData breakPoint="0.0000">
           0.0     10.0
      2.0  1.0000  2.0000
      3.0  3.0000  4.0000
   </tableData>
   <tableData breakPoint="1.0">
            0.0     10.0    20.0
       2.0  1.0000  2.0000  3.0000
       3.0  4.0000  5.0000  6.0000
      10.0  7.0000  8.0000  9.0000
   </tableData>
</table>
```

Note that table values are interpolated linearly, and no extrapolation is done at the table limits — the highest value a table will return is the highest value that is defined.

---

**TODO:** In JSBSim $n$-dimensional table with $n>3$ are also supported. Show how they can be formatted.

---

## Forces and Moments

### Aerodynamics

There are several ways to model the aerodynamic forces and moments (torques) that act on an aircraft. JSBSim started out by using the coefficient buildup method. In the coefficient buildup method, the lift force (for instance) is determined by summing all of the contributions to lift. The contributions differ depending on the aircraft and the fidelity of the model, but contributions to lift can include those from:

- Wing
- Elevator
- Flaps

Aerodynamic coefficients are numbers which, when multiplied by certain other values (such as dynamic pressure and wing area), result in a force or moment. The coefficients can be taken from flight test reports or textbooks, or they can be calculated using software (such as Digital DATCOM or other commercially available programs) or by hand calculations. Eventually, JSBSim added support for aerodynamic properties specified as functions. Within the `<aerodynamics>` section of a configuration file there are six subsections representing the 3 force and 3 moment axes (for a total of six degrees of freedom). The basic layout of the aerodynamics section is as follows:

```xml
<aerodynamics>
   <axis name="DRAG">
      { force contributions }
   </axis>
   <axis name="SIDE">
      { force contributions }
   </axis>
   <axis name="LIFT">
      { force contributions }
   </axis>
   <axis name="ROLL">
      { moment contributions }
   </axis>
   <axis name="PITCH">
      { moment contributions }
   </axis>
   <axis name="YAW">
      { moment contributions }
   </axis>
</aerodynamics>
```

Individual axes are not all absolutely required. There are several standard grouped sets of axes that are supported in JSBSim:

- `"DRAG"`, `"SIDE"`, `"LIFT"` (wind axes)
- `"X"`, `"Y"`, `"Z"` (body axes)
- `"AXIAL"`, `"SIDE"`, `"NORMAL"` (body axes)

All three systems accept `"ROLL"`, `"PITCH"`, `"YAW"` axis definitions. The axial systems cannot be mixed.
Within the axis elements, functions are used to define individual force or moment contributions to the total for that axis. Functions are used throughout JSBSim. In defining a force or moment, functions can employ the use of tables, constants, trigonometric functions, or other standard C
library functions. Simulation parameters are referenced via properties. Here is an example:

```xml
<function name="aero/force/lift_due_to_flap_deflection">
   <description>Lift contribution due to flap deflection</description>
   <product>
      <property>aero/function/ground-effect-factor-lift</property>
      <property>aero/qbar-area</property>
      <table>
         <independentVar>fcs/flap-pos-deg</independentVar>
         <tableData>
             0.0  0.0
            10.0  0.20
            20.0  0.30
            30.0  0.35
         </tableData>
      </table>
   </product>
</function>
```

In this case, a description in words of what the above does is as follows: the value of the function is the product of the `ground-effect-factor-lift`, `qbar-area`, and the value determined by the table, which is indexed as a function of flap position in degrees.

All of the functions in an `<axis/>` section are summed and applied to the aircraft in the appropriate manner. There is some flexibility in this format, though. Functions that are specified outside of any `<axis/>` section are created and calculated, but they do not specifically contribute to any force or moment total by themselves. However, they can be referenced by other functions that are in an `<axis/>` section. This technique allows calculations that might be applied to several individual functions to be performed once and used several times. The technique can be taken even further, with actual aerodynamic coefficients being calculated outside of an `<axis/>` definition, with the coefficients subsequently being multiplied within function definitions by the various factors (properties) that turn them into forces and moments inside an `<axis/>` definition.

As an example, let'’'s examine the instantaneous lift force $L(t)$. It is expressed with the following build-up formula:

$$
L = L_\mathrm{basic} \big(\alpha_\mathrm{B},\phi_\mathrm{hyst}\big) + \Delta L \big(\delta_\mathrm{flap}\big) + \Delta L \big(\delta_\mathrm{e}\big) + \Delta L \big(\dot{\alpha}_\mathrm{B}\big) + \Delta L \big( q \big)
\label{eq:Build:Up:Formula:Lift}
$$

where $\alpha_\mathrm{B}$, $\delta_\mathrm{flap}$, $\delta_\mathrm{e}$, $$\dot{\alpha}_\mathrm{B}$$ and $q$ are the well-known aircraft state variables. The non-dimensional scalar $\phi_\mathrm{hyst}$ is usually equal to 0 and becomes 1 at high angles of attack (near stall situations, when aerodynamic hysteresis effects are modeled).

The term $$L_\mathrm{basic} \big(\alpha_\mathrm{B},\phi_\mathrm{hyst}\big)$$ in (\ref{eq:Build:Up:Formula:Lift}) is called the “basic” contribution to the build-up and is dependent on the angle of attack. We know that increasing the angle of attack increases lift — up to a point. Lift force is traditionally defined as the product of filght dynamic pressure (“qbar”, $$\bar{q}$$, or $$\bar{q}_\infty$$ for aerodynamicists), wing area ($S_\mathrm{W}$ or simply $S$), and lift coefficient ($C_L$). In this case, the lift coefficient is determined via a lookup table, using $\alpha_\mathrm{B}$ and $\phi_\mathrm{hyst}$ as an index into the table:

```xml
<function name="aero/force/lift_from_alpha">
   <description> Lift due to alpha </description>
   <product>
      <property> aero/qbar-psf </property>
      <property> metrics/Sw-sqft </property>
      <property> aero/function/kCLge </property>
      <table>
         <independentVar lookup="row"> aero/alpha-rad </independentVar>
         <independentVar lookup="column"> aero/stall-hyst-norm </independentVar>
         <tableData>
                      0.0000   1.0000
            -0.0900  -0.2200  -0.2200
             0.0000   0.2500   0.2500
             0.0900   0.7300   0.7300
             0.1000   0.8300   0.7800
             0.1200   0.9200   0.7900
             0.1400   1.0200   0.8100
             0.1600   1.0800   0.8200
             0.1700   1.1300   0.8300
             0.1900   1.1900   0.8500
             0.2100   1.2500   0.8600
             0.2400   1.3500   0.8800
             0.2600   1.4400   0.9000
             0.2800   1.4700   0.9200
             0.3000   1.4300   0.9500
             0.3200   1.3800   0.9900
             0.3400   1.3000   1.0500
             0.3600   1.1500   1.1500
         </tableData>
      </table>
   </product>
</function>
```

The basic lift coefficient

$$
C_{L,\mathrm{basic}} = \frac{L_\mathrm{basic} \big(\alpha_\mathrm{B},\phi_\mathrm{hyst}\big) }{\bar{q} S}
\label{eq:Build:Up:Formula:Lift:Coefficient}
$$

is plotted below as a function of $\alpha_\mathrm{B}$ and $\phi_\mathrm{hyst}$.

{% include image.html
  url="/assets/img/c172_CL_basic.png"
  width="70%"
  description="The plotted function of two variables $C_{L,\mathrm{basic}}\big(\alpha_\mathrm{B},\phi_\mathrm{hyst}\big)$ corresponding to the tabular function named 'aero/coefficient/CLwbh' in the aerodynamic model of c172p."
  %}

TBD

---

{% include image.html
  url="/assets/img/c172_CD_basic.png"
  width="70%"
  description="The plotted function of two variables $C_{D,\mathrm{basic}}\big(\alpha_\mathrm{B},\delta_\mathrm{flap}\big)$ corresponding to the tabular function named 'aero/coefficient/CDwbh' in the aerodynamic model of c172p."
  %}

**TODO**

## Flight Control and System Modelling

Regarding the aircraft as a general dynamical system, it is subject to a vector $\boldsymbol{u}$ of control inputs. The number and types of inputs may depend on the particular aircraft under consideration. For a conventional configuration aircraft the minimum arrangement of the inputs is usually given by

\begin{equation}
\boldsymbol{u} = \big[ \,
\delta_\mathrm{T}, \, \delta_\mathrm{a}, \, \delta_\mathrm{e}, \, \delta_\mathrm{r}
\,\big]
\label{eq:Control:Inputs}
\end{equation}

where $\delta_\mathrm{T}$ is the throttle setting and $\delta_\mathrm{a}$, $\delta_\mathrm{e}$, and $\delta_\mathrm{r}$ are the angular deflections of right ailerons, elevator, and rudder, respectively. These quantities have standard signs and their range may vary according to the particular aircraft design. In flight simulation practice their variation is associated with the normalized setting of a corresponding control in the cockpit.

Usually the range of throttle setting goes from 0 (idle) to $+1$ (maximum power). Conceptually $\delta_\mathrm{T}$ may be considered as the current fraction of the maximum thrust output available at the actual flight speed and altitude.

The stick excursions are all mapped to a range that goes from $−1$ to $+1$.

These mappings often depend on the presence of control laws that may alter the final effect of pilot action on the actual effector deflections and thrust output.

In mathematical terms, whether the actual aerosurface deflections and thrust output or the normalized command ranges are considered, they are seen as a set of bounds for the control variables in the vector $\boldsymbol{u}$.

It has to be underlined, once again, that the number and types of control inputs are a feature of the given aircraft. Even if in the same broad category, two airplane designs might present substantially different arrangements and number of controls. But, generally speaking, at least their 'main' controls are conceptually the same: A pair of ailerons, a main longitudinal control, i.e. a pair of symmetrically moving elevators, and a rudder. In many cases the horizontal empennages have also a variable rigging angle with respect to the fuselage reference line, known as the angle $i_\mathrm{H}$ in the majority of flight mechanics textbooks.

### Conventions

{% include image.html
  url="/assets/img/ac_aerosurface_deflections.svg"
  width="80%"
  description="Standard aircraft aerodynamic control surfaces."
  %}

### Overview on Aerodynamic Modelling

Linearized pitch coefficient:

\begin{equation}
C_m = C_{m0} + C_{m\alpha} \, \alpha_\mathrm{B} + C_{m\delta_\mathrm{e}} \delta_\mathrm{e} + C_{m i_\mathrm{H}} \, i_\mathrm{H} + \left( C_{mq} \, q + C_{m\dot{\alpha}} \, \dot{\alpha}_\mathrm{B}\right) \frac{\bar{c}}{2V}
\label{eq:Cm}
\end{equation}

{% include image.html
  url="/assets/img/c172_fcs.svg"
  width="100%"
  description="The command to deflection logic for the elevator channel in the c172p model. The combination of yoke movement and pitch trim lever regulation is normalized and mapped to the interval $[−1, 1]$. The output of the channel is a real variable fcs/elevator-pos-rad representing an equivalent elevator deflection $\delta_\mathrm{e}^\star = \delta_\mathrm{e} + \delta_\mathrm{e,tab}^\star$. The angle $\delta_\mathrm{e,tab}^\star$ is an elevator deflection equivalent to the actual tab angle $\delta_\mathrm{e,tab}$. The $\delta_\mathrm{e}$ varies in the range $[\delta_\mathrm{e,min}, \delta_\mathrm{e,max}]$. The tail is represented with the moving surfaces deflected both in the equivalent condition (top), and in the actual condition (bottom)."
  %}

### Overview on Propulsion Modelling

{% include image.html
  url="/assets/img/ac_thrust_definitions.svg"
  width="80%"
  description="A twin engine propeller aircraft. Location in body frame of the engine thruster, of thrust application point, and thrust vector orientation."
  %}

{% include image.html
  url="/assets/img/c172_thruster.svg"
  width="80%"
  description="Locations associated to the entities 'thruster' and 'tank' in the FDM of c172p."
  %}
