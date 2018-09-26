from PIL import Image
import numpy as np

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


def load_image(name):
	im = Image.open(name)
	return np.array(im).astype('float32') / 255


def save_image(image, name="tmp.png"):
	arr = np.clip(image, 0, 1) * 255
	im = Image.fromarray(arr.astype('uint8'))
	im.save(name)


def new_image(width, height, color=(0, 0, 0)):
	return np.full((height, width, 3), color, dtype='float32')
