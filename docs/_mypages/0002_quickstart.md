---
layout: default
title: Quickstart
categories: [menu, content, quickstart]
permalink: /mypages/quickstart/
---

# Quickstart

To use JSBSim productively you might wanto to assume a *programmer's attitude*. This means you will have to download the sources yourself and compile them on your platform. With the right set of tools installed on your computer, this is a painless procedure after all.

For the impatients, there is an automatic remote build procedure that delivers up-to-date binaries of the library. These can be found on the following links on the [Jenkins](https://jenkins.io/) server:

- [JSBSim build for Linux (Linux CentOS 7 VM)](http://build.flightgear.org:8080/job/JSBsim)

  Go to the workspace area [build.flightgear.org:8080/job/JSBSim/ws](http://build.flightgear.org:8080/job/JSBSim/ws/) and download all files as a [Zip archive](http://build.flightgear.org:8080/job/JSBSim/ws/*zip*/JSBsim.zip). Explore the archive, go to the folder `/JSBSim/build/src/`, and find: the executable file `JSBSim` and the static library file `libJSBSim.a`.

- [JSBSim build for Windows](http://build.flightgear.org:8080/job/JSBsim-win)

Go to the workspace area [build.flightgear.org:8080/job/JSBSim-win/ws](http://build.flightgear.org:8080/job/JSBSim-win/ws/) and download all files as a [Zip archive](http://build.flightgear.org:8080/job/JSBSim-win/ws/*zip*/JSBSim-win.zip). Explore the archive, go to the folder `/JSBSim-win/build/src/Debug/`, and find: the executable file `JSBSim.exe` and the static library file `JSBSim.lib`.


This effort of providing pre-compiled binaries of JSBSim is part of the [continuous integration and delivery service](http://build.flightgear.org:8080/) for the [FlightGear](flightgear.org) project. To learn more about continuous integration with Jenkins you might want to [visit this link](https://wiki.jenkins.io/display/JENKINS/Meet+Jenkins).

{% include image.html
  url="/assets/img/ac_sideview_climb_simplified.svg"
  width="80%"
  description="So, you want to simulate the flight of this aircraft?"
  %}

<p align="right">
{% include search_page_put.html page_category='getting-the-source' put_text='Next ▶' %}</p>
