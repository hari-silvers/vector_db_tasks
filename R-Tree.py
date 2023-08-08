# import  the neccessary modules for the rtree
from rtree import index

# create the index
idx = index.Index()

# Insert points (format: (x_min, y_min, x_max, y_max))
idx.insert(2, (4, 3, 5, 6))
idx.insert(1, (4, 2, 7, 5))
idx.insert(3, (1, 4, 3, 7))

# Query for objects that instersect with a given bounding
query_bbox = (3, 4, 6, 7) # Query bounding box
result_ids = list(idx.intersection(query_bbox))

print("objects that intersect with the query bounding box")
for obj_id in result_ids:
    print(f"Object ID: {obj_id}")

# Find the nearest object to a given point
query_point = (4.5, 3.5)   # Query point
nearest_obj = list(idx.nearest(query_point, 1))[0]

print(f"Nearest object to query point: object ID {nearest_obj}")

idx.close()