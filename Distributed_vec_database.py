class DistributedVectorDatabase:
    def __init__(self, num_nodes):
        self.nodes = [[] for _ in range(num_nodes)]

    def add_vector(self, node_index, vector):
        self.nodes[node_index].append(vector)

    def process_vector(self, vector):
        # Simulate some processing on the vector
        return [ x * 2 for x in vector]

    def distribute_task(self, vector):
        # Simple load balancing: Fing the node with the fewest vectors
        min_index = min(range(len(self.nodes)), key= lambda i: len(self.nodes[i]))
        self.add_vector(min_index, vector)

    def print_nodes(self):
        for i, node in enumerate(self.nodes):
            print(f"Node {i}: {node}")

# Create a distributedVectroDatabase with 3 nodes
db = DistributedVectorDatabase(3)

# Define a simple vector
sample_vector = [1, 2, 3, 4, 5]

# Distribute tasks to simulate load balancing
for _ in range(10):
    db.distribute_task(sample_vector)

# Print the nodes to observe load balancing
db.print_nodes()

# Process a vector and update a specific node
processed_vector = db.process_vector((sample_vector))
db.add_vector(0, processed_vector)

# Print the nodes after processing
db.print_nodes()

