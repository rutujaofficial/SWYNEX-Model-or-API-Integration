
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Step 1: Load the sample dataset
data = pd.read_csv("sample_data.csv")

# Step 2: Select the input features
X = data[
    [
        "account_age_months",
        "connections",
        "profile_completeness",
        "experience_consistency"
    ]
]

# Step 3: Select the target label
y = data["label"]

# Step 4: Create the Decision Tree model
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

# Step 5: Train the model
model.fit(X, y)
# Evaluate model on the training dataset
accuracy = model.score(X, y)

print("Model Training Accuracy:", accuracy * 100, "%")
print("===================================")
print(" LINKEDIN PROFILE DETECTION SYSTEM")
print("===================================")

# Step 6: Get profile details from the user
age = int(input("Enter account age in months: "))
connections = int(input("Enter number of connections: "))
completeness = float(input("Enter profile completeness (0-100): "))

experience = input(
    "Is experience consistent? (yes/no): "
).strip().lower()

# Step 7: Validate the inputs
if age < 0 or connections < 0:
    raise ValueError("Age and connections cannot be negative.")

if not 0 <= completeness <= 100:
    raise ValueError("Completeness must be between 0 and 100.")

if experience not in ["yes", "no"]:
    raise ValueError("Please enter yes or no.")

experience_value = 1 if experience == "yes" else 0

# Step 8: Prepare input for prediction
new_profile = pd.DataFrame(
    [[age, connections, completeness, experience_value]],
    columns=[
        "account_age_months",
        "connections",
        "profile_completeness",
        "experience_consistency"
    ]
)

# Step 9: Predict the profile category
prediction = model.predict(new_profile)[0]

# Step 10: Display the result
print("\n========== PREDICTION ==========")

if prediction == 1:
    print("Result: Potentially suspicious")
else:
    print("Result: Genuine-looking")

print("================================")
print("This is an experimental prediction")
print("based on synthetic training data.")
print("It does not verify a real identity.")

