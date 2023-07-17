---
title: Building the program
description: How to build JSBSim.
tag:
  - quickstart
  - building
---

# Building the program and the library

JSBSim can either be built with [CMake](https://cmake.org/) or [Microsoft Visual Studio](https://www.visualstudio.com/free-developer-offers/). If you are using a Mac OSX or a Linux platform, you must use CMake. If you are a Windows user you can use either one.

JSBSim is coded in standard C++98/C99 and has no dependencies, so all you need is a C/C++ compiler installed on your platform.

## Building with CMake

CMake is a multiplatform tool to build and test software. It can produce files to build JSBSim with GNU make or Microsoft Visual Studio. To keep the build files separated from the source code, it is preferable to build JSBSim in a separate directory.
```bash
> cd jsbsim-code
> mkdir build
> cd build
```
CMake *does not build* software, it produces files *for* a multitude of build tools. The following commands are assuming that you are using GNU make to build JSBSim.

First, you should invoke CMake and then execute make
```bash
> cmake ..
> make
```

This will compile the various classes, and build the JSBSim application which will be located in `build/src`

### Options passed to CMake

CMake can use a number of parameters to tune the build of JSBSim. Different options are presented below. You can use them independently or any combination thereof depending on your needs.

#### Passing parameters to the compiler

If you want to set compiler options, you can pass flags to CMake to build a `Debug` version of JSBSim. JSBSim also uses C for some code, you can set options for both the C++ and the C compiler.
```bash
> cmake -DCMAKE_CXX_FLAGS_DEBUG="-g -Wall" -DCMAKE_C_FLAGS_DEBUG="-g -Wall" -DCMAKE_BUILD_TYPE=Debug ..
> make
```
Or alternatively you can build a release version of JSBSim and request GNU Make to use 4 cores to build the executable faster.
```bash
> cmake -DCMAKE_CXX_FLAGS_RELEASE="-O3 -march=native -mtune=native" -DCMAKE_C_FLAGS_RELEASE="-O3 -march=native -mtune=native" -DCMAKE_BUILD_TYPE=Release ..
> make -j4
```

#### Building Expat or using the system library

JSBSim uses the [Expat library](https://libexpat.github.io/) to read XML files. The Expat source code is provided with JSBSim source code and is compiled along with JSBSim during its build. However, if Expat is already installed on your platform you might prefer to use your system Expat library in order to avoid duplication. In that case, you should pass the `SYSTEM_EXPAT` flag to CMake:
```bash
> cmake -DSYSTEM_EXPAT=ON ..
> make
```

### Building the [Python](https://www.python.org/) module of JSBSim

A Python module of JSBSim can also be built by CMake. For that, you need [Cython](http://cython.org/) installed on your platform. CMake will automatically detect Cython and build the Python module.

## Building with Microsoft Visual Studio

From Visual Studio, you can open the project file `JSBSim.vcxproj` to open a project for JSBSim. The project file will setup Visual Studio for building JSBSim executable.

**Note 1:** JSBSim official build tool is CMake. Visual studio project files are provided as a convenience and are not guaranteed to be up to date with the code.

**Note 2:** Since Visual Studio 2017, Microsoft has included CMake so you should be able to build JSBSim on VS2017 directly from the CMake file.

## Testing JSBSim

JSBSim comes with a test suite to automatically check that the build is correct. This test suite is located in the `tests` directory and is coded in Python so you need the [Python module for JSBSim to be built](Building the Python module of JSBSim).

The test suite can be run using `ctest` in the `build` directory. Tests can be run in parallel on several cores (4 in the example below) using the option `-j`
```bash
> ctest -j4
```

## Installing JSBSim

Once JSBSim is built and tested, you can install the C++ headers and library platform wide. For that, you can invoke GNU make from the `build` directory
```bash
> make install
```

## Installing the Python module

If you plan to install the Python module of JSBSim in addition to the C++ headers and library, then you must pass the flag `INSTALL_PYTHON_MODULE` to CMake
```bash
> cmake -DINSTALL_PYTHON_MODULE=ON ..
> make
> make install
```

Alternatively, the Python module can be installed manually by invoking the following commands from the `build` directory
```bash
> cd tests
> python setup.py install
```
---

<figure markdown>
  ![Placeholder image](../assets/img/ac_airspeeds_recap.svg){: .center width="80%" }
  <figcaption>
	So, you want to simulate the flight of this aircraft?
  </figcaption>
</figure>
