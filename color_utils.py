from color import Color, from_rgb, from_hsl
from random import random, uniform


def random_color():
		return from_rgb(random(), random(), random())


def random_from_hls(h_min=0, h_max=1, s_min=0, s_max=1, l_min=0, l_max=1):
	return from_hsl(uniform(h_min, h_max), uniform(s_min, s_max), uniform(l_min, l_max))
	# return from_hsl(h_min + (h_max - h_min) * random(), s_min + (s_max - s_min) * random(), l_min + (l_max - l_min) * random())


def random_pastel_color():
		return random_from_hls(s_min=0.5, s_max=0.95, l_min=0.45, l_max=1)
