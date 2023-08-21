import math


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    squared_distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dis = math.sqrt(squared_distance)
    return dis


# Define points
point_a = (3, 5)
point_b = (1, 9)

# Calculate Euclidean Distance
distance = euclidean_distance(point_a, point_b)

# Display the result
print(f"The Euclidean Distance between {point_a} and {point_b} is {distance:.2f}")
