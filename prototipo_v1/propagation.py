import numpy as np 

def propagate_infection(
        matrix,
        exposure_time,
        infection_time,
        rng,
        incubation_period,
        infectious_period
):
    right = np.roll(matrix, 1, axis=1)
    left = np.roll(matrix, -1, axis=1)
    up = np.roll(matrix, 1, axis=0)
    down = np.roll(matrix, -1, axis=0)

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

    return matrix, exposure_time, infection_time