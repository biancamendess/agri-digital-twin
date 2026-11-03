# Intelligent Agricultural Disease Detection and Epidemiological Simulation

An ongoing research and development project focused on combining hyperspectral imaging, machine learning, geospatial analysis, and epidemiological modeling to detect agricultural diseases, identify infection hotspots, and simulate their spatial and temporal spread.

The long-term goal is to develop an intelligent system capable of identifying potential disease infections in crops, locating affected areas, estimating how an outbreak may evolve, and supporting decisions about where field inspections and disease management efforts should be prioritized.

**Initial case study:** Asian soybean rust (*Phakopsora pachyrhizi*).

## Project Vision

Agricultural diseases can spread across a field before their presence becomes visually apparent. Identifying early infection hotspots and understanding how a disease may spread are important steps toward more targeted monitoring and management.

This project proposes an integrated approach with two main components:

1. **Hyperspectral disease detection:** Analyze spectral information from crop images to identify patterns associated with plant infection, including potentially asymptomatic stages.
2. **Epidemiological simulation:** Use detected infection hotspots as initial conditions for a spatial and temporal model that simulates disease dissemination across the crop.

By connecting these components, the system aims to distinguish between areas with evidence of infection and areas that may still be healthy but are at higher risk of becoming infected.

The expected outcome is a decision-support system that can help identify where to inspect first, which areas require closer monitoring, and where preventive or management actions may be most relevant.

## Proposed System Architecture

The project is organized into three interconnected components.

### 1. Hyperspectral Disease Detection

Hyperspectral images contain information across multiple narrow wavelength bands, allowing the analysis of spectral signatures that may reveal physiological changes in plants.

This component will investigate how machine learning models can distinguish between:

- Healthy plants.
- Infected plants without visible symptoms.
- Infected plants with visible symptoms.
- Other stress conditions that may produce similar spectral responses.

The objective is to estimate infection probabilities and generate spatial maps highlighting potential disease hotspots.

### 2. Spatial and Temporal Epidemiological Simulation

The infection hotspots identified by the detection component will be used to initialize a disease propagation model.

The simulator will progressively incorporate biological and environmental factors that influence disease development and dissemination, such as:

- Infection and incubation periods.
- Pathogen development and sporulation.
- Spore dispersal.
- Wind direction and intensity.
- Temperature and humidity.
- Leaf wetness and environmental suitability.
- Crop distribution and spatial characteristics.

The model will simulate how the disease may evolve over time and identify regions that could become vulnerable to infection.

### 3. Risk Mapping and Decision Support

The final component will combine detection results and simulation outputs to produce spatial information that can support agricultural monitoring.

Potential outputs include:

- Maps of detected or suspected infection hotspots.
- Estimated disease progression over time.
- Areas with elevated risk of future infection.
- Priority regions for field inspection.
- Comparisons between different environmental and epidemiological scenarios.

The system is intended to support decision-making, not replace field diagnosis or professional agronomic recommendations.

## Initial Study Case: Asian Soybean Rust

The first disease selected for investigation is Asian soybean rust, caused by the fungus *Phakopsora pachyrhizi*.

This disease is particularly relevant because of its agricultural and economic impact, as well as the importance of environmental conditions and spore dispersal in its epidemiological dynamics.

The initial research will investigate the use of hyperspectral information to identify spectral patterns associated with soybean rust, followed by the development of a disease-specific spatial propagation model.

The architecture will be designed with the possibility of future adaptation to other agricultural diseases.

## Current Development

The project is currently in its computational modeling stage.

A preliminary spatial simulator is being developed using Python and NumPy. Its purpose is to establish the computational foundations required for representing spatial environments, infection states, neighborhood relationships, and temporal evolution.

The current prototype explores:

- Two-dimensional spatial environments represented by NumPy arrays.
- Infection propagation between neighboring cells.
- Vectorized operations and boolean masks.
- Boundary handling and spatial relationships.
- Iterative simulation and visualization with Matplotlib.
- Different transmission rules and probabilities.

This prototype is a starting point for the future epidemiological model. It does not yet represent the complete biological dynamics of Asian soybean rust.

## Development Roadmap

The project will be developed incrementally through the following stages.

### Phase 1 — Computational Foundations

- [x] Create a two-dimensional simulation environment.
- [x] Define an initial infected location.
- [x] Implement neighborhood detection using `np.roll`.
- [x] Apply vectorized operations and boolean masks.
- [x] Handle matrix boundaries.
- [x] Implement iterative infection propagation.
- [x] Visualize spatial infection patterns using Matplotlib.
- [x] Animate infection progression over time.
- [x] Display healthy and infected cell counts.
- [x] Experiment with transmission rules and probabilities.
- [ ] Consolidate and test the simulation of epidemiological states and incubation periods.
- [ ] Improve the representation of spatial barriers and environmental conditions.

### Phase 2 — Hyperspectral Data Acquisition and Processing

- [ ] Research available hyperspectral datasets related to soybean diseases.
- [ ] Investigate data acquisition methods and sensor characteristics.
- [ ] Study spectral calibration and reflectance conversion.
- [ ] Explore spectral preprocessing and noise reduction.
- [ ] Analyze spectral signatures of healthy and infected plants.
- [ ] Organize and document the experimental dataset.

### Phase 3 — Machine Learning for Disease Detection

- [ ] Define reliable infection labels and reference diagnoses.
- [ ] Explore methods for distinguishing healthy, asymptomatic, and symptomatic plants.
- [ ] Develop baseline machine learning models.
- [ ] Evaluate classification performance and false positive rates.
- [ ] Investigate early-stage disease detection.
- [ ] Generate infection probability maps.

### Phase 4 — Spatial Identification of Infection Hotspots

- [ ] Associate detection results with spatial coordinates.
- [ ] Generate georeferenced infection probability maps.
- [ ] Identify and group spatially connected infection hotspots.
- [ ] Estimate hotspot location, size, and confidence.
- [ ] Investigate hotspot evolution using images acquired on different dates.

### Phase 5 — Disease-Specific Epidemiological Modeling

- [ ] Study the biological dynamics of Asian soybean rust.
- [ ] Define epidemiological states and transition rules.
- [ ] Model infection latency and sporulation.
- [ ] Investigate local and wind-driven spore dispersal.
- [ ] Incorporate relevant meteorological variables.
- [ ] Evaluate the model under different environmental scenarios.

### Phase 6 — Integration of Detection and Simulation

- [ ] Use detected infection hotspots as simulation initial conditions.
- [ ] Incorporate uncertainty in infection location and detection confidence.
- [ ] Simulate disease progression across the agricultural area.
- [ ] Generate maps of estimated infection and future risk.
- [ ] Compare simulated outcomes with subsequent field observations.

### Phase 7 — Decision-Support System

- [ ] Develop geospatial visualization of infection and risk maps.
- [ ] Identify priority areas for field inspection.
- [ ] Compare alternative disease management scenarios.
- [ ] Evaluate the usefulness of risk maps for monitoring decisions.
- [ ] Investigate the generalization of the system to other crops and diseases.

## Technologies and Tools

**Current technologies**

- Python
- NumPy
- Matplotlib
- Git and GitHub

**Technologies to be explored**

- Pandas
- Scikit-learn
- PyTorch
- Rasterio
- GeoPandas
- Xarray
- Geospatial visualization tools

The technology stack will evolve according to the requirements of each development stage.

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

Install the current dependencies:

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

## Scientific Considerations and Limitations

The project is under active development and its proposed integrated system has not yet been validated in real agricultural field conditions.

Some important research challenges include:

- Spectral variations caused by diseases may overlap with those caused by other plant stresses.
- Detecting an infection before visible symptoms requires reliable reference data and experimental validation.
- The earliest detected infection hotspot is not necessarily the actual origin of the outbreak.
- Disease propagation depends on biological and environmental factors that must be represented using appropriate data and scientific assumptions.
- Results obtained under controlled experimental conditions may not generalize directly to different fields, sensors, cultivars, or environmental conditions.

The system will therefore be developed and evaluated in separate stages, with explicit attention to uncertainty, data quality, and independent validation.

## Project Objective

The ultimate objective is to connect real-world disease detection with epidemiological simulation.

Rather than simply identifying where a disease is present, the proposed system aims to estimate how it may spread, identify vulnerable areas, and help prioritize monitoring and management efforts.

**Detect the infection. Locate its hotspots. Simulate its spread. Support better decisions.**