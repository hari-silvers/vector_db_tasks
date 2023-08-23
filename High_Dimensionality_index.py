import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

# Generate random data points in varying dimension

np.random.seed(0)  # for reproducablity

num_points = 100
dimensions = [2, 5, 10, 20, 50, 100]

data = {}
for dim in dimensions:
    data[dim] = np.random.random((num_points, dim))

# for calculating the average of euclidean distance pairwise

avg_distances = {}

for dim in dimensions:
    distances = []
    for i in range(num_points):
        for j in range(i+1, num_points):
            distance = euclidean(data[dim][i], data[dim][j])
            distances.append(distance)
    avg_distance = np.mean(distances)
    avg_distances[dim] = avg_distance

print('Average pairwise Distances:')
for dim, avg_dist in avg_distances.items():
    print(f"Dimension {dim} : {avg_dist:.4f}")

# visulaize the dimensional data using matplotlib library

plt.figure(figsize = (10, 6))
plt.plot(avg_distances.keys(), avg_distances.values(), marker='o')
plt.xlabel('number of Dimensions')
plt.ylabel('Average of pairwise Distance')
plt.title('Curse of Dimensionality: Average of pairwise Distance')
plt.grid(True)
plt.show()