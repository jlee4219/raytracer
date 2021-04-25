import matplotlib
import matplotlib.image
import numpy as np
import time

from src.ray import ray
from src.vec3 import vec3
from src.util import write_color

IMAGE_WIDTH = 400
VIEWPORT_HEIGHT = 2
ASPECT_RATIO = [16., 9.]
CONST_BLUE = 0.25
MAX_COLOR = 255

def ray_color(r):
    t = 0.5 * (r.direction.normalized().y() + 1.0)
    return vec3(data = (1., 1., 1.)) * (1. - t) + vec3(data = (0.5, 0.7, 1.0)) * t

if __name__ == '__main__':
    aspect_ratio = ASPECT_RATIO[0] / ASPECT_RATIO[1]
    # Image
    image_height = int(IMAGE_WIDTH / aspect_ratio)
    out_shape = (image_height, IMAGE_WIDTH, 3)
    data = np.zeros(shape=out_shape)

    # Camera
    viewport_width = aspect_ratio * VIEWPORT_HEIGHT
    focal_length = 1
    origin = vec3(data = (0., 0., 0.))
    horizontal = vec3(data = (viewport_width, 0., 0.))
    vertical = vec3(data = (0., VIEWPORT_HEIGHT, 0.))
    lower_left_corner = origin - horizontal / 2 - vertical / 2 - vec3(data = (0, 0, focal_length))

    for y in range(image_height):
        for x in range(IMAGE_WIDTH):
            u = x / IMAGE_WIDTH
            v = (image_height - y) / image_height
            r = ray(origin, lower_left_corner + horizontal * u + vertical * v - origin)
            color = ray_color(r)
            write_color(data, y, x, color)

    matplotlib.image.imsave('out.png', data)
