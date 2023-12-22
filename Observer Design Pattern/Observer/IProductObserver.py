from abc import ABCMeta, abstractmethod
from Observable import IProductObservable


class IProductObserver(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def alert(self, productObservable:IProductObservable):
        pass