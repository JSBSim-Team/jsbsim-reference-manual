---
title: State propagation contract
description: JSBSim's process driving state propagation.
---

# State propagation contract

DISCLAIMER: this section is a work in progress.
---

The state of the vehicle is propagated according to the following equation:

$$
\dot{\boldsymbol{x}}(t_{k}) = \boldsymbol{f}\big( \boldsymbol{x}(t_{k}),\dot{\boldsymbol{x}}(t_{k-1}),\boldsymbol{u} \big)
$$

The simulation is expressed as a **discrete-time integration problem**, where time is sampled at $t_k$ and $k$ is an integer index.

## 1.1 State Vector Definition

The propagated state vector is defined as:

$$
\boldsymbol{x} = \big[ u, v, w,\, p, q, r,\, x_{\text{cg}}, y_{\text{cg}}, z_{\text{cg}},\, q_0, q_1, q_2, q_3,\, \text{masses},\text{inertias}\big]
$$

where:

- $u, v, w$: CG's translational velocity components **w.r.t. ECI**, expressed in the **standard body-fixed frame**

- $p, q, r$: vehicle's angular velocity components **w.r.t. ECI**, expressed in the **standard body-fixed frame**

- $x_{\text{cg}}, y_{\text{cg}}, z_{\text{cg}}$: CG's position coordinates expressed in the **ECI frame**

- $q_0, q_1, q_2, q_3$: vehicle's attitude quaternion components defined in the **ECI frame**

- $\text{masses}$: the total mass, and possible individual masses of vehicle's sub-elements (tanks, etc.)

- $\text{inertias}$: the 9 elements of the vehicle's inertia matrix in body-frame

## 1.2 Derivative (Dynamics) Model

At each discrete time $t_k$, the derivative is defined as:

$$
\dot{\boldsymbol{x}}(t_k) = \boldsymbol{f} \left(
  \boldsymbol{x}(t_k), \boldsymbol{u}(t_k), \dot{\boldsymbol{x}}(t_{k-1}), t_k \right)
$$

where:

- $\boldsymbol{x}(t_i)$: current state

- $\boldsymbol{u}(t_i)$: current inputs (controls, propulsion, environment, etc.)

- $\dot{\boldsymbol{x}}(t_{i-1})$: previous-step state derivative

- $\boldsymbol{f}(\cdot)$: vector-valued function representing the RHS of the EOM in explicit form.

Including $\dot{\boldsymbol{x}}(t_{i-1})$ makes explicit what is already implicit in many simulator implementations:

- Predictor/corrector schemes  

- Slope reuse in multi-stage integrators  

- Iterative or stabilized propagation logic  

This formulation clarifies the conceptual boundary between:

- **Derivative formation** (evaluation of $\boldsymbol{f}$)

- **Numerical integration**

## 1.3 Numerical Integration Step

The state update is:

$$
\boldsymbol{x}(t_{i+1}) = \boldsymbol{x}(t_i) + \int_{t_i}^{t_{i+1}} \dot{\boldsymbol{x}}(t)\,dt
$$

The integral is approximated using the integrator selected inside `FGPropagate`.
This makes explicit that:

- `FGPropagate` performs numerical integration

- `FGFDMExec` determines execution ordering and scheduling

- The two together implement the discrete-time realization of the ODE

# 2. Observation Equation (Published Outputs)

In addition to propagation, the simulator produces outputs:

$$
\boldsymbol{y}(t_i) = \boldsymbol{g}\big(
  \boldsymbol{x}(t_i), \boldsymbol{u}(t_i), \ldots \big)
$$

where:

- $\boldsymbol{y}(t_i)$: published or observable outputs (aero angles, derived velocities, accelerations, navigation quantities, atmosphere values, etc.)

- $\boldsymbol{g}(\cdot)$: output mapping

- $\ldots $: additional internal variables (environment state, intermediate model results, property tree values)

This observation equation formalizes what is currently scattered across model execution and property publication.


TBD
