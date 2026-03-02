import pandas as pd
import pickle
from sklearn.metrics import r2_score, mean_absolute_error

# Load dataset
data = pd.read_csv("student_data.csv")
data.columns = data.columns.str.strip()
data = data.select_dtypes(include=['int64','float64'])

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Load trained model
model = pickle.load(open("predict.py .pkl", "rb"))

# Predict
preds = model.predict(X)

# Evaluate
print("\n📊 Model Performance:\n")
print("R2 Score:", r2_score(y, preds))
print("MAE:", mean_absolute_error(y, preds))
