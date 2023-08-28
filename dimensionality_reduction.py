import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_swiss_roll
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.manifold import LocallyLinearEmbedding

# Generate swiss-roll datasets containg 1000 samples
X, color = make_swiss_roll(n_samples=1000, noise=0.2, random_state=42)

# Visualize the data in 3D format
fig= plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0],X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
plt.show()

# Now perform the PCA with 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualize the PCA reduced data
plt.scatter(X_pca[:, 0],X_pca[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title('PCA Result')
plt.show()

# Perform t-SNE with 2 component
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X)

# Visualize the t-SNE result
plt.scatter(X_tsne[:, 0],X_tsne[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title('t-SNE Result')
plt.show()

# Perform LLE with 2 components
lle = LocallyLinearEmbedding(n_components=2, n_neighbors=10, random_state=42)
X_lle = lle.fit_transform(X)

# Visualize the LLE result
plt.scatter(X_lle[:, 0],X_lle[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title('LLE Result')
plt.show()