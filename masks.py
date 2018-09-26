import numpy as np
import random


def circular_mask(image, center=None, radius=None, inside=True):
	y_length, x_length, _ = image.shape
	y, x = np.ogrid[:y_length, :x_length]

	if center is None:
		x_center, y_center = x_length / 2, y_length / 2
	else:
		x_center, y_center = center

	radius = radius or (y_length / 2)

	if inside:
		return ((x - x_center)**2 + (y - y_center)**2 <= radius ** 2)
	else:
		return ((x - x_center)**2 + (y - y_center)**2 > radius ** 2)


# SLOW
# TODO - FAST
def random_circles_mask(image, amount, padding=2, min_size=10, max_size=100):
	y_max, x_max, _ = image.shape
	# Origin selection
	points = [(random.uniform(0, x_max), random.uniform(0, y_max))
           for _ in range(amount)]
	point_sizes = [min_size for _ in range(amount)]

	# Size selection
	for i, point in enumerate(points):
		curr_max_size = max_size
		for j in range(amount):
			if j == i:
				continue
			distance = ((points[j][0] - point[0])**2 +
                            (points[j][1] - point[1])**2) ** (1/2)
			curr_max_size = min(curr_max_size, distance - point_sizes[j] - padding)
		point_sizes[i] = random.uniform(min_size, curr_max_size)

	# Mask creation
	mask = False
	for point, size in zip(points, point_sizes):
		mask |= circular_mask(image, center=(
		    point[0], point[1]), radius=size)
	return mask
