import librosa
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Load audio files
audio_file1 = 'audio_dir\\Sample_audio.wav'
audio_file2 = 'audio_dir\\Sample_audio.wav'

# Load audio and extract spectrogram
def extract_spectrogram(audio_file):
    y, sr = librosa.load(audio_file)
    spectrogram = np.abs(librosa.stft(y))
    return spectrogram

spectrogram1 = extract_spectrogram(audio_file1)
spectrogram2 = extract_spectrogram(audio_file2)

# Flatten and normalize spectrograms
spectrogram1_flat = spectrogram1.flatten()
spectrogram2_flat = spectrogram2.flatten()
spectrogram1_flat /= np.linalg.norm(spectrogram1_flat)
spectrogram2_flat /= np.linalg.norm(spectrogram2_flat)

# Combine the spectrogram's into a single array
spectrograms_combined = np.vstack([spectrogram1_flat, spectrogram2_flat])

# Build the nearest neighbors model using LSH
n_neighbors = 2  # You can adjust this based on your needs
nn = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto', metric='cosine')
nn.fit(spectrograms_combined)

# Query the nearest neighbors to find the similarity
query_result = nn.kneighbors([spectrogram1_flat], n_neighbors=n_neighbors)

similarities = 1 - query_result[0][0]
print("Cosine Similarities:", similarities)

threshold = 0.9

if all(similarity > threshold for similarity in similarities):
    print("The audio files are similar.")
else:
    print("The audio files are not similar.")
