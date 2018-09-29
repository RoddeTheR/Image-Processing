import numpy as np


def extend_border(image, pad_width):
    return np.pad(image, ((pad_width,), (pad_width,), (0,)), mode='edge')


def unpad(image, pad_width):
    return image[pad_width:-pad_width, pad_width:-pad_width, :]
