# mlapp/train_model.py
import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump

# New training data (Years of experience vs Salary)
X = np.array([[1], [2], [3], [4], [5]])  # Features (Years of experience)
y = np.array([30000, 32000, 35000, 38000, 40000])  # Target (Salary)

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
dump(model, 'mlapp/model.joblib')

print("Model trained and saved!")
