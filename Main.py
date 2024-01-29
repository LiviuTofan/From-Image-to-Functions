import cv2
from Image import edge_detection
from Coordinates import pixels_coordinates, adjacent_pixels

# Image path
img = cv2.imread("fata.jpg")

# Transform the image, black edges on white background and save it in final.png file
edge_detection(img)

# Save all [x, y] coordinates of each black pixel from sketch
coordinates = pixels_coordinates('final.png')

# Divide edges like contours by finding adjacent pixels which create lines
data, counter = adjacent_pixels(coordinates)

for function in data:
    print(function)


