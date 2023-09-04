import numpy as np

# create a sample dataset of vectors
dataset = [
    np.array([1.0, 2.0]),
    np.array([2.0, 3.0]),
    np.array([4.0, 5.0]),
    np.array([6.0, 7.0]),
]

# Query vector
Query_vector = np.array([3.0, 4.0])

# calculate cosine similarity between vectors
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm2 * norm1)
    return similarity

# Perform similarity search
similarities = [cosine_similarity(Query_vector, vec) for vec in dataset]

# Find the index of the most similar vector
most_similar_index = np.argmax(similarities)
most_similar_vector = dataset[most_similar_index]

print("Query vector :", Query_vector)
print()
print("Sample dataset for the Given set: ", dataset)
print()
print("Most Similar Vector:", most_similar_vector)
