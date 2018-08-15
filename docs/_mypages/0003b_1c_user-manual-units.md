---
layout: default
title: User Manual - Units
categories: [menu, content, user-manual, units]
permalink: /mypages/user-manual-units/
---

# Units

JSBSim uses English units for internal calculations almost exclusively. However, it is possible to input some parameters in the configuration file using different units. In fact, to avoid confusion, it is recommended that the unit always be specified. Units are specified using the `unit` attribute. For instance, the specification for the wingspan looks like this:

```xml
<wingspan unit="FT"> 35.8 </wingspan>
```

The above statement specifies a wingspan of 35.8 feet. The following statement specifying the wingspan in meters would result in the wingspan being converted to 35.8 feet as it was read in:

```xml
<wingspan unit="M"> 10.91 </wingspan>
```

The two statements for wingspan are effectively equivalent.

The following units are currently supported in JSBSim:

**Length**

| `unit=`  | unit   |
| ---:     | :---   |
| `FT`     | ft     |
| `IN`     | in     |
| `M`      | m      |
| `KM`     | km     |

**Area**

| `unit=`  | unit   |
| ---:     | :---   |
| `M2`     | m²     |
| `FT2`    | ft²    |

**Volume**

| `unit=`  | unit   |
| ---:     | :---   |
| `FT3`    | ft³    |
| `CC`     | cm³    |
| `M3`     | m³     |
| `LTR`    | l      |

**Mass and Weight**

| `unit=`  | unit   |
| ---:     | :---   |
| `LBS`    | lbm    |
| `KG`     | kg     |

**Moments of Inertia**

| `unit=`    | unit   |
| ---:       | :---   |
| `SLUG*FT2` | slug ft² |
| `KG*M2`    | kg m²  |

**Angles**

| `unit=`    | unit   |
| ---:       | :---   |
| `RAD`      | rad    |
| `DEG`      | deg    |

**Spring Force**

| `unit=`    | unit   |
| ---:       | :---   |
| `N/M`      | N/m    |
| `LBS/FT`   | lb/ft  |

**Damping Force**

| `unit=`    | unit   |
| ---:       | :---   |
| `N/M/SEC`  | N/(m s) |
| `LBS/FT/SEC` | lb/(ft s) |

**Power**

| `unit=`    | unit   |
| ---:       | :---   |
| `WATTS`    | W      |
| `HP`       | Hp     |

**Force**

| `unit=`    | unit   |
| ---:       | :---   |
| `LBS`      | lb     |
| `N `       | N      |

**Velocity**

| `unit=`    | unit   |
| ---:       | :---   |
| `KTS`      | kts    |
| `FT/SEC`   | ft/s   |
| `M/S`      | m/s    |

**Torque**

| `unit=`    | unit   |
| ---:       | :---   |
| `N*M`      | N m    |
| `FT*LBS`   | lb ft  |

**Pressure**

| `unit=`    | unit   |
| ---:       | :---   |
| `PSF`      | lb/ft² |
| `PSI`      | lb/in² |
| `ATM`      | atm    |
| `PA`       | N/m²   |
| `INHG`     | in HG  |
