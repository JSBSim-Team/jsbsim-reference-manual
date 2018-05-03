---
layout: default
title: Formulation manual - Overview
categories: [menu, content, formulation-manual, formulation-manual-overview]
permalink: /mypages/formulation-manual-overview/
---

# Overview

The equations of motion of a flying vehicle can be organized as a set of simultaneous first-order differential equations, explicitly solved for the derivatives. For $n$ independent variables, $x_i$ (such as components of position, velocity, etc.), and $m$ control inputs, $u_i$ (such as throttle, control surface deflection, etc.), the general form will be

$$
\left\{
  \begin{array}{rl}
    \dot{x}_1 & {}= f_1\big( x_1\,,\, x_2\,,\, \ldots \,,\,x_n\,,\,u_1\,,\, u_2\,,\, \ldots \,,\,u_m \big) \\
    \dot{x}_2 & {}= f_2\big( x_1\,,\, x_2\,,\, \ldots \,,\,x_n\,,\,u_1\,,\, u_2\,,\, \ldots \,,\,u_m \big) \\
      \cdots  & \quad \cdots \\
    \dot{x}_n & {}= f_n\big( x_1\,,\, x_2\,,\, \ldots \,,\,x_n\,,\,u_1\,,\, u_2\,,\, \ldots \,,\,u_m \big)
  \end{array}
\right.
\label{eq:EoM:ODE}
$$

where the functions $f_i$ are the nonlinear functions that arise from modeling vehicle's real subsystems. The variables $x:i$ constitute the smallest set of variables that, together with given inputs $u_i$, completely describe the behavior of the system (i.e. allow to deterministically compute its evolution in time), and called the *set of state variables* for the system, and Equations (\ref{eq:EoM:ODE}) are a *state-space* description of the system. The functions $f_i$ are single-valued continuous functions. Equations (\ref{eq:EoM:ODE}) are often written symbolically as

$$
\dot{\boldsymbol{x}} = \boldsymbol{f}\big( \boldsymbol{x}\,,\,\boldsymbol{u} \big)
\label{eq:EoM:ODE:Compact}
$$

where the state vector $\boldsymbol{x}$ is an $n \times 1$ column array of the $n$ state variables, the control vector $\boldsymbol{u}$ is an $m \times 1$ column array of the control variables, and $\boldsymbol{f}$ is an array of nonlinear functions.

When $\boldsymbol{u}$ is held constant, the nonlinear state equations (\ref{eq:EoM:ODE}), or a subset of them, usually have one or more *equilibrium points* in the multidimensional state and control space, where a given set of state variable derivatives vanish (usually derivatives having the meaning of translational or angular accelerations).

A major advantage of the state-space formulation is that the nonlinear state equations can be solved numerically. The simplest numerical solution method is Euler integration, described by

$$
\boldsymbol{x}(t_{k+1}) = \boldsymbol{x}(t_k) + \boldsymbol{f}\big( \boldsymbol{x}_k\,,\,\boldsymbol{u}_k \big) \, \Delta t
\label{eq:EoM:ODE:Euler:Integration}
$$

in which $\boldsymbol{x}(t_k)$ is the value of the state vector computed at discrete times $t_k = k \Delta t$, with $k = 0,1,2, \ldots$, starting from an assigned initial condition $\boldsymbol{x}(t_0) = \boldsymbol{x}_0$. The integration time step, $\Delta t$, must be made small enough that, for every $\Delta t$ interval, $\boldsymbol{u}$  can be approximated by a constant value $\boldsymbol{u}(t_k)$, and $\dot{\boldsymbol{x}} \Delta t$  provides a good approximation to the increment in the state vector. This numerical integration allows the state vector to be stepped forward, in time increments of $\Delta t$, to obtain a *time-history simulation*.

---

TBD
