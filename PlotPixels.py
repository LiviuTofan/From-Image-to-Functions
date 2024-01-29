import numpy as np
from matplotlib import pyplot as plt
from Coordinates import pixels_coordinates
from Coordinates import adjacent_pixels

data = pixels_coordinates('final.png')
coordinates, counter = adjacent_pixels(data)

# Flatten and reshape the list of lists
flat_list = [item for sublist in coordinates for item in sublist]
coordinates_array = np.array(flat_list)

# Rotation matrices
rotation_matrix = np.array([[-1, 0], [0, -1]])
rotation_matrix2 = np.array([[-1, 0], [0, 1]])

# Apply the rotation to each coordinate
rotated_coordinates = np.dot(coordinates_array, rotation_matrix)
rotated_coordinates2 = np.dot(rotated_coordinates, rotation_matrix2)

# Use rotated coordinates for plotting
plt.scatter(rotated_coordinates2[:, 0], rotated_coordinates2[:, 1], color="black", s=0.1)
plt.show()
