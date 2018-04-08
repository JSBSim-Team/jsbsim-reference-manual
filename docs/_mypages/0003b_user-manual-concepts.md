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

In the structural frame the X-axis increases from the nose towards the tail, the Y-axis increases from the fuselage out towards the right (when looking forward from the cockpit), and of course the Z-axis then is positive upwards. Typically, the origin $O_\mathrm{C}$ for this frame is near the front of the aircraft (at the tip of the nose, at the firewall, or in front of the nose some distance). This frame is often named $(O_\mathrm{C}, x_\mathrm{C}, y_\mathrm{C}, z_\mathrm{C})$.

The X-axis is typically coincident with the fuselage centerline and passes through the propeller hub (thrust axis). Positions along the $x_\mathrm{C}$ axis are referred to as stations. Positions along the $z_\mathrm{C}$ axis are referred to as waterline positions. Positions along the $y_\mathrm{C}$ axis are referred to as buttline positions.

Note that the origin can be anywhere for a JSBSim-modeled aircraft, because JSBSim internally only uses the relative distances between the CG and the various objects – not the discrete locations themselves.

{% include image.html
  url="/assets/img/ac_center_of_gravity.svg"
  width="90%"
  description="Center of gravity (CG) position, point $G$, determined in a construction frame."
  %}

### Body Frame

In JSBSim, the body frame is similar to the structural frame, but rotated 180 degrees about the $y_\mathrm{C}$, with the origin coincident with the CG. In this frame the aircraft forces and moments are summed and the resulting accelerations are integrated to get velocities.

The frame of body axes is often called $(G, x_\mathrm{B}, y_\mathrm{B}, z_\mathrm{B})$. The $x_\mathrm{C}$ axis is called the *roll axis* and points forward, the $y_\mathrm{B}$ axis is called *pitch axis* and points toward the right wing, the $z_\mathrm{B}$ axis is called *yaw axis* and points towards the fuselage belly.

{% include image.html
  url="/assets/img/ac_body_axes.svg"
  width="90%"
  description="Standard aircraft body axis frame, with origin at the center of gravity $G$."
  %}

### Stability, or "Aerodynamic" Frame

This frame, named $(G, x_\mathrm{A}, y_\mathrm{A}, z_\mathrm{A})$, is similar to the body frame, except that the axis $x_\mathrm{A}$ points into the relative wind vector projected onto the plane of symmetry for the aircraft $x_\mathrm{B} z_\mathrm{B}$. The axis $y_\mathrm{A}$ still points out the right wing and coincides with the body axis $x_\mathrm{B}$, and the axis $z_\mathrm{A}$ completes the right-hand system.

{% include image.html
  url="/assets/img/ac_aero_axes.svg"
  width="90%"
  description="Aerodynamic frame, defining the aerodynamic angles $\alpha_\mathrm{B}$ and $\beta$."
  %}

The two axes $x_\mathrm{A}$ and $z_\mathrm{A}$ belong, by definition, to the aircraft symmetry plane, but they can rotate during flight because the orientation of the relative wind velocity vector $\boldsymbol{V}$ might change with respect to the vehicle. The above figure shows how the aerodynamic frame is constructed. The angle between the two axes $x_\mathrm{A}$ and $x_\mathrm{B}$ is the aircraft angle of attack $\alpha_\mathrm{B}$. The angle formed by the instantaneous direction of $\boldsymbol{V}$ and its projection on the plane $x_\mathrm{B} z_\mathrm{B}$ is the sideslip angle $\beta$.

### Wind Frame

This frame is similar to the stability/aerodynamic frame, except that the X-axis points directly into the relative wind $\boldsymbol{V}$. The Z-axis is perpendicular to the X-axis, and remains within the aircraft body plane $x_\mathrm{B} z_\mathrm{B}$ (also called the reference plane). The Y-axis completes a right hand coordinate system.

When the sideslip angle $\beta$ is zero, the wind frame and the aerodynamic frame are coincident.

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
