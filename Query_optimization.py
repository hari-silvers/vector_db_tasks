import numpy as np

# Generate the sample data: List of vectors
data = [
    np.array([0.2, 0.5, 0.1, 0.4]),
    np.array([0.6, 0.4, 0.8, 0.7]),
    np.array([0.4, 0.2, 0.1, 0.3]),
    np.array([0.5, 0.8, 0.7, 0.6])
]

# Query Vector
query_vector = np.array([0.7, 0.3, 0.8, 0.2])


# Calculate cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity


# Perform similarity search using brute force approach
def brute_force_search(query, data):
    similarities = [cosine_similarity(query, doc) for doc in data]
    most_similar_index = np.argmax(similarities)
    return most_similar_index


# Indexing using precomputed norms
def create_index(data):
    norms = [np.linalg.norm(doc) for doc in data]
    return norms


# Perform similarity search using indexing
def indexed_search(query, data, index):
    query_norm = np.linalg.norm(query)
    normalized_query = query / query_norm
    normalized_data = [doc / norm for doc, norm in zip(data, index)]

    similarities = [np.dot(normalized_query, doc) for doc in normalized_data]
    most_similar_index = np.argmax(similarities)
    return most_similar_index


# Brute-force similarity search
bf_result = brute_force_search(query_vector, data)
print("Brute-Force Result:", bf_result)

# Indexing
index = create_index(data)

# Indexed similarity search
indexed_result = indexed_search(query_vector, data, index)
print("Indexed Result:", indexed_result)
