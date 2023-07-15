---
title: Running the program
description: Running the JSBSim application.
tags:
  - quickstart
---

# Running the program

The path where the JSBSim repository is located will be called here *`<JSBSim-root-dir>`*. If you have built JSBSim from source code there will be an executable (`JSBSim` on Linux or `JSBSim.exe` on Windows) under the path `<JSBSim-root-dir>/src/` subdirectory. This is the JSBSim *standalone application*, that you might want to copy in the root directory:

```
<JSBSim-root-dir>$ cp src/JSBSim .
```

There may be several options specified when running the standalone JSBSim application.

```
<JSBSim-root-dir>$ JSBSim

Usage (items in brackets are optional):
  JSBSim [script name] [output directive files names] <options>
Options:
--help Returns a usage message
--version Returns the version number
--outputlogfile=<filename> Sets/replaces the name of the data log file
--logdirectivefile=<filename> Sets name of data log directives file
--root=<path> Sets the JSBSim root directory (where src/ resides)
--aircraft=<filename> Sets the name of the aircraft to be modeled
--script=<filename> Specifies a script to run
--realtime Specifies to run in actual real world time
--nice Directs JSBSim to run at low CPU usage
--suspend Specifies to suspend the simulation after initialization
--initfile=<filename> Specifies an initialization file to use
--catalog Directs JSBSim to list all properties for this model
  (--catalog can be specified on the command line along with a --aircraft option,
  or by itself, while also specifying the aircraft name, e.g. --catalog=c172)
--end-time=<time> Specifies the sim end time (e.g. time=20.5)
--property=<name=value> Sets a property to a value.
  For example: --property=simulation/integrator/rate/rotational=1

NOTE: There can be no spaces around the = sign when an option is followed by a filename
```

You can run JSBSim by supplying the name of a script:

```
<JSBSim-root-dir>$ JSBSim --script=scripts/c1723.xml
```

!!! note "TODO"

    Complete page contents.

---

<figure markdown>
  ![Placeholder image](/assets/img/ac_euler_gimbal.svg){: .center width="80%" }
  <figcaption>
	So, you want to simulate the flight of this aircraft?
  </figcaption>
</figure>
