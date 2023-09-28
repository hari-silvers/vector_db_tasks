import numpy as np

vector_db = {
    'data_point_1' : np.array([1.2, 0.8, 2.5, 3.7]),
    "data_point_2" : np.array([0.5, 1.9, 3.2, 2.1]),
    "data_point_3" : np.array([2.0, 1.0, 4.0, 2.5]),
    # Add more data points as needed
}

def nearest_neighbor_search(query_vector, vector_db):
    best_match = None
    best_similarity = -1

    # Calculate cosine similarity and find the nearest neighbor
    for key, vector in vector_db.items():
        similarity = np.dot(query_vector, vector)/(np.linalg.norm(query_vector)*np.linalg.norm(vector))
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = key

        return best_match, best_similarity

# Define a query vector
query_vector = np.array([0.9, 1.2, 2.8, 3.5])

# Perform nearest neighbor search
nearest_neighbor, similarity = nearest_neighbor_search(query_vector, vector_db)

print(f"Query Vector: {query_vector}")
print(f"Nearest Neighbor: {nearest_neighbor}")
print(f"Cosine Similarity: {similarity:.4f}")
