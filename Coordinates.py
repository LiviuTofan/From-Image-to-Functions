from PIL import Image

# Function to save in a list, sublists with white pixels coordinates, on black background [x, y]
def pixels_coordinates(image):
    coordinates = []
    with Image.open(image) as img:
        width, height = img.size
        img = img.convert('RGB')
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                if (r, g, b) != (0, 0, 0):  # Correct comparison with black
                    coordinates.append([x, y])

    return coordinates


# Function to save in lists all sublists with coordinates of adjacent pixels (horizontally, vertically and diagonally), using BFS algorithm for graphs
def adjacent_pixels(coordinates):
    counter = 0 # To count how many edges image has
    edges = []

    while coordinates:
        queue = [coordinates.pop(0)] # First pixel for checking will be first from coordinates list, and in the same time delete it from coordinates
        adjacent_pairs = []

        while queue:
            x1, y1 = queue.pop(0) # x1 and y1 are coordinates from first piexl from queue, and in the same time delete it from queue
            adjacent_pairs.append([x1, y1]) # add it adjacent_pairs, like first pixel from the edge

            for i in reversed(range(len(coordinates))): # Reverese to don't mess up indexes
                x2, y2 = coordinates[i]
                if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1: # Check if pixels are adjacent
                    queue.append(coordinates.pop(i)) # If adjacent pixels, delete pixel from coordinates and add it to queue, to check further

        counter += 1
        edges.append(adjacent_pairs)
    return edges, counter
