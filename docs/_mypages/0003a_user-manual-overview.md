---
layout: default
title: Overview
parent: User Manual
nav_order: 100
categories: [menu, content, user-manual, user-manual-overview]
permalink: /mypages/user-manual-overview/
---

# Overview

## What, exactly, is JSBSim?

From an application programming perspective, JSBSim is a collection of program code mostly written in the C++ programming language (but some C language routines are included). Some of the C++ classes that comprise JSBSim model physical entities such as the atmosphere, a flight control system, or an engine. Some of the classes encapsulate concepts or mathematical constructs such as the equations of motion, a matrix, quaternion, or vector. Some classes manage collections of other objects. Taken together, the JSBSim application takes control inputs, calculates and sums the forces and moments that result from those control inputs and the
environment, and advances the state of the vehicle (velocity, orientation, position, etc.) in discrete time steps.

JSBSim has been built and run on a wide variety of platforms such as a PC running Windows or Linux, Apple Macintosh, and even the IRIX operating system from Silicon Graphics. The free GNU g++ compiler easily compiles JSBSim, and other compilers such as those from Borland and Microsoft also work well. See the Programmers Guide for more information.

From an end-user perspective (perhaps a student doing research), JSBSim can be viewed as sort of a “black box” which is supplied with input files in XML format. These XML files contain descriptions of an aerospace vehicle, engines, scripts, and so on. When these files are loaded into JSBSim, they direct it to model the flight of that vehicle in real-time as part of a larger simulation framework (such as FlightGear or OpenEaagles), or faster than real-time in a batch mode. Each run of JSBSim would result in data files showing performance and dynamics of the vehicle being simulated and studied.

From a software integrator perspective (such as someone integrating JSBSim within a larger simulation framework), JSBSim is a library that can be called, supplied with inputs (such as control inputs from the pilot), and returning outputs (describing where the vehicle is at any moment in time).

## Who is it for, and how can it be used?

The JSBSim flight dynamics model (FDM) software library is meant to be reasonably easy to comprehend, and is designed to be useful to advanced aerospace engineering students. Due to the ease with which it can be configured, it has also proven to be useful to industry professionals in a number of ways. It has been incorporated into larger, full-featured, flight simulation applications and architectures (such as FlightGear, Outerra, and OpenEaagles), and has been used as a batch simulation tool in industry and academia.

## Examples of use

### Aerocross Echo Hawk

JSBSim has been used for Hardware-in-the-Loop (HITL) testing of the Aerocross Echo Hawk UAV. Custom code was written to interface with the flight hardware (PC/104-based system) via RS-232/422/485, proportional analog I/O, discrete I/O, and sockets, but the core simulation code was unaltered JSBSim code. Pilot/operator training also relies on JSBSim as the 6-DoF code.

### DuPont Aerospace Company

JSBSim was used at duPont Aerospace Company along with Matlab for real-time HITL simulation and pilot/operator training. Rex duPont of duPont Aerospace Company explained the project:

> In the 1990s duPont Aerospace Company was building an airplane to test its concept for a vertical takeoff fan jet transport plane. We had developed a Microsoft Windows-based flight simulator that we had used to test the flying qualities of the proposed craft. However, we needed a simulation that we could use in real time so that we could test the flight characteristics on a full-sized mockup with the flight actuators operating in the loop. We settled on the FlightGear simulator, using the JSBSim flight dynamics model because we could get the full code, it was nicely organized so that we could create new subprograms to match our aircraft, and support was readily available.

> We developed simultaneously a Matlab simulator for the use in developing more effective autopilot guidance systems, since our primary task became to take the aircraft off using the autopilot alone and to hover in place for 30 seconds. This would show definitively that the control system was sufficiently robust. Therefore, we built into each relevant module of the Matlab simulator and the JSBSim derivative simulator a series of unit tests that provided a sequence of inputs to each model that could be cross verified to ensure that the two systems stayed in sync.

> We used the JSBSim system to test a number of dynamic issues that were not easily testable with the Matlab model, especially issues involving pilot feel and the controllability during transition to and from hover. These issues are hard to evaluate in the pure control-
system world of Matlab because during transition the underlying force structure is continuously varying as aerodynamic forces become more important and pure thrust control forces less.

> We also did parametric studies on such issues as the sensitivity of the key parameters in the aerodynamic simulation to possible errors in estimation. These were done by having the pilot fly a series of standard maneuvers designed to test the aircraft's response when one or more parameter was degraded by as much as 50% (without the pilot knowing which one was changed).

> We simulated various servo bandwidths as well, testing to see at what point the flying characteristics became unacceptable. This helped define the characteristics needed. What pilots desire from control systems is almost always different from the optimal theoretical parameters.

> Additionally, we developed a number of HUD display systems that facilitated operations during hover, where very precise control of ground speed is required. Eventually we achieved a system that allowed a young engineer who did not even have a pilot's license to take off and hold a hover at constant altitude to within one foot for over 30 seconds.

> We finally achieved our goal of autopilot controlled take-off and hover in two flights of approximately 45 seconds duration on September 30, 2007. Both flights were terminated because one of the engines ran out of fuel, rather than for any control problems.

### MITRE Air Traffic Studies

JSBSim is being used at MITRE in developing a 6-DoF simulation of the FMS (Flight Management System) behavior during CDAs (Continuous Descent Arrival) and OPDs (Optimized Profile Descent). Both the standalone version of JSBSim (for batch runs) and a version integrated with FlightGear have been used. Additional control system components have been created to support specific lateral and vertical navigation studies.

JSBSim has also been extended to handle output of messages over a socket to another application used at MITRE which provides a view
similar to what an Air Traffic Control operator would see.

### U.S. Department of Transportation

In work done with and for the U.S. D.O.T., a human pilot math model was developed using JSBSim as the 6-DoF (six degree-of-freedom) simulation core.

### The University of Naples, Italy, Federico II

The University of Naples has a motion base flying/driving simulator that is driven by FlightGear and JSBSim. The simulator has a three-screen visual presentation that provides a 190 degree field-of-view. The JSBSim source code was modified to provide a force feedback capability.

JSBSim has been used at the University of Naples as a tool supporting risk level evaluations of near-ground flight operations. One of the practical problems considered in those collision risk studies consisted in the evaluation of threat posed to flight operations when a new obstacle (such as a building or radar tower) is placed inside the airport area. The risk evaluation has been
performed by varying the obstacle geometry and location. The risk assessment procedure has been based on the analysis of statistical deviations of aircraft trajectories from the “normal” flight path, evaluating the probability of a generic trajectory to cross a given “protection” area enveloping the potential obstacle. Within this framework, the operational scenario has been formally described and implemented in order to run multiple computer simulations.

### Fraunhofer Institute for Wind Energy Systems

In a joint research with the Italian University of Naples Federico II, researchers of Fraunhofer Institute for Wind Energy Systems (IWES) have studied the wake encounter problem occurring when light airplanes fly through or nearby wind turbine wakes.

For this research, a framework of software applications has been developed for generating and controlling a population of flight simulation scenarios in presence of assigned wind and turbulence fields. JSBSim was used in the framework as a flight dynamics model, with its autopilot systems adapted for simulating a realistic pilot behavior during navigation.
The wind distribution in the turbine wakes were calculated with OpenFOAM, and provided as input for the dynamic model.

### TFASA - Test Flying Academy of South Africa

The Test Flying Academy of South Africa has been using JSBSim as the basis for a ground based Variable Stability System (VSS) simulator for test pilot training. The aerodynamic stability and control coefficients of a base aircraft model are modified to demonstrate their effect on flying tasks. Actuators are also modelled to show their potential effect on PIO given varying amounts of lag, delay and rate limits.

Both fixed wing aircraft and rotary aircraft are simulated with programmable force-feedback inceptors in order to also demonstrate the effects of Flight Control Mechanical Characteristics (FCMC).

JSBSim is integrated with Prepar3D to make use of Prepar3D's outside visuals which are rendered on either three large LCDs or connected to a triple projector setup rendering a 180 degree view.

---

**TODO**

Add updated examples of use, 2014+.
