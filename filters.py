import numpy as np
from constants import R, G, B
from image import new_image


def grayscale(image, weights=(0.33, 0.33, 0.33)):
	# return  np.dot(arr[..., :3], [0.3, 0, 0.3])
	return np.dot(image, weights)


def grayscale_2(image):
	max = np.maximum(np.maximum(image[R], image[G]), image[B])
	min = np.minimum(np.minimum(image[R], image[G]), image[B])
	return (max + min)/2


def blackwhite_dots(image):
	y_dim, x_dim, _ = image.shape
	random = np.random.uniform(size=[y_dim, x_dim])
	mask = random < grayscale_2(image)
	out = new_image(x_dim, y_dim)
	out[mask] = (1, 1, 1)
	return out


def rgb_dots(image):
	y_dim, x_dim, _ = image.shape
	probs = image / np.sum(image, axis=2)[:, :, None]
	probs[np.isnan(probs)] = 1/3
	random = np.random.uniform(size=[y_dim, x_dim])
	r_mask = random < probs[R]
	g_mask = random < probs[R] + probs[G]

	random = np.random.uniform(size=[y_dim, x_dim])
	w_mask = random < grayscale_2(image)

	out = new_image(x_dim, y_dim, (0, 0, 1))
	out[g_mask] = (0, 1, 0)
	out[r_mask] = (1, 0, 0)
	out[w_mask] = (1, 1, 1)
	return out
