import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("📈 Linear Regression - Beginner Version")

# Feature (Input)
# Hours studied
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Target (Output)
# Marks scored
y = np.array([45, 50, 60, 65, 75, 85])

# Create model object
model = LinearRegression()

# Train model (learning happens here)
model.fit(X, y)

# Predict using same data
predictions = model.predict(X)

print("Predicted Marks:", predictions)

# Predict for new value
new_hours = np.array([[7]])
new_prediction = model.predict(new_hours)

print("Predicted marks for 7 hours:", new_prediction)

# Visualization
plt.scatter(X, y)
plt.plot(X, predictions)
plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()