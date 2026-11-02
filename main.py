import numpy as np
import matplotlib 
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#Representation of the farm as a 5x5 matrix with a single infected cell in the center
farm = np.zeros((5, 5), dtype=int)
farm[2, 2] = 1
img = plt.imshow(farm, cmap='Blues', vmin=0, vmax=1)
plt.axis('off')
rng = np.random.default_rng()


def propagate_infection(matrix):
    #creation of the matrices shifted in each direction place
    right = np.roll(matrix, 1, axis=1)
    left =np.roll(matrix, -1, axis=1)
    up = np.roll(matrix, 1, axis=0)
    down = np.roll(matrix, -1, axis=0)

    #correction of the edges to prevent "wrap-around"
    right[:, 0] = 0
    left[:, -1 ] = 0
    up[0, :] = 0
    down[-1, :] = 0

    #masks for each direction
    mask_right = right == 1
    mask_left = left == 1
    mask_up = up == 1
    mask_down = down == 1

 
    #Infected matrix and probability of infection
    infected_neighbors_right = mask_right.astype(int)
    infected_neighbors_left = mask_left.astype(int)
    infected_neighbors_up = mask_up.astype(int)
    infected_neighbors_down = mask_down.astype(int)

    infected_neighbors_total = (infected_neighbors_right + infected_neighbors_left + infected_neighbors_up + infected_neighbors_down)    

    probability_of_infection = 1 - (1 -0.30) ** infected_neighbors_total
    aleatory_matrix = rng.random(matrix.shape) 
    condition_matrix = aleatory_matrix < probability_of_infection
    comparation_matrix = (matrix == 0) & condition_matrix
    matrix[comparation_matrix] = 1
 
    return matrix 


#loop to propagate the infection for 4 iterations
for iteration in range(4):
    farm = propagate_infection(farm)
    infected_count = np.count_nonzero(farm == 1)
    healthy_count = np.count_nonzero(farm == 0)
    print(f"Round {iteration + 1}:" )
    print(farm)
    print(f"Number of infected cells: {infected_count}\n")
    print(f"Number of healthy cells: {healthy_count}\n")
    plt.title(f"Round:{iteration + 1}\n Infected Cells: {infected_count} | Healthy Cells: {healthy_count}")
    img.set_data(farm)
    plt.pause(0.5)  

plt.show()  
