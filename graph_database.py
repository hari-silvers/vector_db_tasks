import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec
import numpy as np
from sklearn.decomposition import PCA

# create a graph
G = nx.Graph()

# Add nodes
G.add_node('Alice')
G.add_node("Bob")
G.add_node('Charlie')
G.add_node("David")

# Add edges
G.add_edge("Alice", "Bob")
G.add_edge('Alice', "Charlie")
G.add_edge('Bob', "Charlie")
G.add_edge("Charlie", "David")

# Visualize the graph
pos = nx.spring_layout(G)   # Position nodes using a spring layout algorithm
nx.draw(G, pos, with_labels=True, node_size= 1000, font_size= 10, font_color= "black")

# Create a Node2vec instance
node2vec = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)

# Embed nodes
model = node2vec.fit(window=10, min_count=1, batch_words=4)

# Get node embeddings
node_embeddings = {node: model.wv[node] for node in G.nodes()}
print("Node embeddings:", node_embeddings)

# Exact node embeddings
node_names = list(node_embeddings.keys())
embeddings = np.array([node_embeddings[node] for node in node_names])

# Apply PCA tos reduce dimensions for visualization
pca = PCA(n_components=2)
embedding_2d = pca.fit_transform(embeddings)

# plot the node embeddings
plt.figure(figsize=(8, 6))
plt.scatter(embedding_2d[:, 0], embedding_2d[:, 1], c='b', marker="o")
for i, label in enumerate(node_names):
    plt.annotate(label, (embedding_2d[i, 0], embedding_2d[:, 1]), textcoords="offset points", xytext=(0, 10), ha="center")
plt.title('Node Embeddings using Node2Vec')
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.show()
