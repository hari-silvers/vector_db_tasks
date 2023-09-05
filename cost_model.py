import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force_knn(query_point, dataset, k):
    distances = [(point, euclidean_distance(query_point, point)) for point in dataset]
    distances.sort(key=lambda x: x[1])
    return [point for point, _ in distances[:k]]

def io_cost_estimate(dataset_size, k):
    # In this simple example, assume that each point requires one I/O operation
    return dataset_size + k

# Generate a simple dataset of points
dataset = [Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10)]

# Define a query point
query_point = Point(6, 7)

# Set the value of k for k-NN search
k = 2

# Perform k-NN search using brute-force approach
knn_result = brute_force_knn(query_point, dataset, k)

# Estimate the I/O cost
estimated_io_cost = io_cost_estimate(len(dataset), k)

# Print the k-NN result and estimated I/O cost
print("k-NN result:", [f"({point.x},{point.y})" for point in knn_result])
print("Estimated I/O cost:", estimated_io_cost)
