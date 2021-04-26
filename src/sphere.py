import numpy as np

from src.hittable import Hittable, HitRecord
from src.ray import Ray
from src.util import vec_where
from src.vec3 import Vec3

class Sphere(Hittable):
    def __init__(self, center: Vec3, radius: float):
        self.center = center
        self.radius = radius

    def hit(self, r: Ray, t_min, t_max) -> HitRecord:
        oc = r.origin - self.center
        a = r.direction.squared_length()
        half_b = oc.dot(r.direction)
        c = oc.squared_length() - self.radius * self.radius
        discriminant = half_b * half_b - a * c
        root = (-half_b + np.sqrt(discriminant)) / a
        first_root = np.where((discriminant > 0) & (root > t_min) & (root < t_max), root, t_max)
        root = (-half_b - np.sqrt(discriminant)) / a
        second_root = np.where((discriminant > 0) & (root > t_min) & (root < t_max), root, first_root)

        p = vec_where(second_root < t_max, r.at(second_root), Vec3(data = (np.Inf, np.Inf, np.Inf)))
        rec = HitRecord(t = second_root, p = p)
        rec.normal = vec_where(second_root < t_max, (p - self.center) / self.radius, Vec3(data = (np.Inf, np.Inf, np.Inf)))
        return rec