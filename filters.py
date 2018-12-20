import numpy as np
from constants import R, G, B
from image import new_image
from math import sqrt
from kmeans import k_means
from distortions import displace_layer


def grayscale(image, weights=(0.33, 0.33, 0.33)):
	# return  np.dot(arr[..., :3], [0.3, 0, 0.3])
	return np.dot(image, weights)


def grayscale_2(image):
	return (np.amax(image, axis=2) + np.amin(image, axis=2))/2


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


def contrast(image, mu_p, sigma_p):
	mu = np.mean(image, axis=(0, 1))
	P = np.sum(np.square(image), axis=(0, 1))
	n = image.shape[0] * image.shape[1]
	sigma = np.sqrt((P - n * np.square(mu))/(n-1))
	return mu_p + (sigma_p / sigma) * (image - mu)


def closest_color(image, colors):
	distances = np.sum(np.square(image[:, :, None, :] - colors), axis=3)
	indices = np.argmin(distances, axis=2)
	return colors[indices]


def cluster_color(image, clusters, **kwargs):
	original_shape = image.shape
	data = image.reshape((-1, 3))
	averages, classes = k_means(clusters, data, **kwargs)

	image = averages[classes]
	return image.reshape(original_shape)


def closest_lightness(image, colors):
	colors_l = (np.amax(colors, axis=1) + np.amin(colors, axis=1))/2
	image_l = (np.amax(image, axis=2) + np.amin(image, axis=2))/2
	distances = np.abs(image_l[:, :, None] - colors_l)
	indices = np.argmin(distances, axis=2)
	return colors[indices]


def chromatic_aberration(image, displacement):
	im = np.empty(image.shape)
	im[R] = displace_layer(image[R], 2*displacement//3, -2*displacement//3)
	im[G] = displace_layer(image[G], -displacement//6, displacement)
	im[B] = displace_layer(image[B], -displacement, displacement//3)
	return im
