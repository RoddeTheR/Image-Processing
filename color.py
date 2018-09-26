import colorsys
import numpy as np
from collections import namedtuple


_color = namedtuple('Color', ['r', 'g', 'b'])


class Color(_color):

	# @property
	# def rgb(self):
	# 	return (int(self.r * 255), int(self.g * 255), int(self.b * 255))

	# @property
	# def rgba(self):
	# 	return (int(self.r * 255), int(self.g * 255), int(self.b * 255), int(self.a * 255))

	# @property
	# def rgb_255(self):
	# 	return (self.r, self.g, self.b)

	# @property
	# def rgba_255(self):
	# 	return (self.r, self.g, self.b, self.a)

	def __add__(self, other):
		return Color(self.r + other.r, self.g + other.g, self.b + other.b)

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		return Color(self.r - other.r, self.g - other.g, self.b - other.b)

	def __rsub__(self, other):
		return self.__sub__(other)

	def __mul__(self, other):
	 	return Color(self.r * other, self.g * other, self.b * other)

	def __rmul__(self, other):
		return self.__mul__(other)

	# Need to check if this is needed anymore
	# def __str__(self):
	#  	return f"RGB({self.r},{self.g},{self.b})"

	# __repr__ = __str__


def from_rgb(r, g, b):
	# def clamp(x): return max(0, min(x, 1))
	# return Color(clamp(r), clamp(g), clamp(b))
	return Color(r, g, b)


def from_rgb_255(r, g, b):
	return Color(r/255, g/255, b/255)


def from_hsl(h, s, l):
	return Color(*colorsys.hls_to_rgb(h, l, s))


def from_hex(hex_val):
	# Tack Internet
	hex_val = hex_val.lstrip('#')
	return from_rgb(*(int(hex_val[i:i+2], 16)/255 for i in (0, 2, 4)))
