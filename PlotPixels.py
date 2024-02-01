import numpy as np
from matplotlib import pyplot as plt
from Coordinates import pixels_coordinates, adjacent_pixels, get_upper_edge_pixels, sort_pixels_by_adjacency, get_all_edges

# Load pixel coordinates
pixel_coordinates = pixels_coordinates('final.png')

# Get adjacent pixels
adjacent_pixels = adjacent_pixels(pixel_coordinates)

result = []
for edge in adjacent_pixels:
    upper_pixels = get_upper_edge_pixels(edge)
    sorted_pixels = sort_pixels_by_adjacency(upper_pixels)
    edges = get_all_edges(sorted_pixels)
    result.extend(edges)  # Extend result with edges

# You don't need to flatten the result if each edge is already a list of coordinates
for edge in result:
    coordinates_array = np.array(edge)

    # If you need to apply a rotation
    rotation_matrix = np.array([[-1, 0], [0, -1]])  # Modify as per your requirement
    rotated_coordinates = np.dot(coordinates_array, rotation_matrix)

    # Plotting
    plt.scatter(rotated_coordinates[:, 0], rotated_coordinates[:, 1], color="black", s=0.1)

plt.show()
print(len(result))