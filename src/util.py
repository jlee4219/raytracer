import numpy as np

from src.vec3 import Vec3

IMAGE_WIDTH = 400
ASPECT_RATIO = 16.0 / 9.0

# TODO(Jefferson) do this with numpy reshaping functions instead
def write_color(data, y, x, colors, num_samples):
    index = (int(IMAGE_WIDTH / ASPECT_RATIO) - 1 - y) * IMAGE_WIDTH + x
    for color in colors:
        data[y][x] += [color[0][index], color[1][index], color[2][index]]

    data[y][x] /= num_samples

def vec_where(condition, vec1, vec2):
    x = np.where(condition, vec1.data[0], vec2.data[0])
    y = np.where(condition, vec1.data[1], vec2.data[1])
    z = np.where(condition, vec1.data[2], vec2.data[2])
    return Vec3(data = (x, y, z)) 