from abc import ABCMeta, abstractmethod


# Strategies #
# Abstract Class For WheelerStrategies #
class WheelerStrategy(metaclass=ABCMeta):
    @abstractmethod
    def getWheels(self):
        pass

# Two Wheeler Strategy #
class TwoWheelerStrategy(WheelerStrategy):
    def getWheels(self):
        return 2


# Four Wheeler Strategy #
class FourWheelerStrategy(WheelerStrategy):
    def getWheels(self):
        return 4



# Vehicle Base Class #
class Vehicle():
    def __init__(self, wheelerStrategy: WheelerStrategy):
        self.wheelerStrategy = wheelerStrategy
        
    def getWheels(self):
        return self.wheelerStrategy.getWheels()


# Vehicle Child Classes #
# Bike Vehicle Class #
class Bike(Vehicle):
    def __init__(self):
        super().__init__(TwoWheelerStrategy())


# Scooty Vehicle Class
class Scooty(Vehicle):
    def __init__(self):
        super().__init__(TwoWheelerStrategy())


# Car Vehicle Class #
class Car(Vehicle):
    def __init__(self):
        super().__init__(FourWheelerStrategy())


# Scooty Vehicle Class
class Bus(Vehicle):
    def __init__(self):
        super().__init__(FourWheelerStrategy())



# Using Classes #
lstOfVehicles = [
    Bike(),
    Bus(),
    Car(),
    Scooty(),
]

for vehicle in lstOfVehicles:
    print(vehicle.getWheels())