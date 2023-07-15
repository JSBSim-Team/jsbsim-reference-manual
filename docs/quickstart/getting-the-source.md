---
title: Getting the source
description: Retrieving the JSBSim source code.
tags:
  - quickstart
  - building
---

# Getting the source

The GitHub repository of JSBSim is reachable at this link: [github.com/JSBSim-Team/jsbsim](https://github.com/JSBSim-Team/jsbsim). This repository mirrors the original one on SourceForge: [sourceforge.net/projects/jsbsim](https://sourceforge.net/projects/jsbsim).

## What you need to download the source

You need to have the [Git software](https://git-scm.com/) installed. Git is a *version control software*, a system that records changes to a file or set of files over time so that you can recall specific versions later. The JSBSim software source code files are being version controlled by Git.

To install Git [go to its download site](https://git-scm.com/downloads) and grab the version for your platform. You can choose to use Git locally on your computer in two ways: via one of the [GUI clients](https://git-scm.com/downloads/guis), or through a command shell (e.g. a *Bash shell* on Linux or Windows).

Once you have installed Git, assuming you are going to use Git from the command shell, the JSBSim source code public repository can be *cloned* from one of the two following locations.

## Downloading from [SourceForge](https://sourceforge.net/p/jsbsim/code/ci/master/tree/)

In such case the Git command to clone the repo is (HTTPS mode)

```bash
> git clone https://git.code.sf.net/p/jsbsim/code jsbsim-code
```  

or (SSH mode)

```bash
> git clone git://git.code.sf.net/p/jsbsim/code jsbsim-code
```  

## Downloading from [GitHub](https://github.com/JSBSim-Team/jsbsim)

in such case the Git command to clone the repo is (HTTPS mode)

```bash
> git clone https://github.com/JSBSim-Team/jsbsim.git jsbsim-code
```  

or (SSH mode)

```bash
> git clone git@github.com:JSBSim-Team/jsbsim.git jsbsim-code
```  

---

<figure markdown>
  ![Placeholder image](/assets/img/ac_airspeeds_recap.svg){: .center width="80%" }
  <figcaption>
	So, you want to simulate the flight of this aircraft?
  </figcaption>
</figure>
