#!/usr/bin/env python3

# Predict how far in the NCAA tournament a team will go, takes user input for the data for the team to predict
# also outputs data for a model trained and tested on our split up data.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


# Function to get user input, input data will be used to make prediction
def get_user_input(features):
    print("\nInput the asked-for data:")
    user_input = {}
    for feature in features:
        value = float(input(f"Enter value for {feature}: "))
        user_input[feature] = value
    return user_input


# Load data
file_path = 'cbb.csv'
# Convert to pandas df
data = pd.read_csv(file_path)

# Preprocess data
# Drop empty rows in POSTSEASON, inplace= True means modify original
data.dropna(subset=['POSTSEASON'], inplace=True)
# Drop columns, I don't think these are important and some might cause issues/more work
data.drop(['TEAM', 'CONF', 'YEAR'], axis=1, inplace=True)

# Encode POSTSEASON because not everything is nums, basically turns it into # data so model understands it
encoder = LabelEncoder()
# Takes unique values in POSTSEASON, later to be used for mapping encoding(Line 43) and OG so that we can output the actual rounds
og_labels = data['POSTSEASON'].unique()
data['POSTSEASON'] = encoder.fit_transform(data['POSTSEASON'])
encoded_labels = data['POSTSEASON'].unique()

# Create a mapping from encoded labels to original labels
label_mapping = {encoded: original for encoded, original in zip(encoded_labels, og_labels)}

# Separate the column we are predicting from the rest
X = data.drop('POSTSEASON', axis=1)
y = data['POSTSEASON']

# Split dataset for train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize Random Forest Classifier
rf_model = RandomForestClassifier(random_state=98)

# Hyperparameter tuning w/ Grid Search
param_grid = {
    'n_estimators': [100, 200, 300], # Number of trees in our forest
    'max_features': ['sqrt', 'log2'], 
    'max_depth': [10, 20, 30, None], # Depth of our tree
    'min_samples_split': [2, 5, 10], # Minimum number of samples needed to split a node
    'min_samples_leaf': [1, 2, 4]    # Minimum number of samples needed to be at a leaf node
}

grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=1)

# Fit grid search to data and get best estimator
grid_search.fit(X_train_scaled, y_train)
best_rf_model = grid_search.best_estimator_

# Evaluate the model
accuracy = accuracy_score(y_test, best_rf_model.predict(X_test_scaled))
classification_rep = classification_report(y_test, best_rf_model.predict(X_test_scaled), target_names=[label_mapping[label] for label in sorted(label_mapping.keys())],zero_division=0)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

# User Input
user_input = np.array(list(get_user_input(X.columns).values())).reshape(1, -1)
user_input_scaled = scaler.transform(user_input)

# Make prediction
prediction = best_rf_model.predict(user_input_scaled)
predicted_round = encoder.inverse_transform(prediction)[0]
print(f"\nPredicted Round: {predicted_round}")
