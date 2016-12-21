import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('test.jpg')

print('This image is: ',type(image), 'with dimensions:', image.shape)

y_size          = image.shape[0]
x_size          = image.shape[1]

image_copy      = np.copy(image)

red_threshold   = 200
green_threshold = 200
blue_threshold  = 200
rgb_threshold   = [red_threshold, green_threshold, blue_threshold]


# Identify pixels below the threshold
thresholds = (image[:,:,0] < rgb_threshold[0]) | (image[:,:,1] < rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])
image_copy[thresholds] = [0,0,0]

# Display the image                 
plt.imshow(image_copy)
plt.show()
