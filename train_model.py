import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("student_data.csv")
data.columns = data.columns.str.strip()

# Keep only numeric columns
numeric_data = data.select_dtypes(include=['int64','float64'])

print("Numeric columns found:", list(numeric_data.columns))

# Use first 4 numeric columns as inputs
X = numeric_data.iloc[:, :4]

# Use 5th numeric column as target
y = numeric_data.iloc[:, 4]

print("Using inputs:", list(X.columns))
print("Using target:", y.name)

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
pickle.dump(model, open("predict.py.pkl", "wb"))

print("✅ Model trained with exactly 4 inputs.")
