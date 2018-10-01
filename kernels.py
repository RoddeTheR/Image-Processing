import numpy as np
from image import new_image
from scipy.signal import convolve2d, convolve
from distortions import extend_border, unpad


def apply_kernel(image, kernel):
	pad_width = kernel.shape[0]//2 + 1
	im = extend_border(image, pad_width)
	im = convolve(im, kernel[:, :, None], mode="same")
	return unpad(im, pad_width)


def _apply_kernel(image, kernel):
	im = new_image(image.shape[1], image.shape[0])
	im[:, :, 0] = convolve2d(image[:, :, 0], kernel, mode="same", boundary='symm')
	im[:, :, 1] = convolve2d(image[:, :, 1], kernel, mode="same", boundary='symm')
	im[:, :, 2] = convolve2d(image[:, :, 2], kernel, mode="same", boundary='symm')
	return im


def box_blur(size):
	kernel = np.ones((size, size))
	return kernel / np.sum(kernel)


def gaussian_blur(sigma):
	y, x = np.ogrid[-3*sigma:3*sigma+1, -3*sigma:3*sigma+1]
	return 1 / (2 * np.pi * np.square(sigma) * np.exp((np.square(x) + np.square(y))/(2*np.square(sigma))))


# kernel = np.array([[0,0,0],[0,0,0],[0,0,0]])
