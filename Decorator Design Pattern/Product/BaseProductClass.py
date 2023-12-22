from abc import ABCMeta, abstractmethod


class BaseProductClass(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def getCost(self):
        pass