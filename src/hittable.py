from src.ray import Ray
from src.vec3 import Vec3

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class HitRecord:
    p: Vec3
    normal: Vec3
    t :float

class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, t_min: float, t_max: float) -> HitRecord:
        pass