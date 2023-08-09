import numpy as np

# Generate random data points
np.random.seed(42)
num_points = 100
dimensions = 10
data = np.random.rand(num_points, dimensions)

# create hash functions
num_hash_tables = 5
num_hash_functions = 3

hash_tables = []
for _ in range(num_hash_tables):
    hash_functions = []
    for _ in range(num_hash_functions):
        random_vector = np.random.randn(dimensions)
        hash_functions.append(random_vector)
    hash_tables.append(hash_functions)

# Hash data points into buckets

buckets = [[] for _ in range(num_hash_tables)]
for point_idx, point in enumerate(data):
    for table_idx, hash_functions in enumerate(hash_tables):
        hash_values = []
        for function in hash_functions:
            hash_value = int(np.dot(point, function) > 0)
            hash_values.append(hash_value)
        hash_key = tuple(hash_values)
        buckets[table_idx].append((hash_key, point_idx))

# Query for approximate nearest neighbors
query_point_idx = np.random.randint(num_points)
query_point = data[query_point_idx]
similar_points = set()

for table_idx, hash_functions in enumerate(hash_tables):
    hash_values = []
    for function in hash_functions:
        hash_value = int(np.dot(query_point, function) > 0)
        hash_values.append(hash_value)
    hash_key = tuple(hash_values)

    for key, point_idx in buckets[table_idx]:
        if key == hash_key:
            similar_points.add(point_idx)

#  Print results
print("Query Point:", query_point_idx)
print("Approximate Nearest Neighbors:", similar_points)
