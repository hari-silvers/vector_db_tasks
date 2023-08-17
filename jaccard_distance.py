import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')


def preprocess_text(text):
    text = ''.join([char.lower() for char in text if char.isalnum() or char.isspace()])
    words = nltk.word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return set(words)


def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union


document1 = "Jaccard Similarity is a measure used to determine the similarity between two sets of non-numeric data."
document2 = "Jaccard Similarity measures the ratio of the size of the intersection of two sets to the size of their union."

set1 = preprocess_text(document1)
set2 = preprocess_text(document2)

similarity_score = jaccard_similarity(set1, set2)

if similarity_score == 1:
    interpretation = "The sets are identical."
elif similarity_score == 0:
    interpretation = "The sets have no common elements."
else:
    interpretation = f"The sets have a Jaccard Similarity of {similarity_score:.2f}."

print("Set 1:", set1)
print("Set 2:", set2)
print("Jaccard Similarity:", similarity_score)
print(interpretation)
