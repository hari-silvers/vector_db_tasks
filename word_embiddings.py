# import neccessary Libraries

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
import random
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment import SentimentIntensityAnalyzer

# Load movie reviews dataset
nltk.download('movie_reviews')
nltk.download('vader_lexicon')

# prepare data for sentiment analysis
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in
             movie_reviews.fileids(category)]

# Shuffle the documents
random.shuffle(documents)


# Define feature extraction function
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features


# Extract features and split data into training and testing sets
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]  # Choose top 2000 most frequent words as features
featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[:100], featuresets[:100]

# Train a Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Test the classifier
accuracy = nltk.classify.accuracy(classifier, test_set)
print("Classify Accuracy:", accuracy)

# Perform sentiment analysis on new text
new_text = "This movie was fantastic! I loved every moment of it."
new_text_tokens = word_tokenize(new_text.lower())
new_text_features = document_features(new_text_tokens)
sentiment = classifier.classify(new_text_features)
print("Sentiment:", sentiment)

# Step 9: Use SentimentIntensityAnalyzer from NLTK
sia = SentimentIntensityAnalyzer()
sentiment_scores = sia.polarity_scores(new_text)
print("Sentiment Scores:", sentiment_scores)
