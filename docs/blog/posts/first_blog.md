---
date:
  created: 2026-08-08
draft: true
---

# Can Satellites Reflect Sunlight Back to Earth?

## 1. Introduction

What if we could turn sunlight back on after sunset?

The basic idea is:

$$
\text{Sun} \rightarrow \text{Orbital Mirror} \rightarrow \text{Earth}
$$

A large reflective surface in space can intercept sunlight and redirect it toward a selected location on the night side of Earth. Unlike conventional artificial lighting, the energy source is the Sun itself.

This idea is not new. The Soviet/Russian **Znamya** experiments demonstrated that an orbital reflector could redirect sunlight toward the nighttime Earth.

Today, the concept is being revisited by **Reflect Orbital**, which is developing satellites intended to redirect sunlight toward selected locations on Earth.

The interesting question is:

> **Does the physics actually work as expected, and what kind of orbital system would be required to make it practical?**

This article uses Python and the Skyfield astronomy library to investigate the orbital geometry, sunlight reflection, Earth visibility, and resulting ground illumination.

---

## 2. A Brief History of Space Mirrors

The idea of using mirrors in space to redirect sunlight has been considered for decades.

The most important practical demonstration came from the Soviet/Russian **Znamya** program.

### 2.1 Znamya-2

The first major orbital experiment, **Znamya-2**, used a large aluminized reflective membrane. It was deployed from the Mir space station in February 1993.

The approximately 20-meter reflector successfully redirected sunlight toward the nighttime surface of Earth, demonstrating that the fundamental concept was physically possible.

$$
\boxed{\text{Sunlight can be reflected from orbit onto the nighttime Earth.}}
$$

### 2.2 Znamya-2.5

A larger follow-up experiment, **Znamya-2.5**, was attempted in 1999. The planned reflector was approximately 25 meters across, but the reflector became caught on an antenna during deployment and the experiment failed.

The Znamya program therefore demonstrated both the potential and the engineering difficulty of very large lightweight orbital reflectors.

---

## 3. Reflect Orbital

More than two decades later, the concept has returned in a commercial form.

Reflect Orbital is developing satellites designed to redirect sunlight toward selected locations on Earth. The company describes the concept as a controllable sunlight service.

Potential applications include:

- extending solar-energy production after sunset,
- emergency response,
- remote industrial operations,
- agriculture,
- nighttime illumination.

The company has described a roadmap that progresses from demonstration satellites toward a much larger constellation. These are company roadmap targets, not demonstrated operational capabilities.

This raises an important engineering question:

> **How large does the orbital system actually need to be to produce useful illumination on Earth?**

That is what this simulation investigates.

---

## 4. What Is This Simulation Trying to Determine?

The goal is to use physics and numerical simulation to independently investigate the feasibility of orbital sunlight reflection.

The main questions are:

1. What orbit is most suitable for space-based sunlight-reflecting mirrors?
2. Is a dawn-dusk Sun-synchronous orbit a good choice?
3. What altitude is required to illuminate a particular city?
4. How many mirrors can be distributed around such an orbit?
5. How much visible light can reach the ground?
6. How does the resulting illumination compare with the full Moon?

The simulation uses:

- Python
- Skyfield
- NumPy
- Matplotlib

Skyfield provides astronomical positions and coordinate transformations, while the simulation calculates orbital geometry, reflection geometry, Earth occlusion, optical power, and ground irradiance.

---

## 5. Why Consider a Dawn-Dusk Sun-Synchronous Orbit?

A conventional low-Earth orbit periodically passes through Earth's shadow. For a mirror whose purpose is to reflect sunlight, this is undesirable because the mirror cannot reflect sunlight when it is itself in darkness.

A **Sun-synchronous orbit (SSO)** maintains a nearly constant relationship between the orbital plane and the Sun.

A particularly interesting configuration is a **dawn-dusk SSO**, in which the orbital plane is approximately aligned with the day-night terminator.

This makes a dawn-dusk orbit an attractive candidate because the mirrors can have favorable access to sunlight.

However, dawn-dusk SSO does not automatically mean "best orbit." The mirror also needs to:

- remain illuminated by the Sun,
- see the desired location on Earth,
- have sufficient optical power,
- be close enough to Earth to produce a useful spot,
- have an appropriate orbital period,
- provide useful geographic coverage.

There is therefore a tradeoff between sunlight availability, ground coverage, and optical intensity.

---

## 6. Orbital Altitude and Earth Coverage

Consider a satellite at altitude $h$ above a spherical Earth of radius $R_E$.

The maximum Earth central angle between the satellite's subpoint and its horizon point is:

$$
\boxed{
\psi_\mathrm{max}
=
\cos^{-1}
\left(
\frac{R_E}{R_E+h}
\right)
}
$$

This is the **Earth central angle**. It should not be confused with the angle measured at the satellite.

As altitude increases:

- the satellite can see a larger fraction of Earth,
- the mirror-to-ground distance increases,
- the reflected spot becomes larger,
- the irradiance density decreases.

This creates an important altitude tradeoff.

---

# 7. Simulation Part I — Quick Results

The actual numerical results and figures will be inserted after the simulation is finalized.

## 7.1 Selected Location

- City: `[CITY]`
- Latitude: `[LATITUDE]`
- Longitude: `[LONGITUDE]`

## 7.2 Orbital Configuration

- Orbit type: Dawn-dusk SSO
- Altitude: `[ALTITUDE] km`
- Number of mirrors: `[NUMBER]`
- Mirror size: `[MIRROR SIZE] m × [MIRROR SIZE] m`
- Mirror area: `[AREA] m²`
- Reflectivity: `[REFLECTIVITY]`

## 7.3 Simulation Result

[INSERT FIGURE: Orbit and mirror geometry]

**Number of mirrors capable of illuminating the target:**

$$
\boxed{[NUMBER]}
$$

**Total visible irradiance at the ground:**

$$
\boxed{[IRRADIANCE]\ \mathrm{W/m^2}}
$$

**Equivalent full-Moon illumination:**

$$
\boxed{[RATIO]\times\text{full Moon}}
$$

[INSERT FIGURE: Close-up showing illuminating mirrors and target]

---

# 8. Detailed Physical Model

The complete optical path is:

$$
\boxed{
\text{Sun} \rightarrow \text{Mirror} \rightarrow \text{Earth}
}
$$

For every mirror, the simulation determines whether this path is geometrically possible.

## 8.1 Sun Position

The Sun's position is obtained from Skyfield using a JPL planetary ephemeris.

The Sun-to-mirror vector is:

$$
\mathbf{s}
=
\mathbf{r}_{Sun}
-
\mathbf{r}_{mirror}
$$

and the Sun-mirror distance is:

$$
d_{Sun}=|\mathbf{s}|.
$$

The unit vector pointing from the mirror toward the Sun is:

$$
\hat{\mathbf{s}}
=
\frac{\mathbf{s}}{|\mathbf{s}|}.
$$

The simulation uses the actual Sun position rather than assuming an infinitely distant Sun.

## 8.2 Mirror Area and Projected Area

For a square mirror with side length $L$:

$$
\boxed{A_m=L^2}
$$

If the angle between the mirror normal and the incoming sunlight direction is $\theta_i$, the effective illuminated area is:

$$
\boxed{
A_\mathrm{projected}
=
A_m\cos\theta_i
}
$$

The incident optical power is:

$$
P_\mathrm{incident}
=
E_\odot A_m\cos\theta_i.
$$

With mirror reflectivity $\rho$:

$$
\boxed{
P_\mathrm{reflected}
=
\rho E_\odot A_m\cos\theta_i
}
$$

## 8.3 Specular Reflection

Define $\hat{\mathbf{s}}$ as the unit vector from the mirror toward the Sun and $\hat{\mathbf{r}}$ as the desired reflected direction toward the Earth target.

For ideal specular reflection:

$$
\boxed{
\hat{\mathbf{n}}
=
\frac{
\hat{\mathbf{s}}+\hat{\mathbf{r}}
}{
|\hat{\mathbf{s}}+\hat{\mathbf{r}}|
}
}
$$

The reflected vector is:

$$
\boxed{
\hat{\mathbf{r}}_\mathrm{reflected}
=
2(\hat{\mathbf{s}}\cdot\hat{\mathbf{n}})
\hat{\mathbf{n}}
-
\hat{\mathbf{s}}
}
$$

The simulation checks that the resulting reflected direction points toward the desired Earth target.

## 8.4 Sun → Mirror Visibility

A mirror cannot reflect sunlight if Earth blocks the Sun.

The simulation checks the line segment:

$$
\text{Sun}\rightarrow\text{Mirror}.
$$

The line is:

$$
\mathbf{p}(t)=\mathbf{p}_0+t\mathbf{d},
\qquad 0\le t\le1.
$$

If the segment intersects the spherical Earth, that mirror contributes zero illumination.

## 8.5 Mirror → Earth Visibility

The second visibility test is:

$$
\text{Mirror}\rightarrow\text{Target}.
$$

If Earth blocks this path, the mirror cannot illuminate the target.

Thus:

$$
\boxed{
\text{Sun visible}
\quad\text{AND}\quad
\text{Target visible}
}
$$

are both required.

## 8.6 Reflected Beam Footprint

The Sun has a finite angular diameter of approximately:

$$
\boxed{\theta_\odot\approx9.3\ \mathrm{mrad}}
$$

For mirror-to-ground distance $d$, the first-order spot diameter is:

$$
\boxed{
D_\mathrm{spot}\approx\theta_\odot d
}
$$

and:

$$
\boxed{
A_\mathrm{spot}
=
\frac{\pi}{4}D_\mathrm{spot}^2
}
$$

or:

$$
A_\mathrm{spot}
=
\frac{\pi}{4}(\theta_\odot d)^2.
$$

Because:

$$
A_\mathrm{spot}\propto d^2,
$$

higher altitude generally produces a larger spot and lower irradiance density.

## 8.7 Ground Incidence Angle

Let $\hat{\mathbf{n}}_g$ be the outward normal of the Earth's surface at the target and $\hat{\mathbf{r}}$ the direction of reflected light from mirror to Earth.

The incoming direction at the surface is $-\hat{\mathbf{r}}$.

Therefore:

$$
\cos\theta_g
=
\hat{\mathbf{n}}_g\cdot(-\hat{\mathbf{r}})
$$

and:

$$
E_{\mathrm{ground,TOA}}
=
\frac{P_\mathrm{visible}}{A_\mathrm{spot}}
\cos\theta_g.
$$

If $\cos\theta_g\le0$, the reflected ray does not illuminate the outward-facing surface.

## 8.8 Visible-Light Fraction

For this first-order model, use approximately:

$$
\boxed{f_\mathrm{visible}\approx0.46}
$$

for the fraction of solar power in the approximately 400–700 nm visible range.

Thus:

$$
\boxed{
P_\mathrm{visible}
=
f_\mathrm{visible}P_\mathrm{reflected}
}
$$

The exact value depends on the spectral definition and solar spectrum used.

## 8.9 Atmospheric Attenuation

The irradiance above the atmosphere is higher than the irradiance at the ground.

Introduce an atmospheric transmission factor:

$$
T_\mathrm{atm}.
$$

Then:

$$
\boxed{
E_\mathrm{ground}
=
E_\mathrm{ground,TOA}T_\mathrm{atm}
}
$$

For the initial simplified clear-sky model:

$$
\boxed{T_\mathrm{atm}=0.80}
$$

is used as an approximate visible-light transmission factor.

Actual transmission depends on:

- elevation angle,
- wavelength,
- aerosols,
- water vapor,
- ozone,
- atmospheric pressure,
- local weather.

A future version can replace this constant with an air-mass and wavelength-dependent model.

## 8.10 Complete Ground-Irradiance Equation

Combining the optical and geometric terms:

$$
\boxed{
E_\mathrm{ground}
=
\frac{
\rho
E_\odot
f_\mathrm{visible}
A_m
\cos\theta_i
\cos\theta_g
T_\mathrm{atm}
}{
\frac{\pi}{4}(\theta_\odot d)^2
}
}
$$

This shows the important scaling relationships:

$$
E_\mathrm{ground}\propto A_m
$$

$$
E_\mathrm{ground}\propto\rho
$$

and approximately:

$$
E_\mathrm{ground}\propto\frac{1}{d^2}.
$$

---

# 9. Total Illumination from Multiple Mirrors

For mirror $i$:

$$
E_i=
\begin{cases}
\text{calculated irradiance}, & \text{if mirror can illuminate target}\\
0, & \text{otherwise}
\end{cases}
$$

The total ground irradiance is:

$$
\boxed{
E_\mathrm{total}
=
\sum_{i=1}^{N}E_i
}
$$

The simulation separates mirrors into:

- mirrors capable of illuminating the selected location,
- mirrors that cannot.

In the visualization:

- **yellow dots** represent mirrors capable of illuminating the target,
- **black dots** represent mirrors that cannot.

---

# 10. How Many Mirrors Can the Orbit Hold?

If mirrors are distributed around an orbit, their approximate along-track separation is:

$$
s=\frac{2\pi r_\mathrm{orbit}}{N}
$$

where:

$$
r_\mathrm{orbit}=R_E+h.
$$

Thus:

$$
\boxed{
N\approx\frac{2\pi(R_E+h)}{s}
}
$$

The actual number of satellites would also depend on collision avoidance, deployment, station keeping, communications, constellation phasing, and required coverage.

The simulation therefore treats the number of mirrors as a configurable parameter:

```python
N_MIRRORS = 10
```

which can be changed to 100, 1000, or more.

---

# 11. Comparison with Full-Moon Illumination

Define:

$$
\boxed{
R_\mathrm{Moon}
=
\frac{
E_\mathrm{reflected}
}{
E_\mathrm{full\,Moon}
}
$$

The interpretation is:

$$
R_\mathrm{Moon}=1
$$

approximately full-Moon illumination,

$$
R_\mathrm{Moon}>1
$$

brighter than the full Moon, and

$$
R_\mathrm{Moon}<1
$$

dimmer than the full Moon.

Final result:

$$
\boxed{
[INSERT\ RESULT]\times\text{full Moon}
}
$$

[INSERT FIGURE: Comparison with full-Moon illumination]

---

# 12. Simulation Results

## Target

- Location: `[CITY]`
- Latitude: `[LATITUDE]`
- Longitude: `[LONGITUDE]`

## Orbit

- Orbit: Dawn-Dusk SSO
- Altitude: `[ALTITUDE] km`
- Number of mirrors: `[NUMBER]`

## Mirror

- Size: `[SIZE] m × [SIZE] m`
- Area: `[AREA] m²`
- Reflectivity: `[REFLECTIVITY]`

## Illumination

**Number of mirrors illuminating target:**

$$
\boxed{[NUMBER]}
$$

**Total visible irradiance:**

$$
\boxed{[VALUE]\ \mathrm{W/m^2}}
$$

**Equivalent full-Moon illumination:**

$$
\boxed{[VALUE]\times\text{full Moon}}
$$

[INSERT FIGURE: Simulation result]

[INSERT FIGURE: Close-up orbital geometry]

---

# 13. Limitations of the Model

This simulation is intentionally a first-order physical model.

### Earth model

The initial simulation treats Earth as a sphere rather than using the WGS84 ellipsoid and terrain elevation.

### Atmospheric model

A constant clear-sky transmission factor is used rather than a full radiative-transfer model.

### Solar spectrum

The visible fraction is approximated rather than calculated wavelength by wavelength.

### Solar disk

The approximately 9.3 mrad solar angular diameter is used to estimate the reflected spot size.

### Mirror

The mirror is assumed to be an ideal specular reflector with a specified reflectivity.

Real mirrors will have surface imperfections, wrinkles, pointing errors, deformation, and nonuniform reflectivity.

### Diffraction

Diffraction and the detailed optical point-spread function are not included.

### Clouds

Clouds are not included. Cloud cover can dominate atmospheric attenuation.

### Atmospheric scattering

The initial model does not explicitly calculate scattered sunlight or sky glow.

### Orbital perturbations

The initial constellation model uses simplified circular orbital geometry rather than a complete long-term perturbation model.

The purpose of this first simulation is to answer:

> **Is the basic orbital and optical concept physically capable of producing useful illumination at Earth's surface?**

---

# 14. Python Simulation

The complete simulation is written in Python.

The primary libraries are:

- **Skyfield** — astronomical positions and coordinate transformations
- **NumPy** — vector and numerical calculations
- **Matplotlib** — three-dimensional visualization

The simulation allows parameters such as the following to be changed:

```python
N_MIRRORS = 10
ORBIT_ALTITUDE_KM = 600
MIRROR_AREA_M2 = ...
MIRROR_REFLECTIVITY = ...
```

The program determines which mirrors can illuminate a selected Earth location and calculates the resulting total visible irradiance.

The simulation also provides a three-dimensional visualization showing:

- Earth,
- orbital mirrors,
- selected ground target,
- Sun-to-mirror geometry,
- reflected-light paths,
- Earth coordinate axes,
- equatorial plane,
- zero-degree longitude plane.

## Get the Python Simulation

The complete Python simulation will be available here:

**[INSERT GUMROAD LINK]**

---

# 15. Future Work

Several extensions are possible.

## More Mirrors

The simulation can be extended from:

$$
N=10
$$

to:

$$
N=100,\quad1000,\quad5000
$$

or more.

## Global Illumination Map

A grid of latitude and longitude points can be evaluated to produce:

$$
E(\mathrm{latitude},\mathrm{longitude})
$$

and a global illumination map.

## Time-Dependent Simulation

The simulation can evaluate the illumination continuously as the satellites orbit Earth, showing:

- when a city becomes visible,
- how long it can be illuminated,
- which satellites contribute,
- how illumination changes with time.

## Improved Atmospheric Model

A future version could calculate:

$$
T_\mathrm{atm}=T(\lambda,\mathrm{airmass})
$$

rather than using a single constant transmission value.

## Realistic Earth Model

The spherical Earth could be replaced with:

- WGS84 Earth,
- terrain elevation,
- geographic maps,
- atmospheric models,
- cloud data.

## Optical Model

A more advanced model could include:

- mirror deformation,
- pointing errors,
- diffraction,
- finite mirror aperture,
- nonuniform reflectivity,
- solar spectral distribution.

---

# 16. Conclusion

The idea of reflecting sunlight from orbit is not science fiction. The Znamya experiments demonstrated that a large orbital reflector can redirect sunlight toward the nighttime Earth.

The modern version is more ambitious. Instead of a single experimental reflector, Reflect Orbital is pursuing a controllable satellite constellation intended to provide sunlight on demand.

But the important question is not simply whether a mirror can reflect sunlight.

It can.

The more interesting engineering questions are:

> **Where should the mirrors orbit?**

> **How many mirrors are required?**

> **How large should each mirror be?**

> **How much visible light can actually reach the ground?**

> **How does orbital altitude affect the illuminated area?**

> **Can the resulting illumination become comparable to natural moonlight or even daylight?**

A dawn-dusk Sun-synchronous orbit is an especially interesting candidate because it can provide favorable access to sunlight while the satellites move around Earth. But the final answer depends on orbital geometry, target location, mirror size, constellation size, reflection geometry, and atmospheric transmission.

The Python simulation developed in this article provides a way to investigate these questions quantitatively rather than relying only on conceptual diagrams.

The next step is therefore not to ask whether orbital sunlight reflection is possible.

The question is:

$$
\boxed{
\text{How much useful sunlight can we actually deliver to Earth?}
}
$$
