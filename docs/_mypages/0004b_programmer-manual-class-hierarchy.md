---
layout: default
title: Class hierarchy
parent: Programmer Manual
nav_order: 200
categories: [menu, content, programmer-manual, programmer-manual-class-hierarchy]
permalink: /mypages/programmer-manual-class-hierarchy/
---

# Class Hierarchy

TBD

```cpp
fdmex = new FGFDMExec( /* ... */ ); // (1) Instantiation
result = fdmex->LoadModel( /* ... */ ); // (2) Model loading
```

{% include image.html
  url="/assets/img/Class_Diagram_FGJSBBase.png"
  width="95%"
  description="Class diagram of class FGJSBBase."
  %}

{% include image.html
  url="/assets/img/Call_Diagram_FGFDMExec_Initialize.png"
  width="95%"
  description="Call graph of the function FGFDMExec::Initialize."
  %}
