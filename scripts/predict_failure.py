import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("ml/builds.csv")

print("Dataset loaded successfully!")

# Separate features and target
X = df.drop("failed", axis=1)
y = df["failed"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

print("\nModel training completed!")

# Predict test data
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy * 100, "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Feature importance
print("\nFeature Importance:")
for feature, importance in zip(
    X.columns, model.feature_importances_
):
    print(feature, ":", round(importance, 3))

# Predict a new build
new_build = pd.DataFrame([{
    "files_changed": 12,
    "lines_changed": 450,
    "tests_touched": 0,
    "hour": 22
}])

prediction = model.predict(new_build)
probability = model.predict_proba(new_build)[0][1]

print("\nNew Build Prediction:")

if prediction[0] == 1:
    print("Build is likely to FAIL")
else:
    print("Build is likely to PASS")

print("Failure Probability:", round(probability * 100, 2), "%")