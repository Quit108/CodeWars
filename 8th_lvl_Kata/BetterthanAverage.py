class_points = [70, 80, 90]
your_points = 85

def better_than_average(class_points, your_points):
    return True if your_points > sum(class_points) / len(class_points) else False

print(better_than_average(class_points, your_points))