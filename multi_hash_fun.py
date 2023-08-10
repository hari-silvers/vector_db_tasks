import numpy as np
from sklearn.datasets import make_blobs
from sklearn.neighbors import NearestNeighbors

# Generate a synthetic dataset
X, _ = make_blobs(n_samples=1000, n_features=50, centers=5, random_state=42)

# Create a NearestNeighbors model with LSH (Multi-index hashing)
n_neighbors = 5
index_params = dict(algorithm='auto', n_neighbors=n_neighbors, n_jobs=-1)
neigh = NearestNeighbors(**index_params)
neigh.fit(X)

# Step 3: Define a query vector
query_vector = np.random.rand(1, 50)

# Step 4: Perform the nearest neighbor search using the LSH model
distances, indices = neigh.kneighbors(query_vector)

# Step 5: Display the nearest neighbors and their distances
print("Query Vector:", query_vector)
print("Nearest Neighbors:")
for dist, ind in zip(distances[0], indices[0]):
    print(f"Distance: {dist:.4f}, Index: {ind}, Vector: {X[ind]}")
