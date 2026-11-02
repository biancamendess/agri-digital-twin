import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

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


def propagate_infection(matrix):

    # Identify infectious neighbors in the four orthogonal directions
    right = np.roll(matrix, 1, axis=1)
    left = np.roll(matrix, -1, axis=1)
    up = np.roll(matrix, 1, axis=0)
    down = np.roll(matrix, -1, axis=0)

    # Prevent wrap-around between opposite edges
    right[:, 0] = 0
    left[:, -1] = 0
    up[0, :] = 0
    down[-1, :] = 0

    mask_right = right == 2
    mask_left = left == 2
    mask_up = up == 2
    mask_down = down == 2

    infected_neighbors_total = (
        mask_right.astype(int)
        + mask_left.astype(int)
        + mask_up.astype(int)
        + mask_down.astype(int)
    )

    # Calculate transmission probability based on infectious neighbors
    probability_of_infection = 1 - (1 - 0.30) ** infected_neighbors_total
    aleatory_matrix = rng.random(matrix.shape)
    condition_matrix = aleatory_matrix < probability_of_infection
    comparation_matrix = (matrix == 0) & condition_matrix

    # Susceptible (S) -> Exposed (E)
    exposed_mask = matrix == 1
    exposure_time[exposed_mask] += 1
    matrix[comparation_matrix] = 1
    exposure_time[comparation_matrix] = 0

    # Infectious (I) -> Recovered (R)
    infected_mask = matrix == 2
    infection_time[infected_mask] += 1

    ready_to_recover_mask = infected_mask & (infection_time >= infectious_period)
    matrix[ready_to_recover_mask] = 3

    # Exposed (E) -> Infectious (I)
    ready_to_infect_mask = exposed_mask & (exposure_time >= incubation_period)
    matrix[ready_to_infect_mask] = 2
    infection_time[ready_to_infect_mask] = 0
    exposure_time[ready_to_infect_mask] = 0

    return matrix


# Run the simulation
for iteration in range(70):

    farm = propagate_infection(farm)

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