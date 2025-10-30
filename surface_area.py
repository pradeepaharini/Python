import math

# Function to compute Euclidean distance between two 3D points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

# Function to compute the area of a triangle using Heron's formula
def heron_area(triangle):
    a = distance(triangle[0], triangle[1])
    b = distance(triangle[1], triangle[2])
    c = distance(triangle[2], triangle[0])
    s = (a + b + c) / 2  # Semi-perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Function to read an STL file and extract vertices
def read_stl(file_path):
    vertices = []

    with open(file_path, "r") as file:
        lines = file.readlines()  # Read file into a list of strings

    for line in lines:  # Go through each line in the file
        words = line.strip().split()  # Remove spaces and break the line into words
        
        if words[0].lower() == "vertex":  # If the line starts with "vertex"
            x, y, z = float(words[1]), float(words[2]), float(words[3])  # Convert to float
            vertices.append((x, y, z))  # Save the vertex as a set of 3D coordinates

    # Group every 3 vertices into a triangle using a loop instead of list comprehension
    triangles = []
    for i in range(0, len(vertices), 3):  # Step through every 3rd element
        triangles.append(vertices[i:i+3])  # Add a group of 3 vertices to triangles

    return triangles

# Upload STL file path
file_path = "/content/fan_volume 1 (1).stl"  # Path for uploaded file in Colab

# Read STL file and extract triangles
triangles = read_stl(file_path)

# Compute total surface area
total_area = sum(heron_area(tri) for tri in triangles)
print(f"Total Surface Area of STL: {total_area:.5f} square units")
