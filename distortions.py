import numpy as np


def extend_border(image, pad_width):
    return np.pad(image, ((pad_width,), (pad_width,), (0,)), mode='edge')


def unpad(image, pad_width):
    return image[pad_width:-pad_width, pad_width:-pad_width, :]


def wavy(image, amplitude, frequency=1, phase=0):
	y_dim, x_dim, _ = image.shape
	x = np.arange(x_dim)
	y = np.arange(y_dim)
	displacement = (amplitude * np.sin(frequency * (x - phase) / x_dim * 2 * np.pi)).astype(int)
	yy = np.clip(y[:, None] + displacement, 0, y_dim - 1)
	return image[yy, x]


def displace_layer(layer, x_displacement, y_displacement):
	y_dim, x_dim = layer.shape
	x = np.arange(x_dim) + x_displacement
	x = np.clip(x, 0, x_dim - 1)
	y = np.arange(y_dim) + y_displacement
	y = np.clip(y[:, None], 0, y_dim - 1)
	return layer[y, x]
