import matplotlib
import matplotlib.image
import numpy as np
import time

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256
CONST_BLUE = 0.25
MAX_COLOR = 255

if __name__ == '__main__':
    out_shape = (IMAGE_HEIGHT, IMAGE_WIDTH, 3)
    data = np.zeros(shape=out_shape)

    for y in range(IMAGE_HEIGHT):
        for x in range(IMAGE_WIDTH):
            data[y][x] = [(IMAGE_HEIGHT - y) / IMAGE_HEIGHT, x / IMAGE_WIDTH, CONST_BLUE]

    matplotlib.image.imsave('out.png', data)
