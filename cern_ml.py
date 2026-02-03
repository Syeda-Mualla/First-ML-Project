import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("cern_sample.csv")

print("\n=== RAW DATA ===")
print(df)

# Convert Particle column to numeric labels
df["Label"] = df["Particle"].astype("category").cat.codes

# Save label decoder (mapping numbers → names)
label_map = dict(enumerate(df["Particle"].astype("category").cat.categories))

# Features and target
X = df[["Energy_GeV", "Momentum_GeV_c"]]
y = df["Label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("\n=== ML MODEL ACCURACY ===")
print(accuracy)

# Predict a new fake event
test_event = pd.DataFrame({"Energy_GeV": [126.4], "Momentum_GeV_c": [204]})
predicted_label = model.predict(test_event)[0]

print("\n=== PREDICTED PARTICLE TYPE FOR NEW EVENT ===")
print(label_map[predicted_label])