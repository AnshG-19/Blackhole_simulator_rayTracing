# Blackhole_simulator_rayTracing
# Black Hole Simulation: Light Ray Tracing

A Python-based black hole visualization and simulation project exploring light bending, Schwarzschild geometry, timelike particle orbits, gravitational lensing, and accretion-disk illustrations.

The project uses numerical methods and visualizations to explore how objects and light behave near a non-rotating Schwarzschild black hole.

## Project Objectives

- Calculate important Schwarzschild black hole radii.
- Numerically calculate light-ray trajectories near a black hole.
- Explore timelike geodesics and particle motion.
- Estimate gravitational light deflection.
- Visualize an illustrative accretion disk.
- Interactively explore how impact parameter affects light bending.
- Measure the computational cost of the light-ray solver.

## Physics Covered

For a black hole of mass \(M\), using geometric units \(G=c=1\):

| Quantity | Radius |
|---|---|
| Event horizon | \(2M\) |
| Photon sphere | \(3M\) |
| Innermost stable circular orbit (ISCO) | \(6M\) |
| Critical light-ray impact parameter | \(3\sqrt{3}M\) |

The light-ray solver numerically integrates an orbit equation in Schwarzschild spacetime. Escaping trajectories require an impact parameter greater than the critical value.

## Repository Structure

```text
Blackhole_simulator_rayTracing/
├── notebooks/
│   ├── 01_black_hole_geometry.ipynb
│   ├── 02_light_ray_trajectories.ipynb
│   ├── 03_schwarzschild_geodesics.ipynb
│   ├── 04_gravitational_lensing.ipynb
│   ├── 05_accretion_disk.ipynb
│   ├── 06_interactive_visualization.ipynb
│   └── 07_performance_experiments.ipynb
├── src/
│   └── physics/
│       ├── black_hole.py
│       └── ray_tracing.py
├── tests/
│   └── test_ray_tracing.py
└── README.md
```

## Notebook Guide

1. **Black Hole Geometry:** Calculate and visualize the event horizon and photon sphere.
2. **Light-Ray Trajectories:** Calculate and plot light paths near a black hole.
3. **Schwarzschild Geodesics:** Explore timelike particle trajectories and check energy conservation.
4. **Gravitational Lensing:** Compare numerical light deflection with a weak-field approximation.
5. **Accretion Disk:** Visualize an illustrative disk and orbital angular velocity.
6. **Interactive Visualization:** Explore how changing the impact parameter affects light-ray trajectories.
7. **Performance Experiments:** Measure solver execution time at different numerical resolutions.

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebooks / Google Colab
- pytest

## Running the Project

### Option 1: Google Colab

1. Open the repository on GitHub.
2. Open a notebook under `notebooks/`.
3. Open the notebook in Google Colab.
4. Run its cells from top to bottom.

Some notebooks require the repository to be cloned into the Colab runtime before importing modules from `src/`.

### Option 2: Run Locally

Clone the repository:

```bash
git clone https://github.com/AnshG-19/Blackhole_simulator_rayTracing.git
cd Blackhole_simulator_rayTracing
```

Install the dependencies:

```bash
python -m pip install numpy scipy matplotlib ipywidgets pytest jupyter
```

Run Jupyter:

```bash
python -m jupyter notebook
```

Open the notebooks in the `notebooks/` directory.

## Running Tests

From the repository root, run:

```bash
python -m pytest -q
```

The tests check important black hole calculations, input validation, and light-ray solver behavior.

## Scientific Scope and Limitations

This is an educational numerical simulation, not a full general-relativistic rendering engine.

- The black hole model uses Schwarzschild spacetime, which describes a non-rotating, uncharged black hole.
- The light-ray calculations use geometric units and a numerical orbit equation.
- The weak-field deflection formula is an approximation and is most appropriate when the impact parameter is large compared with the black hole mass.
- The accretion-disk image is illustrative, not a complete radiation-transfer simulation.
- Numerical trajectories and performance measurements depend on integration settings and computational conditions.

## Future Improvements

- Improve trajectory handling near the critical impact parameter.
- Add more robust numerical accuracy and convergence experiments.
- Improve physical consistency checks for timelike geodesics.
- Develop more realistic accretion-disk rendering.
- Build a web-based interface for exploring black hole physics.

## Author

**Ansh Gaur**

GitHub: [AnshG-19](https://github.com/AnshG-19)
