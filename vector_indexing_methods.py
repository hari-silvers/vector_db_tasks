import numpy as np

# print 10 random 3 dimensional vectors.
num_vectors = 10
dimensionality = 3
np.random.seed(42)
vectors = np.random.rand(num_vectors, dimensionality)
print("Generated Vectors")
print(vectors)


def build_inverted_index(vectors):
    inverted_index = {}
    for idx, vector in enumerate(vectors):
        for feature_idx, feature_value in enumerate(vector):
            if feature_value not in inverted_index:
                inverted_index[feature_value] = [idx]
            else:
                inverted_index[feature_value].append(idx)
    return inverted_index


inverted_index = build_inverted_index(vectors)
print("\nInverted Index:")
print(inverted_index)


def search_inverted_index(inverted_index, feature_value):
    if feature_value in inverted_index:
        return inverted_index[feature_value]
    else:
        return []


search_value = 0.5
result_indices = search_inverted_index(inverted_index, search_value)
print(f"\nvectors with feature value {search_value}:")
print(vectors[result_indices])


from sklearn.neighbors import KDTree

def build_kd_tree(vectors):
    kdtree = KDTree(vectors)
    return kdtree

kd_tree = build_kd_tree(vectors)

def search_kd_tree(kdtree, query_vector, k=2):
    _, indices = kdtree.query([query_vector], k=k)
    return indices[0]

query_vector = [0.3, 0.4, 0.6]
nearest_neighbor_indices = search_kd_tree(kd_tree, query_vector)
nearest_neighbors = vectors[nearest_neighbor_indices]
print(f"\nQuery Vector: {query_vector}")
print(f"Nearest Neighbors: {nearest_neighbors}")


print("\n Generated Vecotors:")
print(vectors)

print("\nInverted Index:")
print(inverted_index)

print(f"\n Vectors with feature value {search_value}")
print(vectors[result_indices])

print(f"\n Query Vector: {query_vector}")
print(f"Nearest Neighbors: {nearest_neighbors}")