import numpy as np
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections

# Generate random vectors as sample data
np.random.seed(0)
num_vectors = 100
dimension = 50
data = np.random.randn(num_vectors, dimension)

# Create an LSH engine with Random Binary Projections
num_bits = 10   # Number of hash bits
num_tables = 5  # Number of hash tables
rbp = RandomBinaryProjections('rbp', num_bits)
engine = Engine(dimension, lshashes=[rbp]*num_tables)

# Index the sample data vectors
for i, vector in enumerate(data):
    engine.store_vector(vector, i)

# Create a query vector for the search
query_vector = np.random.randn(dimension)

# Perform approximate search
num_results = 5  # Number of results of retrieve
results = engine.neighbours(query_vector)

print("Query Vector:")
print(query_vector)
print("\nApproximate Nearest Neighbors:")
for (vector_id, distance) in results:
    print(f"Vector ID: {vector_id}, Distance: {distance:.4f}")