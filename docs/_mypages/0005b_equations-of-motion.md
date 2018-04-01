---
layout: default
title: Formulation manual - Equations of motion
categories: [menu, content, formulation-manual, formulation-manual-equations-of-motion]
permalink: /mypages/formulation-manual-equations-of-motion/
---

# Equations of motion

The core purpose of a flight dynamics model is to propagate and track the path of a flying craft over the surface of the Earth (or another planet), given the forces and moments that act on the vehicle. We know the characteristics of the aircraft, and we know the characteristics of the planet (gravity, rotation rate, etc.). And it is expected that the reader is familiar with rigid body dynamics, where moving reference frames are involved. Still, putting all of the pieces together in a flight
simulator can be overwhelming and tedious.

This section discusses aerospace vehicle equations of motion, as implemented in `JSBSim::FGPropagate`, using the quaternion, matrix, vector, and location math classes provided in JSBSim. Many of the equations listed in the following sections related to the rigid body equations of motion are taken from the book **(Stevens:Lewis:Johnson:2015)**, which is considered the main formulation reference for the JSBSim software.

The notation used in this reference manual is the same that Stevens and Lewis use:

- The lower right subscript, e.g. $$\boldsymbol{v}_\mathrm{CM/e}$$, describes the object or frame relationship of the parameter.
  In the example given, $$\boldsymbol{v}_\mathrm{CM/e}$$, we refer to the velocity of the CM (center of mass) with respect to the ECEF frame.

- The upper right superscript, e.g. $\boldsymbol{v}^\mathrm{b}$, refers to a coordinate system.
  That is, it states which coordinate system the motion is expressed in.

- The left superscript specifies the frame in which a derivative is taken.

**To be completed**

{% include image.html
  url="/assets/img/inertial_frame.png"
  width="60%"
  description="Earth-Centered Inertial (ECI) frame and Earth-Centered Earth-Fixed (ECEF) frame."
  %}

{% include image.html
  url="/assets/img/earth_frames.png"
  width="60%"
  description="Earth-Centered Earth-Fixed (ECEF) frame, geografic coordinates, Tangent (T) frame, and local Vertical (V) frame."
  %}
