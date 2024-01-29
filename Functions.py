import numpy as np
import matplotlib.pyplot as plt
from Coordinates import pixels_coordinates, adjacent_pixels
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def rotate_points(points, angle):
    angle_rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad), np.cos(angle_rad)]
    ])
    return np.dot(points, rotation_matrix)


coordinates = pixels_coordinates('final.png')
data = adjacent_pixels(coordinates)
data = data[0]

# Choose an angle for rotation
angle = 180  # Rotating by 180 degrees (mirroring)

# Define the maximum degree to test for polynomials
max_degree = 10
degrees = range(1, max_degree + 1)

# List to store the best degree for each edge
best_degrees = []

# Start plotting
plt.figure(figsize=(12, 8))

# Process each sublist (edge)
for sublist in data:
    edge = np.array(sublist)

    # Check if there are enough points for cross-validation
    if len(edge) < 5:
        continue

    x = edge[:, 0].reshape(-1, 1)  # Reshape for sklearn
    y = edge[:, 1]

    best_degree = None
    best_score = float('inf')

    for degree in degrees:
        # Create a pipeline that creates polynomial features and fits a linear regressor
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

        # Perform k-fold cross-validation
        try:
            scores = cross_val_score(model, x, y, scoring='neg_mean_squared_error', cv=5)
        except ValueError:
            # Not enough samples for cross-validation
            continue

        score = -scores.mean()  # Negate to get positive MSE

        # Update the best degree if this score is better
        if score < best_score:
            best_score = score
            best_degree = degree

    # Skip if we couldn't compute a best degree
    if best_degree is None:
        continue

    best_degrees.append(best_degree)

    # Fit the model with the best degree found
    model = make_pipeline(PolynomialFeatures(best_degree), LinearRegression())
    model.fit(x, y)

    # Generate points for plotting the smooth curve
    x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
    y_range = model.predict(x_range)

    # Plot the original points and the fitted curve
    plt.scatter(x, y, color='blue', s=1)  # Original points
    plt.plot(x_range, y_range, color='red')  # Fitted curve

# Show combined plot for all edges
plt.title("Polynomial Fit for Edges")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.show()

# Optionally, print out or process the best degrees for each edge
print("Best polynomial degrees for each edge:", best_degrees)
