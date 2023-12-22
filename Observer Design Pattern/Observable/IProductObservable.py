from abc import ABCMeta, abstractmethod
from Observer.IProductObserver import IProductObserver

class IProductObservable(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.productObservers = list()
        self.stockCount = 0
    
    @abstractmethod
    def addProudctObserver(self, productObserver:IProductObserver):
        pass

    @abstractmethod
    def removeProductObserver(self, productObserver:IProductObserver):
        pass

    @abstractmethod
    def setStockCount(self, stockCount):
        pass

    @abstractmethod
    def getStockCount(self):
        pass
    
    @abstractmethod
    def notifyProductObservers(self):
        pass