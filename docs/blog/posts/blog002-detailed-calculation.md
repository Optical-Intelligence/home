---
date:
  created: 2026-08-22
draft: False
---

# How Does a Space Mirror Light Up the Night? The Physics Behind the Simulation

## 1. Introduction

In my [previous article](https://optical-intelligence.github.io/home/blog/2026/08/16/how-many-space-mirrors-would-it-take-to-light-up-your-night), I used a Python simulation to investigate a simple but interesting question:

> **How many orbital mirrors are needed to illuminate Boston with an irradiance approximately equivalent to the Full Moon?**

The previous article focused on the **results**. I compared different dawn-dusk Sun-synchronous orbit (SSO) altitudes and showed how many mirrors could potentially reflect sunlight toward Boston.

But how did I actually calculate those numbers? This article goes one level deeper.

Here I will explain the physics and mathematics behind the simulation, starting with the orbital geometry and ending with the estimated irradiance on the ground.

The complete Python simulation used to generate the results is available on my **[Gumroad page](https://opticalpython.gumroad.com/l/mirror_sso)**. I have decided to keep the code separate from this article so that you can experiment with the simulation yourself.

The calculation can be divided into several major steps:

$$
\boxed{
\text{Sun}
\rightarrow
\text{Mirror}
\rightarrow
\text{Earth}
}
$$

First, I determine where the Sun and mirrors are located. Then I determine whether a particular mirror can see both the Sun and the target on Earth. If it can, I calculate the mirror orientation required for specular reflection, the effective area of the mirror illuminated by the Sun, the size of the reflected light spot on Earth, and finally the irradiance reaching the ground.

The goal is not to build a perfect optical or orbital model. Instead, I want to develop a reasonably simple physical model that captures the most important effects and allows us to understand which parameters dominate the final result.

---

## 2. Coordinate Systems

The first challenge is that the Sun, satellites, and locations on Earth are naturally described using different coordinate systems. If these coordinate systems are mixed incorrectly, even a mathematically correct calculation can produce a physically incorrect result.

For this simulation, we used Earth-Centered Inertial Coordinates and the location of the Sun, Mirrors or Target on Earth are all converted into this system.

An Earth-Centered Inertial coordinate system places the origin at the center of Earth while keeping the coordinate axes approximately fixed relative to distant stars. The important point is that this coordinate system does **not rotate with Earth**.

---

## 3. Dawn-Dusk Sun-Synchronous Orbit

The [first article](https://optical-intelligence.github.io/home/blog/2026/08/16/how-many-space-mirrors-would-it-take-to-light-up-your-night) showed that I selected a **dawn-dusk Sun-synchronous orbit** as the candidate orbit for the mirrors.

But why is this orbit attractive?

### 3.1 What Is a Sun-Synchronous Orbit?

![Dawn-dusk Sun-synchronous orbit](images/blog002_figure1.PNG)
*Figure 1 — Dawn-dusk Sun-synchronous orbit ([image credit](https://www.esa.int/ESA_Multimedia/Images/2018/07/The_SMOS_satellite_in_sun-synchronous_orbit))*

A Sun-synchronous orbit is an orbit whose orbital plane precesses around Earth at approximately the same rate that Earth moves around the Sun. The orbital plane therefore maintains approximately the same orientation relative to the Sun.

This behavior is produced primarily by Earth's oblateness. The Earth's equatorial bulge produces a gravitational perturbation commonly represented by the $J_2$ coefficient. This perturbation causes the satellite's orbital plane to slowly rotate.

For a near-circular orbit, the rate of change of the right ascension of the ascending node (RAAN) can be approximated by

$$
\boxed{
\dot{\Omega}
=
-\frac{3}{2}
J_2
\left(
\frac{R_E}{p}
\right)^2
n\cos i
}
$$

where:

- $J_2$ is Earth's second zonal harmonic coefficient;
- $R_E$ is Earth's equatorial radius;
- $p$ is the orbital semi-latus rectum;
- $n$ is the mean motion;
- $i$ is the orbital inclination.

For a circular orbit,

$$
p=a,
$$

where the semi-major axis is

$$
a=R_E+h,
$$

and $h$ is the orbital altitude.

The mean motion is

$$
n=
\sqrt{\frac{\mu}{a^3}},
$$

where $\mu$ is Earth's gravitational parameter.

For a Sun-synchronous orbit, the required nodal precession rate is approximately equal to Earth's mean orbital angular velocity around the Sun.

Therefore, the required inclination can be found from the above relationship.

Rearranging gives

$$
\boxed{
\cos i
=
-\frac{2}{3}
\frac{\dot{\Omega}}
{J_2n}
\left(
\frac{a}{R_E}
\right)^2
}
$$

and therefore

$$
\boxed{
i=
\cos^{-1}
\left[
-\frac{2}{3}
\frac{\dot{\Omega}}
{J_2n}
\left(
\frac{a}{R_E}
\right)^2
\right].
}
$$

This is why the required SSO inclination changes with orbital altitude.

### 3.2 What Is LTAN?

LTAN stands for **Local Time of the Ascending Node**.

It describes the local solar time when the satellite crosses the equator from south to north.

For example:

- LTAN = 06:00 corresponds approximately to dawn.
- LTAN = 12:00 corresponds approximately to local noon.
- LTAN = 18:00 corresponds approximately to dusk.

A dawn-dusk orbit therefore has an ascending-node local time close to

$$
\boxed{
\mathrm{LTAN}\approx06:00
}
$$

with the descending node occurring approximately at 18:00 local time.

### 3.3 Why Dawn-Dusk?

For our space mirror whose purpose is to collect sunlight, Earth's shadow is undesirable. A dawn-dusk Sun-synchronous orbit is designed to provide near-continuous sunlight exposure by keeping the orbital plane close to the day-night terminator. However, it is important not to interpret "dawn-dusk" as a guarantee that every satellite will always receive sunlight under every possible condition. The exact eclipse geometry depends on altitude, season, orbital orientation, and the relative positions of the Sun and Earth.

This makes the orbit attractive for our sunlight-reflection system. The important point is that a dawn-dusk SSO is a natural candidate when continuous access to sunlight is an important design objective.

---
## 4. Distributing the Mirrors Around the Orbit

Once the orbit altitude and inclination are determined, the mirrors can be distributed around the circular orbit.

The orbit radius is

$$
\boxed{
r_{\mathrm{orbit}}
=
R_E+h
}
$$

and the orbital circumference is

$$
\boxed{
C
=
2\pi r_{\mathrm{orbit}}.
}
$$

If adjacent mirrors are separated by approximately $s$ kilometers, the approximate number of mirrors is

$$
\boxed{
N
\approx
\frac{2\pi r_{\mathrm{orbit}}}{s}.
}
$$

For example, if the mirror spacing is

$$
s=100\ \mathrm{km},
$$

then

$$
N
\approx
\frac{2\pi(R_E+h)}
{100}.
$$

At an altitude of approximately $2100$ km, this gives roughly

$$
\boxed{
N\approx1064
}
$$

mirrors.

This number, however, is the number of mirrors that **can physically fit around the orbit** at the specified spacing.

It is not the number of mirrors that can illuminate Boston.

That distinction is extremely important.

---

## 5. Mirror Positions

For a circular orbit, each mirror can be represented by its position around the orbital plane.

Let $\nu$ represent the angular position of a mirror around the orbit.

In the orbital coordinate system, a circular orbit can be written as

$$
\mathbf{r}_{orbital}
=
\begin{bmatrix}
r\cos\nu\\
r\sin\nu\\
0
\end{bmatrix}.
$$

This vector is then rotated into the Earth-centered inertial coordinate system according to the orbital inclination and RAAN.

The mirrors are distributed by varying $\nu$ from

$$
0^\circ
$$

to

$$
360^\circ.
$$

For $N$ evenly distributed mirrors,

$$
\boxed{
\nu_k
=
\frac{2\pi k}{N},
\qquad
k=0,1,\ldots,N-1.
}
$$

This creates an evenly spaced constellation around the orbit.

---

## 6. Earth Visibility and Line of Sight

Knowing the position of a mirror is not enough. The mirror must satisfy two visibility conditions:

1. The mirror must be able to see the Sun.
2. The mirror must be able to see the target location on Earth.

If either path is blocked by Earth, that mirror contributes zero illumination.

The two paths are therefore:

$$
\boxed{
\text{Sun}\rightarrow\text{Mirror}
}
$$

and

$$
\boxed{
\text{Mirror}\rightarrow\text{Earth}
}
$$

---

### 6.1 Sun-to-Mirror Visibility

Consider the line segment connecting the Sun and the mirror.

Let $\mathbf{p}_0$ be the Sun position and $\mathbf{p}_1$ be the mirror position.

The line segment can be written as

$$
\boxed{
\mathbf{p}(t)
=
\mathbf{p}_0
+
t(\mathbf{p}_1-\mathbf{p}_0)
}
$$

where

$$
0\leq t\leq1.
$$

If this line intersects Earth, the mirror is inside Earth's shadow and cannot receive direct sunlight.

---

### 6.2 Mirror-to-Earth Visibility

The same geometric test is performed between the mirror and the target.

Let

$$
\mathbf{p}_0=\mathbf{r}_{\mathrm{mirror}}
$$

and

$$
\mathbf{p}_1=\mathbf{r}_{\mathrm{target}}.
$$

Then

$$
\mathbf{p}(t)
=
\mathbf{p}_0
+
t\mathbf{d},
$$

where

$$
\mathbf{d}
=
\mathbf{p}_1-\mathbf{p}_0.
$$

If this line segment intersects Earth before reaching the target, the reflected sunlight is blocked.

---

## 7. Line-Segment / Earth Intersection

For a spherical Earth, the Earth surface is described by

$$
|\mathbf{p}|=R_E.
$$

Substituting the line equation

$$
\mathbf{p}(t)
=
\mathbf{p}_0+t\mathbf{d}
$$

gives

$$
|\mathbf{p}_0+t\mathbf{d}|^2
=
R_E^2.
$$

Expanding this equation produces

$$
(\mathbf{d}\cdot\mathbf{d})t^2
+
2(\mathbf{p}_0\cdot\mathbf{d})t
+
(\mathbf{p}_0\cdot\mathbf{p}_0-R_E^2)
=
0.
$$

This is a quadratic equation of the form

$$
at^2+bt+c=0
$$

with

$$
a=\mathbf{d}\cdot\mathbf{d},
$$

$$
b=2\mathbf{p}_0\cdot\mathbf{d},
$$

and

$$
c=\mathbf{p}_0\cdot\mathbf{p}_0-R_E^2.
$$

The discriminant is

$$
\Delta=b^2-4ac.
$$

If

$$
\Delta<0,
$$

there is no intersection with the Earth.

If

$$
\Delta\geq0,
$$

the line intersects the Earth at one or two points.

The important question is whether an intersection occurs within the line segment:

$$
\boxed{
0\leq t\leq1.
}
$$

This provides a direct geometric test for Earth occlusion.

---

# 8. Sun-to-Mirror-to-Earth Reflection Geometry

![Sun-to-Mirror-to-Earth Reflection Geometry](images/blog002_figure2.PNG)

*Figure 2. Sun-to-Mirror-to-Earth Reflection Geometry.*

Now we reach the central optical calculation.

Suppose the mirror is located at

$$
\mathbf{r}_{\mathrm{mirror}}
$$

and the target on Earth is located at

$$
\mathbf{r}_{\mathrm{target}}
$$

The vector from the mirror toward the Sun is

$$
\boxed{
\mathbf{s}
=
\mathbf{r}_{Sun}
-
\mathbf{r}_{\mathrm{mirror}}
}
$$

with unit vector

$$
\boxed{
\hat{\mathbf{s}}
=
\frac{\mathbf{s}}
{|\mathbf{s}|}.
}
$$

The vector from the mirror toward the target is

$$
\boxed{
\mathbf{r}
=
\mathbf{r}_{\mathrm{target}}
-
\mathbf{r}_{\mathrm{mirror}}
}
$$

with unit vector

$$
\boxed{
\hat{\mathbf{r}}
=
\frac{\mathbf{r}}
{|\mathbf{r}|}.
}
$$

We now know the two directions required for the reflection:

- the direction toward the Sun;
- the desired direction toward the Earth target.

---

## 8.1 Required Mirror Normal

For an ideal flat mirror undergoing specular reflection, the surface normal bisects the angle between the incoming and outgoing directions.

Therefore, the required mirror normal is

$$
\boxed{
\hat{\mathbf{n}}
=
\frac{
\hat{\mathbf{s}}
+
\hat{\mathbf{r}}
}{
\left|
\hat{\mathbf{s}}
+
\hat{\mathbf{r}}
\right|
}.
}
$$

This is one of the most important equations in the simulation.

The incidence angle is then

$$
\boxed{
\theta_i
=
\cos^{-1}
\left(
\hat{\mathbf{n}}
\cdot
\hat{\mathbf{s}}
\right).
}
$$

For an ideal mirror,

$$
\theta_i=\theta_r.
$$

The mirror therefore redirects the sunlight from the Sun toward the selected point on Earth.

---

# 9. Mirror Area and Projected Area

Suppose each mirror is a square with side length $L$.

The physical mirror area is

$$
\boxed{
A_m=L^2.
}
$$

For an $18\ \mathrm{m}\times18\ \mathrm{m}$ mirror,

$$
A_m=18^2
$$

and therefore

$$
\boxed{
A_m=324\ \mathrm{m^2}.
}
$$

However, the full physical area of the mirror is not necessarily exposed to the full solar irradiance.

If $\theta_i$ is the angle between the mirror normal and the incoming sunlight direction, the projected area facing the Sun is

$$
\boxed{
A_{\mathrm{proj}}
=
A_m\cos\theta_i.
}
$$

Therefore, the incident solar power is approximately

$$
\boxed{
P_{\mathrm{incident}}
=
E_{\odot}
A_m
\cos\theta_i.
}
$$

where $E_{\odot} = 1361 W/m^2$ is the average solar irradiance hitting the top of Earth's atmosphere. 

When the mirror faces the Sun directly,

$$
\theta_i=0^\circ
$$

and

$$
A_{\mathrm{proj}}=A_m.
$$

As the mirror becomes more oblique to the sunlight,

$$
\cos\theta_i<1,
$$

and the effective collecting area decreases.

---

# 10. Reflected Optical Power

Let the mirror reflectivity be $\rho$.

The reflected optical power is approximately

$$
\boxed{
P_{\mathrm{reflected}}
=
\rho
E_{\odot}
A_m
\cos\theta_i.
}
$$

This assumes an ideal specular reflector with no additional optical losses.

A real mirror may have losses caused by:

- imperfect reflectivity;
- surface scattering;
- deformation;
- pointing error;
- contamination;
- thermal distortion.

These effects can be incorporated later using more sophisticated models.

---

# 11. The Finite Angular Size of the Sun

The sun light coming to Earth is not perfeclty parrellel and has an angular divergence of approximately

$$
\boxed{
\theta_{\odot}
\approx
0.53^\circ
}
$$

or, in radians,

$$
\boxed{
\theta_{\odot}
\approx
9.3\times10^{-3}\ \mathrm{rad}.
}
$$

This means the reflected sunlight from the flat mirror forms a finite illuminated region on Earth.

Let

$$
d
$$

be the distance between the mirror and the target.

For small angles, the approximate diameter of the illuminated spot is

$$
\boxed{
D_{\mathrm{spot}}
\approx
\theta_{\odot}d.
}
$$

For example, if

$$
d=2000\ \mathrm{km},
$$

then

$$
D_{\mathrm{spot}}
\approx
0.0093\times2000
$$

which gives approximately

$$
D_{\mathrm{spot}}
\approx18.6\ \mathrm{km}.
$$

The corresponding circular spot area is approximately

$$
\boxed{
A_{\mathrm{spot}}
=
\frac{\pi}{4}
D_{\mathrm{spot}}^2
}
$$

or

$$
\boxed{
A_{\mathrm{spot}}
=
\frac{\pi}{4}
\left(
\theta_{\odot}d
\right)^2.
}
$$

This relationship is extremely important because

$$
A_{\mathrm{spot}}\propto d^2.
$$

Therefore, as the mirror becomes farther from the target, the reflected sunlight is distributed over a larger area.

This is one of the reasons that increasing orbital altitude does not necessarily increase the illumination on Earth.

---

# 12. Ground Incidence Angle

The reflected light does not necessarily hit Earth's surface perpendicular to the ground.

At the target location, the outward surface normal can be represented by (Figure 2)

$$
\hat{\mathbf{n}}_g.
$$

The reflected sunlight travels from the mirror toward Earth, so its propagation direction is

$$
\hat{\mathbf{r}}.
$$

The direction from which the sunlight arrives at the surface is therefore

$$
-\hat{\mathbf{r}}.
$$

The ground incidence angle is determined from

$$
\boxed{
\cos\theta_g
=
\hat{\mathbf{n}}_g
\cdot
(-\hat{\mathbf{r}}).
}
$$

If

$$
\cos\theta_g\le0,
$$

the reflected ray is not arriving at the outward-facing surface.

Otherwise, the projected illumination is proportional to

$$
\boxed{
\cos\theta_g.
}
$$

Therefore, the same amount of reflected optical power can produce different ground irradiances depending on the angle at which the light reaches the surface.

---

# 13. Visible-Light Component

![Solar_spectrum](images/blog002_figure3.PNG)

*Figure 3. Solar spectrum.*

The sunlight arriving at the mirror contains a broad range of wavelengths.

For this study, I am primarily interested in the visible component.

As a first-order approximation, I use

$$
\boxed{
f_{\mathrm{visible}}\approx0.46
}
$$

for the fraction of solar power contained in the visible spectrum.

The visible reflected power is therefore approximately

$$
\boxed{
P_{\mathrm{visible}}
=
f_{\mathrm{visible}}
P_{\mathrm{reflected}}.
}
$$

This is an approximation rather than a detailed spectral calculation.

A more rigorous model would integrate the solar spectral irradiance over a defined wavelength range, such as approximately $400$–$700$ nm.

---

# 14. Atmospheric Attenuation

The reflected irradiance calculated above represents the illumination before accounting for atmospheric losses.

The atmosphere absorbs and scatters part of the incoming light.

For the initial model, I use a representative clear-sky transmission factor:

$$
\boxed{
T_{\mathrm{atm}}\approx0.80.
}
$$

Therefore,

$$
\boxed{
E_{\mathrm{ground}}
=
E_{\mathrm{TOA}}
T_{\mathrm{atm}}.
}
$$

This is intentionally a simplified approximation.

Actual atmospheric transmission depends on:

- wavelength;
- aerosols;
- water vapor;
- solar elevation;
- weather conditions.

Therefore, the atmospheric factor used here should be regarded as a representative clear-sky approximation rather than a universal value.

---

# 15. Final Ground-Irradiance Equation

We can now combine the optical and geometric calculations.

The incident solar power on the mirror is

$$
P_{\mathrm{incident}}
=
E_{\odot}
A_m
\cos\theta_i.
$$

The reflected power is

$$
P_{\mathrm{reflected}}
=
\rho
E_{\odot}
A_m
\cos\theta_i.
$$

The visible portion is

$$
P_{\mathrm{visible}}
=
f_{\mathrm{visible}}
\rho
E_{\odot}
A_m
\cos\theta_i.
$$

The reflected spot area is

$$
A_{\mathrm{spot}}
=
\frac{\pi}{4}
\left(
\theta_{\odot}d
\right)^2.
$$

Therefore, before accounting for the ground incidence angle and atmospheric attenuation,

$$
E_{\mathrm{TOA}}
=
\frac{
\rho
E_{\odot}
f_{\mathrm{visible}}
A_m
\cos\theta_i
}{
\frac{\pi}{4}
\left(
\theta_{\odot}d
\right)^2
}.
$$

Including the ground incidence angle,

$$
E_{\mathrm{TOA}}
=
\frac{
\rho
E_{\odot}
f_{\mathrm{visible}}
A_m
\cos\theta_i
\cos\theta_g
}{
\frac{\pi}{4}
\left(
\theta_{\odot}d
\right)^2
}.
$$

Finally, including atmospheric transmission,

$$
\boxed{
E_{\mathrm{ground}}
=
\frac{
\rho
E_{\odot}
f_{\mathrm{visible}}
A_m
\cos\theta_i
\cos\theta_g
T_{\mathrm{atm}}
}{
\frac{\pi}{4}
\left(
\theta_{\odot}d
\right)^2
}
}
$$

This is the main irradiance equation used in the simplified model.

---

# 16. What Each Term Means

The equation looks complicated, but every term has a straightforward physical meaning:

$$
E_{\mathrm{ground}}
=
\frac{
\rho
E_{\odot}
f_{\mathrm{visible}}
A_m
\cos\theta_i
\cos\theta_g
T_{\mathrm{atm}}
}{
\frac{\pi}{4}
\left(
\theta_{\odot}d
\right)^2
}.
$$

| Symbol | Meaning |
|---|---|
| $\rho$ | Mirror reflectivity |
| $E_{\odot}$ | Solar irradiance at the mirror |
| $f_{\mathrm{visible}}$ | Fraction of solar power in the visible spectrum |
| $A_m$ | Physical mirror area |
| $\cos\theta_i$ | Projected mirror area toward the Sun |
| $\cos\theta_g$ | Ground incidence-angle factor |
| $T_{\mathrm{atm}}$ | Atmospheric transmission |
| $\theta_{\odot}$ | Angular diameter of the Sun |
| $d$ | Mirror-to-target distance |

Several important scaling relationships are immediately visible.

For example,

$$
E_{\mathrm{ground}}\propto A_m.
$$

Therefore, doubling the mirror area approximately doubles the ground irradiance.

Similarly,

$$
E_{\mathrm{ground}}\propto\rho.
$$

However, because

$$
A_{\mathrm{spot}}\propto d^2,
$$

the ground irradiance approximately scales as

$$
E_{\mathrm{ground}}\propto\frac{1}{d^2}.
$$

This means that increasing the distance between the mirror and the target can significantly reduce the irradiance.

---

# 17. Why Orbital Altitude Matters

Orbital altitude affects several parts of the calculation simultaneously.

Increasing the altitude:

1. increases the distance between the mirror and Earth;
2. increases the portion of Earth visible from the mirror;
3. changes the required SSO inclination;
4. changes the Sun → Mirror → Earth reflection geometry;
5. changes the mirror-to-target distance;
6. changes the reflected spot size;
7. changes the number of mirrors that can fit into the orbit for a fixed spacing.

This creates a tradeoff.

At lower altitude, the target may not have line of sight to the part of the orbit required for reflection.

At higher altitude, the target can see a larger portion of the orbit, but the reflected light is spread over a larger area.

Therefore, the best orbital altitude cannot be determined from orbit visibility alone.

It requires evaluating the complete optical and geometric model.

---

# 18. Why Only Some Mirrors Contribute

This is one of the most important results of the simulation.

Suppose an orbit contains

$$
N=1064
$$

mirrors.

It does **not** mean that all 1064 mirrors illuminate Boston simultaneously.

A mirror must satisfy several conditions:

$$
\boxed{
\text{Sun visible}
}
$$

and

$$
\boxed{
\text{Target visible}
}
$$

and

$$
\boxed{
\text{Valid reflection geometry}
}
$$

and

$$
\boxed{
\cos\theta_i>0
}
$$

and

$$
\boxed{
\cos\theta_g>0.
}
$$

Only mirrors satisfying these conditions contribute to the final irradiance.

For the example discussed in the first article, an SSO at approximately 2100 km can accommodate about 1064 mirrors with 100 km spacing, but only about 169 mirrors contribute to the illumination of Boston at the selected simulation time.

That is approximately

$$
\boxed{
\frac{169}{1064}
\approx16\%
}
$$

of the total constellation.

This is why simply calculating the irradiance from one mirror and multiplying it by the total number of mirrors would give an incorrect result.

---

# 19. Comparing the Result with Full-Moon Illumination

Once the total reflected irradiance has been calculated, it can be compared with a reference full-Moon irradiance.

Define

$$
\boxed{
R_{\mathrm{Moon}}
=
\frac{
E_{\mathrm{mirror}}
}{
E_{\mathrm{Full\ Moon}}
}.
}
$$

If

$$
R_{\mathrm{Moon}}=1,
$$

the simulated illumination is approximately equivalent to the selected full-Moon reference.

If

$$
R_{\mathrm{Moon}}=0.01,
$$

the simulated illumination is approximately 1% of that reference.

This provides a more intuitive way to interpret the numerical result.

Instead of simply saying

$$
E=0.003\ \mathrm{W/m^2},
$$

we can say:

> The reflected illumination is approximately 0.01 times the irradiance of the Full Moon.

---

# 20. Limitations of the Model

The model described above is intentionally simplified.

It is designed to understand the dominant physical relationships rather than reproduce every detail of a real spacecraft system.

### 20.1 Spherical Earth

The line-of-sight calculation uses a spherical Earth approximation.

A more accurate model would use the WGS84 ellipsoid and potentially include terrain elevation.

### 20.2 Simplified Atmosphere

The atmosphere is represented using a single transmission factor.

A realistic calculation would account for:

- wavelength;
- aerosols;
- water vapor;
- elevation angle;
- weather conditions.

### 20.3 Ideal Mirror

The mirror is assumed to behave as an ideal specular reflector.

Real mirrors have:

- scattering;
- deformation;
- pointing errors;
- wavelength-dependent reflectivity.

### 20.4 Orbital Perturbations

The orbit model is based on a simplified circular SSO.

A real constellation would experience additional perturbations, including:

- atmospheric drag;
- solar radiation pressure;
- third-body gravitational effects;

### 20.5 Pointing Accuracy

The simulation assumes that the mirror can be oriented exactly toward the desired target.

A real spacecraft would have finite attitude-control accuracy.

Even a small pointing error could move the illuminated spot by many kilometers.

### 20.6 Seasonal Effects

The simulation represents a particular Sun-Earth geometry at a selected time.

The Sun's position changes throughout the year, which changes the orbital geometry and the illumination conditions.

A complete analysis should therefore examine different seasons rather than relying on a single simulation date.

---

# 21. What the Simulation Really Tells Us

The most important lesson from this calculation is that the problem is much more complicated than

$$
\text{mirror area}
\times
\text{sunlight}
=
\text{ground illumination}.
$$

The actual calculation is a chain of physical and geometric constraints:

$$
\boxed{
\begin{aligned}
\text{Orbit}
&\rightarrow
\text{Sun visibility}\\
&\rightarrow
\text{Earth visibility}\\
&\rightarrow
\text{Reflection geometry}\\
&\rightarrow
\text{Projected mirror area}\\
&\rightarrow
\text{Reflected power}\\
&\rightarrow
\text{Beam footprint}\\
&\rightarrow
\text{Ground incidence}\\
&\rightarrow
\text{Atmospheric transmission}
\end{aligned}
}
$$

Every step affects the final result.

This is also why changing the orbital altitude can produce surprisingly large changes in the final irradiance.

---

# 22. Conclusion

The goal of this simulation was not simply to calculate how much sunlight an 18-meter mirror can reflect.

The more interesting question is:

> **How much of that reflected sunlight can actually reach a specific location on Earth?**

The answer depends on much more than mirror size.

The most important parameters are:

- **orbit altitude**
- **SSO inclination**
- **RAAN and LTAN**
- **Sun position**
- **Earth visibility**
- **mirror-to-target distance**
- **mirror projected area**
- **reflection angle**
- **reflected beam size**
- **ground incidence angle**
- **atmospheric attenuation**
- **number and distribution of mirrors**

Most importantly:

$$
\boxed{
\text{Not every mirror contributes.}
}
$$

Even if an orbit contains more than one thousand mirrors, only a fraction may have the correct geometry to illuminate a particular location at a particular time.

That is what makes this problem interesting from both an orbital-mechanics and optical-engineering perspective.

If you would like to reproduce the calculations, experiment with different orbital altitudes, mirror sizes, target locations, and constellation sizes, the complete Python simulation is available on my **[Gumroad page](https://opticalpython.gumroad.com/l/mirror_sso)**.

In future articles, I plan to extend this model beyond a single point in Boston and investigate how the illumination changes across **different cities, different seasons, and potentially the entire nighttime side of Earth**.