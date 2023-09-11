import numpy as np

# Define a list of generates
genres = ['Action', 'Comedy', 'Drama', 'Sci-fi', 'Horror', 'Romance']

# Create vector representation for movies
movies = {
    'Movie1': [1, 0, 1, 0, 0, 1],
    'Movie2': [1, 1, 0, 0, 0, 1],
    'Movie3': [0, 1, 1, 1, 0, 0],
    'Movie4': [0, 0, 1, 0, 1, 1],
    'Movie5': [1, 0, 0, 1, 1, 0],
}


# Define a cosine similarity function for comparing the two functions
def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    similarit = dot_product / (norm_b * norm_a)
    return similarit


# Calculate the Similarity between Movie1 and other movies
target_movie = "Movie1"
similarities = {}
for movie, vector in movies.items():
    if movie != target_movie:
        similarity = cosine_similarity(movies[target_movie], vector)
        similarities[movie] = similarity

# Sort and get movie recommendations based on similarity
recommendations = sorted(similarities, key=similarities.get, reverse=True)

# Let's display the recommended movies
print(f"Recommendations for {target_movie}:")
for i, movie in enumerate(recommendations, start=1):
    print(f"{i}. {movie} (Similarity : {similarities[movie]:.2f})")
