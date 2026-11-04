import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from src.epidemiology.propagation import propagate_infection


colors = ['#9CA3AF', '#FACC15', '#EF4444', '#22A06B']
cmap = ListedColormap(colors)

bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
norm = BoundaryNorm(bounds, cmap.N)

# Initialize the farm grid and patient zero
farm = np.zeros((50, 50), dtype=int)
farm[25, 25] = 2

# Track the duration of each disease stage
exposure_time = np.zeros(farm.shape, dtype=int)
infection_time = np.zeros(farm.shape, dtype=int)

# Define disease parameters (in simulation rounds)
incubation_period = 3
infectious_period = 5

img = plt.imshow(farm, cmap=cmap, norm=norm)
plt.axis('off')
rng = np.random.default_rng()


# Run the simulation
for iteration in range(70):

    farm, exposure_time, infection_time = propagate_infection(
        farm,
        exposure_time,
        infection_time,
        rng,
        incubation_period,
        infectious_period
    )

    susceptible_count = np.count_nonzero(farm == 0)
    exposed_count = np.count_nonzero(farm == 1)
    infectious_count = np.count_nonzero(farm == 2)
    recovered_count = np.count_nonzero(farm == 3)

    print(f"Round {iteration + 1}:")
    print(farm)
    print(f"Number of susceptible cells: {susceptible_count}\n")
    print(f"Number of exposed cells: {exposed_count}\n")
    print(f"Number of infectious cells: {infectious_count}\n")
    print(f"Number of recovered cells: {recovered_count}\n")

    plt.title(
        f"Round: {iteration + 1}\n"
        f"Susceptible Cells: {susceptible_count} | Exposed Cells: {exposed_count} \n Infectious Cells: {infectious_count} | Recovered Cells: {recovered_count}"
    )

    img.set_data(farm)
    plt.pause(0.5)

plt.show()