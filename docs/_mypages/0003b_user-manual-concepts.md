---
layout: default
title: User manual - Concepts
categories: [menu, content, user-manual, concepts]
permalink: /mypages/concepts/
---

# Concepts

## Simulation

While the JSBSim user does not need to know some of the finer details of the flight simulator operation, it can be helpful to understand basically how JSBSim works. Some of the most important concepts are described in this section.

Frames of reference are used to describe the placement and location of various items in a vehicle model.

There is flexibility in how the units of measure can be specified when defining a vehicle model – both English and metric units are supported.

The use of “Properties” permits JSBSim to be a generic simulator, providing a way to interface the various systems with parameters (or variables). Properties are used throughout the configuration files that describe aircraft and engine characteristics.

Obviously, math plays a big part in modeling flight physics. JSBSim makes use of data tables, as flight dynamics characteristics are often stored in tables. Arbitrary algebraic functions can also be set up in JSBSim, allowing broad freedom for describing aerodynamic and flight control characteristics.

## Frames of Reference

Before moving into a description of the configuration file syntax, one must understand some basic information about some of the frames of reference used in describing the location of objects on the aircraft.

### Structural, or "Construction" Frame

This frame is a common manufacturer's frame of reference and is used to define points on the aircraft such as the center of gravity, the locations of all the wheels, the pilot eye-point, point masses, thrusters, and so on. Items in the JSBSim aircraft configuration file are located using this frame.

In the structural frame the X-axis runs along the fuselage length and points towards the tail, the Y-axis points from the fuselage out towards the right wing, and of course the Z-axis then is positive upwards. Typically, the origin $O_\mathrm{C}$ for this frame is near the front of the aircraft (at the tip of the nose, at the firewall for a single engine airplane, or at some distance in front of the nose). This frame is often named $$\mathcal{F}_\mathrm{C} = \{O_\mathrm{C}, x_\mathrm{C}, y_\mathrm{C}, z_\mathrm{C}\}$$.

{% include image.html
  url="/assets/img/ac_construction_axes.svg"
  width="90%"
  description="Aircraft structural (or construction) frame of reference with origin $O_\mathrm{C}$. Besides the structural frame axes $x_\mathrm{C}$, $y_\mathrm{C}$, and $z_\mathrm{C}$, the standard body frame axes $x_\mathrm{B}$, $y_\mathrm{B}$, and $z_\mathrm{B}$ are also shown with their origin at the center of mass $G$. The pilot's eye-point is located at $P_\mathrm{ep}$."
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

### Body Frame

In JSBSim, the body frame is similar to the structural frame, but rotated 180 degrees about the $y_\mathrm{C}$, with the origin coincident with the CG. Typycally, the body frame is defined by knowning the position of the airplane's center of mass $G$ and the direction of the longitudinal construction axis $x_\mathrm{C}$ with respect to the fuselage. The axis $x_\mathrm{B}$ is so taken that it originates from $G$, is parallel to $x_\mathrm{C}$, and points forward.

The frame of body axes is often called $$\mathcal{F}_\mathrm{B} = \{G, x_\mathrm{B}, y_\mathrm{B}, z_\mathrm{B}\}$$. The $x_\mathrm{B}$ axis is called the *roll axis* and points forward, the $y_\mathrm{B}$ axis is called *pitch axis* and points toward the right wing, the $z_\mathrm{B}$ axis is called *yaw axis* and points towards the fuselage belly.

{% include image.html
  url="/assets/img/ac_body_axes.svg"
  width="90%"
  description="Standard aircraft body axis frame, with origin at the center of gravity $G$."
  %}

In the body frame the aircraft forces and moments are summed and the resulting accelerations are integrated to get velocities.

### Stability, or "Aerodynamic" Frame

This frame is defined according to the instantaneous orientation of the relative wind vector with respect to the airframe. If, for simplycity, the air is still with respect to the Earth (no wind), and $\boldsymbol{V}$ is the aircraft center-of-mass velocity vector with respect to the Earth-fixed observer (also named $\boldsymbol{v}_\mathrm{CM/E}$ to emphasize the relative motion), then $-\boldsymbol{V}$ is the relative wind velocity and $V = \|\boldsymbol{V}\|$ is the airspeed.

The frame, named $$\mathcal{F}_\mathrm{A} = \{ G, x_\mathrm{A}, y_\mathrm{A}, z_\mathrm{A} \}$$, has the axis $x_\mathrm{A}$ that points into the relative wind vector projected onto the plane of symmetry for the aircraft, $x_\mathrm{B} z_\mathrm{B}$. The axis $y_\mathrm{A}$ still points out the right wing and coincides with the body axis $y_\mathrm{B}$, and the axis $z_\mathrm{A}$ completes the right-hand system.

{% include image.html
  url="/assets/img/ac_aero_axes.svg"
  width="90%"
  description="Aerodynamic frame, defining the aerodynamic angles $\alpha_\mathrm{B}$ and $\beta$."
  %}

The two axes $x_\mathrm{A}$ and $z_\mathrm{A}$ belong, by definition, to the aircraft symmetry plane, but *they can rotate during flight* because the orientation of the relative wind velocity vector $\boldsymbol{V}$ might change with respect to the vehicle. The above figure shows how the aerodynamic frame is constructed. The angle between the two axes $x_\mathrm{A}$ and $x_\mathrm{B}$ is the aircraft angle of attack $\alpha_\mathrm{B}$. The angle formed by the instantaneous direction of $\boldsymbol{V}$ and its projection on the plane $x_\mathrm{B} z_\mathrm{B}$ is the sideslip angle $\beta$.

This frame is called an 'aerodynamic' frame because the projection of the instantaneous aerodynamic resultant force $$\boldsymbol{F}_\mathrm{A}$$ onto the axes $x_\mathrm{A}$ and $z_\mathrm{A}$ defines the aerodynamic drag and lift. In particular, the drag $D$ is such that $-D$ is the component of $$\boldsymbol{F}_\mathrm{A}$$ along $x_\mathrm{A}$; the lift $L$ is such that $-L$ is the component of $$\boldsymbol{F}_\mathrm{A}$$ along $z_\mathrm{A}$. In presence of a nonzero sideslip angle $\beta$, a third nonzero component of $$\boldsymbol{F}_\mathrm{A}$$ arises along the lateral axis $y_\mathrm{B} \equiv y_\mathrm{A}$, i.e. the side force component named $Y_\mathrm{A}$.

To visualize the above observations, consider a typical maneuver studied in flight mechanics: the zero-sideslip (or 'corrected'), constant altitude turn at a steady airspeed. In this situation the wings are banked and so is the lift. In such a turn $$\mathcal{F}_\mathrm{A}$$ is banked and $x_\mathrm{A}$ is kept horizontal. In other words, for an aircraft the lift and drag are always defined in the symmetry plane.

*Remark* --- In dynamic stability studies what is referred to as 'stability frame' is something slightly different from the aerodynamic frame introduced above: The stability frame in aircraft flight dynamics and stability conventions is nothing but a particular kind of body-fixed frame, defined with respect to an initial symmetrical, steady, wings-level, constant altitude flight condition. This conditions gives the direction of $x_\mathrm{S}$ (which coincides with $x_\mathrm{A}$ at that particular flight attitude). Therefore, in dynamic stability studies the stability frame, unlike the aerodynamic frame, is fixed with the vehicle.

### Wind Frame

This frame is similar to the stability/aerodynamic frame, except that the X-axis points directly into the relative wind direction (velocity $$-\boldsymbol{V}=-\boldsymbol{v}_\mathrm{CM/E}$$ in calm air). The Z-axis is perpendicular to the X-axis, and remains within the aircraft body plane $x_\mathrm{B} z_\mathrm{B}$ (also called the reference plane). It turns out that the axis $z_\mathrm{W}$ coincides with the aerodynamic axis $z_\mathrm{A}$. The Y-axis completes a right hand coordinate system.

When the sideslip angle $\beta$ is zero, the wind frame and the aerodynamic frame are coincident.

{% include image.html
  url="/assets/img/ac_wind_axes.svg"
  width="90%"
  description="Standard frames of reference with the origin at the aircraft center of mass $G$. In this particular
situation the air is calm and the velocity vector $\boldsymbol{v}_\mathrm{CM/E}$, of $G$ with respect to the Earth-fixed observer, is horizontal and pointing to North; hence it gives the direction of the relative wind. The standard three aerodynamic resultant force components $D$ (drag), $L$ (lift) and $Y_\mathrm{A}$ (side force) are also shown, with the angle of attack $\alpha_\mathrm{B}$ (referred to $x_\mathrm{B}$) and the angle of sideslip $\beta$. The aircraft weight is a vector of magnitude $W = mg$, directed downwards, parallel to $z_\mathrm{V}$ (the local vertical)."
  %}

In the figure below again the standard frames of reference are shown, for an aircraft in climbing flight in calm air. By definition, the two axes $z_\mathrm{A}$ and $z_\mathrm{W}$ are coincident and the wind frame $$\mathcal{F}_\mathrm{W}$$ can be superimposed to the aerodynamic frame $$\mathcal{F}_\mathrm{A}$$ when rotated around $z_\mathrm{W}$ of the angle $-\beta$. The components $-D$ and $Y_\mathrm{A}$ can also be seen as the component of the resultant aerodynamic force on the axes $x_\mathrm{W}$ and $y_\mathrm{W}$.

{% include image.html
  url="/assets/img/three_d_definitions.svg"
  width="90%"
  description="Standard frames of reference and aircraft in climbing flight in calm air. The CG velocity vector $\boldsymbol{V}$ forms the flight path angle $\gamma$ with the horizontal plane. The standard three aerodynamic resultant force components $D$, $L$ and $Y_\mathrm{A}$ are also shown."
  %}

Therefore, the wind frame $$\mathcal{F}_\mathrm{W}$$ can be superimposed to the body frame $$\mathcal{F}_\mathrm{B}$$ when rotated first around $z_\mathrm{W}$ of the angle $-\beta$ then around the axis $y_\mathrm{A}$ of the angle $\alpha_\mathrm{B}$:

$$
\mathcal{F}_\mathrm{W} \stackrel{-\beta \, | \, z_\mathrm{W}}{ \longrightarrow } \mathcal{F}_\mathrm{A} \stackrel{\alpha_\mathrm{B} \, | \, y_\mathrm{A}}{ \longrightarrow } \mathcal{F}_\mathrm{B}
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
    -D \\ Y_\mathrm{A} \\ -L
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

## Flight Control and System Modelling
