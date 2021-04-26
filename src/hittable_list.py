import numpy as np
from src.hittable import Hittable, HitRecord
from src.ray import Ray
from src.util import vec_where

class HittableList(Hittable):
    def __init__(self, hittable_list = []):
        self.hittable_list = hittable_list

    def add(self, object):
        self.hittable_list.append(object)

    def clear(self):
        self.hittable_list = []

    def hit(self, r: Ray, t_min, t_max) -> HitRecord:
        record = None
        closest_so_far = t_max
        for hittable in self.hittable_list:
            new_record = hittable.hit(r, t_min, closest_so_far)

            if record:
                record.t = np.where((new_record.t < closest_so_far), new_record.t, record.t)
                record.normal = vec_where((new_record.t < closest_so_far), new_record.normal, record.normal)
                record.front_face = np.where((new_record.t < closest_so_far), new_record.front_face, record.front_face)
                record.p = vec_where((new_record.t < closest_so_far), new_record.p, record.p)
            else:
                record = new_record

            closest_so_far = record.t

        # TOD (Jefferson) moved this from sphere, might need to move back?
        record.set_face_normal(r, record.normal)
        return record