---
layout: default
title: Class hierarchy
parent: Programmer Manual
nav_order: 200
categories: [menu, content, programmer-manual, programmer-manual-class-hierarchy]
permalink: /mypages/programmer-manual-class-hierarchy/
---

# Class Hierarchy

!!! note "TODO"

    Complete page content.


```cpp
fdmex = new FGFDMExec( /* ... */ ); // (1) Instantiation
result = fdmex->LoadModel( /* ... */ ); // (2) Model loading
```
<figure markdown>
  ![FGJSBBase Diagram](/assets/img/Class_Diagram_FGJSBBase.png){: .center width="95%" }
  <figcaption>
    Class diagram of class FGJSBBase.
  </figcaption>
</figure>

<figure markdown>
  ![FGJSBBase Diagram](/assets/img/Call_Diagram_FGFDMExec_Initialize.png){: .center width="95%" }
  <figcaption>
    Call graph of the function FGFDMExec::Initialize.
  </figcaption>
</figure>

