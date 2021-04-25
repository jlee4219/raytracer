import numpy as np

from src.vec3 import vec3

def write_color(data, y, x, color):
    data[y][x] = [color.r(), color.g(), color.b()]