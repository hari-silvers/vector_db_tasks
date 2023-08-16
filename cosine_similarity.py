import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example document for searching
documents = ["This is the first file",
             "This  is the second file",
             "and this is the third document",
             "Is this is the first document?"]

# Vectorization - Converting text documents into matrix
vectorizer = CountVectorizer().fit_transform(documents)

# Calculate the cosine similarity
cosine_sim_matrix = cosine_similarity(vectorizer)

# Working with the document sample
num_documents = len(documents)

for i in range(num_documents):
    for j in range(i+1, num_documents):
        similarity = cosine_sim_matrix[i, j]
        print(f"Cosine Similarity between Document {i+1} and Document {j+1}:{similarity:.4f}")