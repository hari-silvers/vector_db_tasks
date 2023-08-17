import numpy as np

class Node:
    def __init__(self, vector, left=None, right=None):
        self.vector = vector
        self.left = left
        self.right = right


def build_kdtree(points, depth=0):
    if not points:
        return None

    axis = depth % len(points[0])
    sorted_points = sorted(points, key=lambda point: point[axis])
    median_idx = len(sorted_points) // 2
    median = sorted_points[median_idx]

    return Node(
        vector=median,
        left=build_kdtree(sorted_points[:median_idx], depth + 1),
        right=build_kdtree(sorted_points[median_idx + 1:], depth + 1)
    )


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)


def knn_search_kdtree(root, query, k=1):
    def _search(node, depth=0):
        if node is None:
            return []

        axis = depth % len(node.vector)
        if query[axis] < node.vector[axis]:
            next_node, other_node = node.left, node.right
        else:
            next_node, other_node = node.right, node.left

        neighbors = _search(next_node, depth + 1)

        if len(neighbors) < k or abs(query[axis] - node.vector[axis]) < cosine_similarity(neighbors[-1][0], query):
            neighbors = neighbors + [(node.vector, cosine_similarity(node.vector, query))]
            neighbors.sort(key=lambda neighbor: neighbor[1], reverse=True)
            neighbors = neighbors[:k]

        if len(neighbors) < k or abs(query[axis] - node.vector[axis]) < cosine_similarity(neighbors[-1][0], query):
            neighbors += _search(other_node, depth + 1)

        return neighbors

    return _search(root)


# Sample data (2D vectors)
data = [
    np.array([1.0, 2.0]),
    np.array([3.0, 4.0]),
    np.array([5.0, 6.0]),
    np.array([7.0, 8.0]),
    np.array([9.0, 10.0])
]

# Build k-d tree
root = build_kdtree(data)

# Query vector
query_vector = np.array([2.5, 3.5])

# Perform k-NN search using k-d tree
k_neighbors = knn_search_kdtree(root, query_vector, k=2)

# Display results
print("Query Vector:", query_vector)
print("K-Nearest Neighbors:")
for neighbor, similarity in k_neighbors:
    print("Vector:", neighbor, "Similarity:", similarity)
