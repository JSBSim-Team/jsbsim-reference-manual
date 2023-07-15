---
title: Quickstart
description: Getting started with JSBSim.
tags:
  - quickstart
---

# Quickstart

To use JSBSim productively you might want to assume a *programmer's attitude*. This means you will have to download the sources yourself and compile them on your platform. With the right set of tools installed on your computer, this is a painless procedure after all.

For the impatients, there are automatic remote build procedures that deliver up-to-date binaries of the library. These can be found on the following links:

## Builds provided by the FlightGear project developers ([Jenkins server](https://jenkins.io/))

- [JSBSim build for Linux (Linux CentOS 7 VM)](http://build.flightgear.org:8080/job/JSBsim)

  Go to the workspace area [build.flightgear.org:8080/job/JSBSim/ws](http://build.flightgear.org:8080/job/JSBSim/ws/) and download all files as a [Zip archive](http://build.flightgear.org:8080/job/JSBSim/ws/*zip*/JSBsim.zip). Explore the archive, go to the folder `/JSBSim/build/src/`, and find: the executable file `JSBSim` and the static library file `libJSBSim.a`.

- [JSBSim build for Windows](http://build.flightgear.org:8080/job/JSBsim-win)

Go to the workspace area [build.flightgear.org:8080/job/JSBSim-win/ws](http://build.flightgear.org:8080/job/JSBSim-win/ws/) and download all files as a [Zip archive](http://build.flightgear.org:8080/job/JSBSim-win/ws/*zip*/JSBSim-win.zip). Explore the archive, go to the folder `/JSBSim-win/build/src/Debug/`, and find: the executable file `JSBSim.exe` and the static library file `JSBSim.lib`.

This effort of providing pre-compiled binaries of JSBSim is part of the [continuous integration and delivery service](http://build.flightgear.org:8080/) for the [FlightGear](https://www.flightgear.org/) project. To learn more about continuous integration with Jenkins you might want to [visit this link](https://wiki.jenkins.io/display/JENKINS/Meet+Jenkins).

## Builds provided by the JSBSim-Team ([Travis server](https://travis-ci.org/) and [AppVeyor server](https://www.appveyor.com/))

The JSBSim-Team provides its own Continuous Integration service that delivers x64 binaries for both Ubuntu 14.04.5 LTS (Trusty Tahr) and MS Windows. The releases are tagged `v2018a` (or later) and can be downloaded [from the Releases section of the GitHub repository](https://github.com/JSBSim-Team/jsbsim/releases).

To check the current status of the latest builds one can go and visit the links:

- [Travis build for Ubuntu](https://travis-ci.org/JSBSim-Team/jsbsim) (include tests with both Python 2.7 and 3.6) [![Travis CI](https://travis-ci.org/JSBSim-Team/jsbsim.svg?branch=master)](https://travis-ci.org/JSBSim-Team/jsbsim)

- [AppVeyor build for Windows](https://ci.appveyor.com/project/agodemar/jsbsim/branch/master) (no tests) [![Build status](https://ci.appveyor.com/api/projects/status/89wkiqja63kc6h2v/branch/master?svg=true)](https://ci.appveyor.com/project/agodemar/jsbsim/branch/master)

<figure markdown>
  ![Placeholder image](/assets/img/ac_sideview_climb_simplified.svg){: .center width="80%" }
  <figcaption>
	So, you want to simulate the flight of this aircraft?
  </figcaption>
</figure>
