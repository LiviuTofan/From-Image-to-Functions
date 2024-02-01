import cv2
from Image import edge_detection
from Coordinates import pixels_coordinates, adjacent_pixels, get_upper_edge_pixels, sort_pixels_by_adjacency, get_all_edges
from Functions import rotate_points, functions
# Image path
img = cv2.imread("fata.jpg")

# Transform the image, black edges on white background and save it in final.png file
edge_detection(img)

pixel_coordinates = pixels_coordinates('final.png')

adjacent_pixels = adjacent_pixels(pixel_coordinates)

result = []
for edge in adjacent_pixels:
    uper_pixels = get_upper_edge_pixels(edge)
    sorted_pixels = sort_pixels_by_adjacency(uper_pixels)
    edges = get_all_edges(sorted_pixels)
    result.append(edges)

# Assuming result is a list of lists of lists (edges nested within edges for each adjacent_pixels)
flattened_result = [edge for edges_group in result for edge in edges_group]
points = rotate_points(flattened_result, 180)
functions(points)