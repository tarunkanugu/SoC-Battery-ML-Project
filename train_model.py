# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the dataset
df = pd.read_csv("soc_data.csv")  # Make sure soc_data.csv is in the same folder

# Split features and target
X = df.drop("soc", axis=1)  # Features
y = df["soc"]               # Target: State of Charge

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "soc_model.pkl")

print("✅ Model trained and saved as soc_model.pkl")
