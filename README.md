# 2D Heat Conduction Simulation

This Python script simulates the two-dimensional heat conduction on a square plate using the explicit finite difference method. It visualizes the temperature distribution evolving over time.

## Description

The script initializes a 2D grid representing a plate with an initial uniform temperature. It then applies fixed temperature boundary conditions to three specific rows/edges of the plate. The simulation iteratively calculates the temperature at each internal grid point based on its neighbors and the thermal diffusivity of the material, updating a plot at each time step to show the heat distribution.

## Requirements

To run this script, you will need Python 3 and the following libraries:

* **NumPy**: For numerical operations, especially array manipulation.
* **Matplotlib**: For plotting the temperature distribution.

## Installation

If you don't have these libraries installed, you can install them using pip:

```bash
pip install numpy matplotlib
