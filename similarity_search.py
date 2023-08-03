from math import sqrt

class Vector:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)


class VectorDatabase:
    def __init__(self):
        self.vectors = []

    def add_vector(self, vector):
        self.vectors.append(vector)

    def euclidean_distance(self, vector1, vector2):
        return sqrt(sum((a - b) ** 2 for a, b in zip(vector1.data, vector2.data)))

    def cosine_similarity(self, vector1, vector2):
        dot_product = sum(a * b for a, b in zip(vector1.data, vector2.data))
        norm1 = sqrt(sum(a ** 2 for a in vector1.data))
        norm2 = sqrt(sum(b ** 2 for b in vector2.data))
        return dot_product / (norm1 * norm2)

    def find_nearest_neighbors(self, query_vector, k=5):
        # Find k-nearest neighbors to the query vector
        distances = [(vector, self.euclidean_distance(query_vector, vector)) for vector in self.vectors]
        distances.sort(key=lambda x: x[1])  # Sort by distance
        return distances[:k]

    def find_similar_vectors(self, query_vector, similarity_threshold=0.9):
        # Find vectors similar to the query vector using cosine similarity
        similar_vectors = []
        for vector in self.vectors:
            similarity = self.cosine_similarity(query_vector, vector)
            if similarity >= similarity_threshold:
                similar_vectors.append((vector, similarity))
        return similar_vectors

if __name__ == "__main__":
    # Create a VectorDatabase instance
    db = VectorDatabase()

    # Add some vectors to the database
    vector1 = Vector([1, 2, 3, 4])
    vector2 = Vector([5, 6, 7, 8])
    vector3 = Vector([9, 10, 11, 12])
    db.add_vector(vector1)
    db.add_vector(vector2)
    db.add_vector(vector3)

    # Find k-nearest neighbors to a query vector
    query_vector = Vector([3, 4, 5, 6])
    k_nearest = db.find_nearest_neighbors(query_vector, k=4)
    print("K-Nearest Neighbors:")
    for vector, distance in k_nearest:
        print(f"Vector: {vector}, Distance: {distance}")

    # Find vectors similar to the query vector
    query_vector_cosine = Vector([1, 2, 3, 5])
    similar_vectors = db.find_similar_vectors(query_vector_cosine, similarity_threshold=0.8)
    print("\nSimilar Vectors (Cosine Similarity):")
    for vector, similarity in similar_vectors:
        print(f"Vector: {vector}, Similarity: {similarity:.2f}")


