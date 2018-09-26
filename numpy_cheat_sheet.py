import numpy as np
from image import load_image, save_image, new_image
from filters import grayscale
from constants import R, G, B

# arr is a numpy array Y * X * 3 of floats 0-1
image_array = load_image('test1.jpg')


# get size
y, x, three = image_array.shape

# OPERATIONS
# looping over all pixels SLOW SLOW
for y in range(image_array.shape[0]):
    for x in range(image_array.shape[1]):
    	image_array[y, x, 0] += 0.5
    	# same as above but worse
    	# image_array[y, x][0] += 0.5

# Applies * (1.2,1.2,1.2) to all pixels due to broadcasting FAST
image_array = image_array * (1.2, 1.2, 1.2)
# Same result same broadcasting
image_array *= 1.2


# SELECTION
# Slicing works(there are some cool tricks though)
image_array[100:200, 200:300, :] = 0

# Get all the red values (mutable)
image_array[R] = 0


# MASKS
# Creates an array(size of the original array)with True where the condition is true
r = image_array[R] <= 0.5

# Selects only the pixels where the condition is true
image_array[r]
# Red band of the pixels where the condition is true
image_array[r, 0] = 0


# save array to a image
save_image(image_array, "test1-out.png")
