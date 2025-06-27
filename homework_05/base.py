from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight = 1500 # kg
    started = False
    fuel = 40 # liters
    fuel_consumption = 7 # liters / 100 km

    def __init__(self, weight: float, fuel: int, fuel_consumption: float):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def __str__(self):
        return f"{self.__class__} weight={self.weight} fuel={self.fuel} fuel_consumption={self.fuel_consumption} started={self.started}"

    def start(self):
        if self.fuel <= 0:
            raise LowFuelError("Not enough fuel to start the vehicle.")
        if not self.started:
            self.started = True
        print("Vehicle started.")

    def move(self, distance: float):
        if not self.started:
            print("Vehicle is not started.")
            return
        fuel_needed = distance / 100 * self.fuel_consumption
        if fuel_needed > self.fuel:
            raise NotEnoughFuel("Not enough fuel to move the vehicle.")
        self.fuel -= fuel_needed
        print(f"Vehicle moved {distance} km.")
