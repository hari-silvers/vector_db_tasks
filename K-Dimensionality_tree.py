# creating the sample data
data = [(2, 4), (3, 5), (2, 5), (9, 8), (7, 5), (3, 5), (4, 7)]

# creating a programmatic approach for the K-Dimensionality
class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, points):
        self.root = self._build_kd_tree(points, depth=0)

    def _build_kd_tree(self, points, depth):
        if not points:
            return None

        dimension = depth % 2  # Split along x-axis at even depth, y-axis at odd depth
        points.sort(key=lambda point: point[dimension])
        median_idx = len(points) // 2

        return KDNode(
            point=points[median_idx],
            left=self._build_kd_tree(points[:median_idx], depth + 1),
            right=self._build_kd_tree(points[median_idx + 1 :], depth + 1),
        )

import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def nearest_neighbor_search(node, query_point, depth=0):
    if node is None:
        return None

    dimension = depth % 2
    current_point = node.point

    if query_point == current_point:
        return current_point

    if query_point[dimension] < current_point[dimension]:
        next_node = node.left
        opposite_node = node.right
    else:
        next_node = node.right
        opposite_node = node.left

    best = current_point
    best_dist = distance(current_point, query_point)

    candidate = nearest_neighbor_search(next_node, query_point, depth + 1)
    if candidate is not None:
        candidate_dist = distance(candidate, query_point)
        if candidate_dist < best_dist:
            best = candidate
            best_dist = candidate_dist

    if best_dist > abs(query_point[dimension] - current_point[dimension]):
        candidate = nearest_neighbor_search(opposite_node, query_point, depth + 1)
        if candidate is not None:
            candidate_dist = distance(candidate, query_point)
            if candidate_dist < best_dist:
                best = candidate
                best_dist = candidate_dist

    return best



# testing with an output

query_point = (4,7)
kd_tree = KDTree(data)
nearest_neighbor = nearest_neighbor_search(kd_tree.root, query_point)

print(f"Query Point : {query_point}")
print(f"Nearest Neighbor: {nearest_neighbor}")
