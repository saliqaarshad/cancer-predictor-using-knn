import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import streamlit as st

# Load and prepare the dataset
df = pd.read_csv("KNNAlgorithmDataset.csv")
# Separate features and target
df=df.drop(columns=['Unnamed: 32'])
df.dropna()
x = df.drop(columns=['diagnosis', 'id'])
y = df['diagnosis'].apply(lambda x: 1 if x=='B' else 0).values
# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)
# Train the KNN model
model = KNeighborsClassifier(n_neighbors=1)
model.fit(x_train, y_train)
# Save the model
joblib.dump(model, 'MODEL.pkl')  # Corrected: changed from dumb to dump
