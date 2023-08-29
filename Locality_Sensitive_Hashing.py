import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

# Generate the data sets
np.random.seed(0)
num_features = 5
num_data_points = 10
data = np.random.rand(num_data_points, num_features)

# define a class for the LSH definition
class LSH:
    def __init__(self, num_hash_functions, num_buckets):
        self.num_hash_functions = num_hash_functions
        self.num_buckets = num_buckets
        self.hash_functions = [np.random.randn(num_features) for _ in range(num_hash_functions)]
        self.buckets = {i: [] for i in range(num_buckets)}

    def hash(self, point):
        return [int(np.dot(hash_function, point) > 0) for hash_function in self.hash_functions]

    def index(self, data):
        for idx, point in enumerate(data):
            hash_values = self.hash(point)
            for i, val in enumerate(hash_values):
                self.buckets[i * 2 + val].append(idx)

    def query(self, query_point):
        hash_values = self.hash(query_point)
        candidate_set = set()
        for i, val in enumerate(hash_values):
            candidate_set.update(self.buckets[i * 2 + val])
        return candidate_set

lsh = LSH(num_hash_functions=3, num_buckets=10)
lsh.index(data)

# query a data point
query_idx = 0
query_point = data[query_idx]
candidate_set = lsh.query(query_point)

# Find the index of the nearest neighbor in the candidate set
distances = euclidean_distances([query_point], data[np.array(list(candidate_set))])
nearest_neighbor_candidate_idx = np.argmin(distances)
nearest_neighbor_idx = list(candidate_set)[nearest_neighbor_candidate_idx]
nearest_neighbor = data[nearest_neighbor_idx]

# print the output using print statement
print(f'Query Point: {query_point}')
print(f'Nearest Neighbor: {nearest_neighbor}')
