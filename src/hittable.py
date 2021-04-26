import numpy as np

from src.ray import Ray
from src.util import vec_where
from src.vec3 import Vec3

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class HitRecord:
    p: Vec3
    t: np.array
    normal: Vec3 = Vec3(data=(0., 0., 0.))
    front_face: np.array = None

    def set_face_normal(self, r: Ray):
        self.front_face = r.direction.dot(self.normal)
        self.normal = vec_where(self.front_face, self.normal, self.normal * -1.)

class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, t_min, t_max) -> HitRecord:
        pass