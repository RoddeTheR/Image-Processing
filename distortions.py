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
	y_disp = (y_displacement, 0) if y_displacement > 0 else (0, -y_displacement)
	x_disp = (x_displacement, 0) if x_displacement > 0 else (0, -x_displacement)
	im = np.pad(layer, (y_disp, x_disp), mode='edge')
	im = im[:-y_displacement, :] if y_displacement > 0 else im[-y_displacement:, :]
	return im[:, :-x_displacement] if x_displacement > 0 else im[:, -x_displacement:]
