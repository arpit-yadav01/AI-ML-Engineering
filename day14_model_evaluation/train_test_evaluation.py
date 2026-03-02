

import numpy as np
import matplotlib.pyplot as plt

# Import ML tools
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

print("📊 Day 14 - Model Evaluation")

# Step 1: Create Dataset
# Feature (Hours studied)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)

# Target (Marks)
y = np.array([40, 50, 55, 65, 70, 75, 85, 95])

# Step 2: Split Data
# 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Create Model
model = LinearRegression()

# Step 4: Train Model on Training Data
model.fit(X_train, y_train)

# Step 5: Predict on Test Data
y_pred = model.predict(X_test)

# Step 6: Evaluate Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Test Data:", X_test.flatten())
print("Actual Marks:", y_test)
print("Predicted Marks:", y_pred)

print("\nModel Performance:")
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

# Step 7: Visualization
plt.scatter(X_train, y_train, color="blue", label="Training Data")
plt.scatter(X_test, y_test, color="green", label="Test Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Train/Test Split Visualization")
plt.legend()
plt.show()