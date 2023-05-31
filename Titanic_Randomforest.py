# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the Titanic dataset
train_data = pd.read_csv('sources/titanic/train.csv')
test_data = pd.read_csv('sources/titanic/test.csv')

# Preprocessing: Select relevant features and handle missing values
selected_features = ['PassengerId','Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Survived']
train_data = train_data[selected_features].dropna()
test_data = test_data[selected_features[:-1]].fillna(0)  # Fill missing values with 0

# Convert categorical variables into numerical values
train_data['Sex'] = train_data['Sex'].map({'female': 0, 'male': 1})
train_data['Embarked'] = train_data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
test_data['Sex'] = test_data['Sex'].map({'female': 0, 'male': 1})
test_data['Embarked'] = test_data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Split the dataset into features (X) and target variable (y)
X_train = train_data.drop('Survived', axis=1)
y_train = train_data['Survived']

# Build a decision tree classifier
model = RandomForestClassifier() #n_estimators=100, max_depth=5, random_state=1
model.fit(X_train, y_train)

# Make predictions on the test set
X_test = test_data
predictions = model.predict(X_test)

# Create a submission DataFrame
submission = pd.DataFrame({
    'PassengerId': test_data['PassengerId'],
    'Survived': predictions
})

# Save the submission to a CSV file
submission.to_csv('submission.csv', index=False)
