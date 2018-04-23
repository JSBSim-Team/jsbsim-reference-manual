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

---

**TODO**

... to be continued.

## Properties

## Math

## Forces and Moments

{% include image.html
  url="/assets/img/ac_ground_effect.svg"
  width="100%"
  description="Explanation of ground effect."
  %}

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
