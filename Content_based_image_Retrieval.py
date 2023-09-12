import os
import numpy as np
from skimage import io, color
from skimage.feature import local_binary_pattern
from skimage.transform import resize
from skimage.color import rgb2gray
from scipy.spatial.distance import euclidean
from PIL import Image

# Load the query image
query_image_path = 'C:\\Users\\Trainee\\Pictures\\Screenshots\\Screenshot (8).jpg'
query_image = io.imread(query_image_path)
query_image = resize(query_image, (256, 256))  # Resize the image for consistency

# Define the directory containing the database images
database_dir = 'C:\\Users\\Trainee\\Pictures\\Screenshots'

# Load and preprocess database images
database_images = []
for filename in os.listdir(database_dir):
    if filename.endswith(".jpg"):
        image_path = os.path.join(database_dir, filename)
        try:
            image = io.imread(image_path)
            if image.shape[2] == 4:  # Check if the image has 4 channels (RGBA)
                # Convert RGBA image to RGB using PIL
                image_pil = Image.open(image_path).convert("RGB")
                image = np.array(image_pil)
            image = resize(image, (256, 256))  # Resize the image for consistency
            database_images.append(image)
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            continue

# Extract color Histogram Features
def extract_color_histogram(image):
    image_lab = color.rgb2lab(image)
    hist_l, _ = np.histogram(image_lab[:, :, 0], bins=8, range=(0, 100))
    hist_a, _ = np.histogram(image_lab[:, :, 1], bins=8, range=(-128, 127))
    hist_b, _ = np.histogram(image_lab[:, :, 2], bins=8, range=(-128, 127))
    hist_features = np.concatenate((hist_l, hist_a, hist_b))
    normalized_hist = hist_features / np.sum(hist_features)  # Normalize the histogram
    return normalized_hist

# Extract features for the query image and database images
query_features = extract_color_histogram(query_image)
database_features = [extract_color_histogram(image) for image in database_images]

# Calculate Similarity and Rank images
def calculate_similarity(feature1, feature2):
    return euclidean(feature1, feature2)

# Calculate similarities and rank the database images
similarities = [calculate_similarity(query_features, feature) for feature in database_features]
sorted_indices = np.argsort(similarities)  # Indices of images in ascending order of similarity

# Display the ranked images
for i, idx in enumerate(sorted_indices):
    ranked_image = database_images[idx]
    io.imshow(ranked_image)
    io.show()

    if i >= 4:
        break
