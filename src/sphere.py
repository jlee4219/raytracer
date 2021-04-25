import numpy as np

from src.hittable import Hittable, HitRecord
from src.ray import Ray
from src.vec3 import Vec3

class Sphere(Hittable):
    def __init__(self, center: Vec3, radius: float):
        self.center = center
        self.radius = radius

    def hit(self, r: Ray, t_min: float, t_max: float) -> HitRecord:
        oc = r.origin - self.center
        a = r.direction.squared_length()
        half_b = oc.dot(r.direction)
        c = oc.squared_length() - self.radius * self.radius
        discriminant = half_b * half_b - a * c
        root = (-half_b + np.sqrt(discriminant)) / a
        first_root = np.where((discriminant > 0) & (root > t_min) & (root < t_max), root, -1)
        root = (-half_b - np.sqrt(discriminant)) / a
        second_root = np.where((discriminant > 0) & (root > t_min) & (root < t_max), root, first_root)

        p = r.at(second_root)
        return HitRecord(t = second_root, p = p, normal = (p - self.center) / self.radius)
