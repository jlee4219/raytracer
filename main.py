import matplotlib
import matplotlib.image
import numpy as np
import time

from src.ray import Ray
from src.sphere import Sphere
from src.vec3 import Vec3
from src.util import write_color, vec_where, IMAGE_WIDTH, ASPECT_RATIO

VIEWPORT_HEIGHT = 2
CONST_BLUE = 0.25
MAX_COLOR = 255

def ray_color(r):
    sphere = Sphere(Vec3(data = (0., 0., -1.)), 0.5)
    hits = sphere.hit(r, 0, 100000000)
    colors = (hits.normal.normalized() + Vec3(data = (1., 1., 1.))) * .5
    t = 0.5 * (r.direction.normalized().y() + 1.0)
    sky = Vec3(data = (1., 1., 1.)) * (1. - t) + Vec3(data = (0.5, 0.7, 1.0)) * t
    return vec_where(hits.t > 0, colors, sky)

if __name__ == '__main__':
    start = time.time()
    # Image
    image_height = int(IMAGE_WIDTH / ASPECT_RATIO)
    out_shape = (image_height, IMAGE_WIDTH, 3)
    data = np.zeros(shape=out_shape)

    # Camera
    viewport_width = ASPECT_RATIO * VIEWPORT_HEIGHT
    focal_length = 1
    origin = Vec3(data = (0., 0., 0.))
    horizontal = Vec3(data = (viewport_width, 0., 0.))
    vertical = Vec3(data = (0., VIEWPORT_HEIGHT, 0.))
    lower_left_corner = origin - horizontal / 2 - vertical / 2

    x = np.tile(np.linspace(lower_left_corner.x(), lower_left_corner.x() + viewport_width, IMAGE_WIDTH), image_height)
    y = np.repeat(np.linspace(lower_left_corner.y(), lower_left_corner.y() + VIEWPORT_HEIGHT, image_height), IMAGE_WIDTH)
    uv = Vec3(data = (x, y, -focal_length))

    r = Ray(origin, uv - origin)
    color = ray_color(r)

    for y in range(image_height):
        for x in range(IMAGE_WIDTH):
            u = x / IMAGE_WIDTH
            v = (image_height - y) / image_height
            write_color(data, y, x, color)

    matplotlib.image.imsave('out.png', data)
    print(f"Finished in {time.time() - start} seconds")
