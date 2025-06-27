"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self, message="Fuel level is too low."):
        self.message = message
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    def __init__(self, message="Not enough fuel for this operation."):
        self.message = message
        super().__init__(self.message)

class CargoOverload(Exception):
    def __init__(self, message="Cargo weight exceeds the maximum capacity."):
        self.message = message
        super().__init__(self.message)