import numpy as np


def grayscale(image, weights=(0.33, 0.33, 0.33)):
	# return  np.dot(arr[..., :3], [0.3, 0, 0.3])
	return np.dot(image, weights)
