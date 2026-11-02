# Vectorized Epidemiological Simulator

A computational simulator for modeling disease spread in two-dimensional environments, developed with Python and NumPy.

The project aims to model how an infection spreads across space and evolves over time, exploring vectorized operations, cellular automata, and dynamic system modeling.

The goal is to progressively build a model capable of representing different disease transmission scenarios, visualizing epidemic progression, and investigating how spatial factors and transmission rules influence the spread of infection.

## Project Overview

The environment is initially represented as a two-dimensional grid, where each cell corresponds to a position in the simulated area. The infection starts in an initial cell, known as the index case or patient zero, and spreads to neighboring cells according to the rules defined by the model.

At each iteration, the simulator updates the state of the cells, allowing the expansion of the infected region to be tracked over time.

The implementation starts with a simple deterministic model and will gradually incorporate more sophisticated epidemiological rules and environmental scenarios.

## Planned Features

- **Spatial infection propagation:** Model the spread of infection between neighboring cells in a two-dimensional grid.
- **Temporal evolution:** Run multiple iterations and observe how the infected region expands over time.
- **Infection visualization:** Transform matrices into visual representations and develop an animation to track the progression of infection.
- **Transmission scenarios:** Investigate how alternative rules, transmission probabilities, and environmental conditions affect simulation outcomes.
- **Epidemiological dynamics:** Evolve from a binary model into a representation inspired by the SEIR model, distinguishing between susceptible, exposed, infectious, and recovered individuals.
- **Environmental influence:** Explore factors such as predominant propagation direction, spatial barriers, and terrain characteristics in the dynamics of infection.

These features will be implemented incrementally, starting with spatial propagation and gradually moving toward more advanced models.

## How the Model Works

The simulator uses a NumPy array to represent the environment. Each position contains a state that determines the condition of that cell.

In the current prototype, the states are:

- `0`: Healthy cell.
- `1`: Infected cell.

The simulation starts with a single infected cell. At each iteration, the algorithm identifies the orthogonal neighbors of infected cells, selects the healthy cells adjacent to them, and updates their states.

Propagation considers the four main directions: up, down, left, and right. Matrix boundaries are explicitly handled to prevent opposite edges of the environment from being incorrectly treated as neighbors due to circular shifts.

The process is repeated using the result of the previous iteration, allowing the infected region to expand progressively.

## Current Development Status

The project is being developed incrementally.

- [x] Create the two-dimensional grid.
- [x] Define the initial infected cell (patient zero).
- [x] Identify neighboring cells using `np.roll`.
- [x] Implement vectorized operations and boolean masks to identify new infections.
- [x] Handle matrix boundaries.
- [x] Implement infection propagation across multiple iterations.
- [x] Implement static spatial visualization using Matplotlib.
- [x] Animate the progression of infection over time.
- [x] Display infected and healthy cell counts during animation.
- [x] Experiment with different transmission rules and probabilities.
- [ ] Introduce epidemiological states and incubation periods.
- [ ] Explore environmental factors and spatial barriers.

## Technologies and Concepts

**Technologies**

- Python
- NumPy
- Matplotlib
- Git and GitHub

**Concepts**

- Scientific computing with Python.
- Vectorized array operations.
- Array indexing and boolean masks.
- Cellular automata.
- Dynamic system simulation.
- Spatial modeling and visualization.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/biancamendess/simulador-epidemiologico.git
cd simulador-epidemiologico
```

Create and activate a virtual environment on Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
python -m pip install numpy matplotlib
```

On Ubuntu or Debian, install Tkinter if it is not already available:

```bash
sudo apt update
sudo apt install python3-tk
```

Run the simulator:

```bash
python main.py
```

## Limitations

The current model uses simplified and deterministic rules. At this stage, it does not account for factors such as transmission probability, infection duration, recovery, or real epidemiological data.

This simulator is an educational project focused on computational modeling and scientific programming. It is not intended to provide epidemiological predictions or support real-world public health decisions.

## Learning Objectives

Develop an incremental software project to explore, in practice, how data structures, vectorized operations, visualization, and mathematical rules can be combined to build a spatial and temporal simulation.