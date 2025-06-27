"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = None

    def __init__(self, weight, fuel, fuel_consumption, max_cargo:int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def __str__(self):
        return f"{super().__str__()} max_cargo={self.max_cargo} cargo={self.cargo}"

    def load_cargo(self, new_cargo: int):
        cargo = self.cargo + new_cargo
        if cargo > self.max_cargo:
            raise CargoOverload
        self.cargo = cargo

    def remove_all_cargo(self) -> int:
        result = self.cargo
        return result