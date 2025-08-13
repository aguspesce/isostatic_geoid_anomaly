# Isostatic Geoid Anomaly Calculation

## Geoid Anomaly from Airy Isostatic Compensation

The geoid anomaly caused by isostatic compensation is expressed as:

$$
\Delta N = -\frac{2\pi G}{g_r} \int_{-\infty}^{z_c} z \Delta \rho(z) dz
$$

where $\Delta N$ is the geoid anomaly, $G$ is the gravitational constant, $g_r$ is
gravity on the reference geoid, $z$ is depth (positive downward), $\Delta \rho(z)$ is
the lateral density difference, and $z_c$ is the compensation depth.

In the Airy model, the crust has a constant density $\rho_c$, and topography $h$ is
supported by a root of thickness $b$, where:

$$
b = \frac{\rho_c h}{\rho_m - \rho_c}
$$

where $\rho_m$ is the mantle density.
Substituting into the geoid anomaly formula gives:

$$
\Delta N = -\frac{2 \pi G}{g_r} \left[
  \int_{-h}^{0} \rho_c z dz +
  \int_{0}^{H} (\rho_c - \rho_c) \cdot z dz +
  \int_{H}^{H+b} (\rho_c - \rho_m) z dz
\right]
$$

which simplifies to

$$
\Delta N = \frac{\pi G \rho_c}{g_r} \left[
  2 H h + \frac{\rho_m h^2}{\rho_m - \rho_c}
\right]
$$

## Geoid Anomaly from Tesseroid Modeling

The geoid anomaly can also be computed by modeling the gravitational potential of the topography and the isostatic root using tesseroids:

$$
\Delta N = -\frac{2\pi G}{g_r} \int_{-\infty}^{z_c} z \Delta \rho(z) dz = \frac{T_{topo} + T_{root}}{g_r}
$$

where $T_{\text{topo}}$ is the gravitational potential from the topographic mass,
$T_{\text{root}}$ is the gravitational potential from the crustal root, and $g_r$ is
the reference gravity.

## How to Run the Notebooks

You'll need a few things installed on your computer to be able to run the content in
this repository:

- A working Python installation (([Anaconda](https://www.anaconda.com/) o Miniconda)).
- The conda environment installed (conda environment).
- A web browser that works with Jupyter.

### Step 1: Install a Python Distribution

If you already have Anaconda or Miniconda installed, you can skip this step.
Otherwise, follow the instructions on the Anaconda website.

If you need more help installing Anaconda, you can watch this video tutorial from
[Software Carpentry](https://carpentries.github.io/workshop-template/#python).

### Step 2: Create the Conda Environment

All necessary dependencies can be installed through the `conda` package manager.
The file called `environment.yml` contains all the dependencies that the manager needs
to install.
To do this, run:

```
conda env create -f environment.yml
```

Then activate the environment:

```
conda activate geoid
```

### Step 3: Launch JupyterLab

Once the environment is activated, launch the JupyterLab server:

```
jupyter lab
```

Jupyter should open in your default web browser.
If you need more help running JupyterLab, you can watch this lesson from
[Software Carpentry](https://swcarpentry.github.io/python-novice-gapminder/01-run-quit/index.html).

## Dependencies

- numpy
- scipy
- boule
- harmonica
- matplotlib
- pandas
- verde

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
