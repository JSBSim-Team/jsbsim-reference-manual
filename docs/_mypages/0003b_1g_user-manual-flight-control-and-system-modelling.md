---
layout: default
title: Flight Control and System Modelling
categories: [menu, content, user-manual, flight-control-and-system-modelling]
permalink: /mypages/user-manual-flight-control-and-system-modelling/
---

# Flight Control and System Modelling

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

## Conventions

{% include image.html
  url="/assets/img/ac_aerosurface_deflections.svg"
  width="80%"
  description="Standard aircraft aerodynamic control surfaces."
  %}

## Overview on Aerodynamic Modelling

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

## Overview on Propulsion Modelling

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
