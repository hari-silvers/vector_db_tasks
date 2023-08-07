import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# load the necessary data
iris = load_iris()
x = iris.data
y = iris.target

# split the data into training and testing datasets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# implement the k-NN algorithm
k=3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_train_scaled, y_train)

# Make predictions
y_pred = knn.predict(x_test_scaled)

# Now evaluate the performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)


