from PIL import Image
from moviepy.editor import ImageSequenceClip
import numpy as np
import itertools

# class Image:
# 	count = 0

# 	def __init__(self, width=500, height=500):
# 		self.width = width
# 		self.height = height
# 		self.image = PILImage.new('RGB', (self.width, self.height), 0xffffff)
# 		self.pixels = self.image.load()
# 		self.draw = PILImageDraw.Draw(self.image)

# 	def save(self, name=None):
# 		# Makes it possible to keep spamming save and not overriding the images
# 		if name == None:
# 			name = f"temp-{Image.count}.png"

# 		self.image.save(name)
# 		Image.count += 1

# 	def draw_rectangle(self, cord1, cord2, colour_fill=None, colour_outline=None):
# 		self.draw.rectangle([cord1, cord2],
# 		                    fill=colour_fill, outline=colour_outline)

# 	def draw_text(self, cord, text, font_size=20, font_name="Arial Bold", outline=False, color=(0, 0, 0), outline_color=(255, 255, 255)):
# 		font = PILImageFont.truetype(font_name, font_size)
# 		if outline:
# 			self.draw.text((cord[0]-1, cord[1]-1), text, outline_color, font=font)
# 			self.draw.text((cord[0]+1, cord[1]-1), text, outline_color, font=font)
# 			self.draw.text((cord[0]-1, cord[1]+1), text, outline_color, font=font)
# 			self.draw.text((cord[0]+1, cord[1]+1), text, outline_color, font=font)

# 		self.draw.text((cord[0], cord[1]), text, color, font=font)

# 	def __setitem__(self, key, item):
# 		self.pixels[key] = item

# 	def __getitem__(self, key):
# 		return self.pixels[index]


# SINGLE IMAGE
def load_image(name):
	im = Image.open(name)
	return np.array(im).astype('float32') / 255


def save_image(image, name="temp"):
	arr = np.clip(image, 0, 1) * 255
	im = Image.fromarray(arr.astype('uint8'))
	im.save(f"{name}.png")


def new_image(width, height, color=(0, 0, 0)):
	return np.full((height, width, 3), color, dtype='float32')


# UTILS
def clip_and_convert(image):
	return (np.clip(image, 0, 1) * 255).astype('uint8')


# MULTIPLE IMAGES
def make_image_array(function, image, **kwargs):
	params = [dict(zip(kwargs, x)) for x in itertools.product(*kwargs.values())]
	images = [clip_and_convert(function(image=image, **param)) for param in params]
	return images


def save_array_as_video(images, name="temp", fps=24):
	clip = ImageSequenceClip(images, fps=fps)
	clip.write_videofile(f"{name}.mp4", fps=fps, verbose=False)


def save_array_as_gif(images, name="temp", fps=24):
	clip = ImageSequenceClip(images, fps=fps)
	clip.write_gif(f"{name}.gif", fps=fps, verbose=False)
