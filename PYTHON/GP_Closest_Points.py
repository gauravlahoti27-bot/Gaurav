import csv
import math

points = []

# Read CSV file
with open("points.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        points.append((float(row[0]), float(row[1]), float(row[2])))

min_dist = float('inf')
p1 = p2 = None

# Find closest pair
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        d = math.sqrt(
            (points[i][0] - points[j][0]) ** 2 +
            (points[i][1] - points[j][1]) ** 2 +
            (points[i][2] - points[j][2]) ** 2
        )

        if d < min_dist:
            min_dist = d
            p1, p2 = points[i], points[j]

# Output
print("Closest Points:", p1, "and", p2)
print("Distance:", round(min_dist, 4))