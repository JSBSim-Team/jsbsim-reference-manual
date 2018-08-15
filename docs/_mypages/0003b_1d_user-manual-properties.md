---
layout: default
title: User Manual - Properties
categories: [menu, content, user-manual, properties]
permalink: /mypages/user-manual-properties/
---

# Properties

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
