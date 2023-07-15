---
title: Programmer Manual
description: JSBSim Programmer Manual home page.
---

# Programmer manual

One of the specific goals of the design of JSBSim is to make sure it is relatively easy to incorporate into a small or large simulation program. As often happens with simulation programs (and software applications in general) "feature creep" sets in and the program code blossoms into a larger-than-intended product. In the case of JSBSim, we have attempted to maintain the code base as small as possible, but at first glance it can still be overwhelming.

Unlike some simulator applications, JSBSim (at the time of this writing) has no external dependencies. That is, *all* code that is needed to build JSBSim is packaged along with it. This greatly simplifies the building of the JSBSim executable. There is also no automatically generated code within JSBSim. All code is straight C++ (with some C code from the included eXpat XML parsing code).

!!! info ""

	No proprietary program code is included in JSBSim distribution. All code coming with JSBSim has been developed on a volunteer basis using publicly available information, and is often directly referenced to a particular textbook, for educational purposes. In some cases, code of a generic nature has been donated back to the project.
