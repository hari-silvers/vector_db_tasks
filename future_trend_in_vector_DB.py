import numpy as np
import faiss

# Generate Random Multi-Modal data vectors
num_vectors = 100
vector_dimension = 50

# Generate random vectors for three modalities: Text, Image and audio
text_vectors = np.random.rand(num_vectors, vector_dimension)
image_vectors = np.random.rand(num_vectors, vector_dimension)
audio_vectors = np.random.rand(num_vectors, vector_dimension)

# Combine the modalities to create multi-modal data vectors
multi_modal_vectors = np.hstack((text_vectors, image_vectors, audio_vectors))

# Bulid a Simple Vector Index
index = faiss.IndexFlatL2(vector_dimension*3)  # Create an index for multi-modal

# Add the multi-modal vectors to the index
index.add(multi_modal_vectors)

# Perform Similarity Search
query_vector = np.random.rand(vector_dimension * 3)  # Generate a query vector
k=5  # Number of nearest neighbors to retrieve

# Perform a similarity search
distance, indices = index.search(np.array([query_vector]), k)

# Retrieve and Analyze Results
print("Query Vector:")
print(query_vector)

print("\nNearest Neighbors:")
for i in range(k):
    neighbor_index = indices[0][i]
    neighbor_distance = distance[0][i]
    print(f"Neighbor {i + 1}: index {neighbor_index}, Distance {neighbor_distance:.4f}")