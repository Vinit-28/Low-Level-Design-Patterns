from Observable import IProductObservable
from Observer import IProductObserver

class ProductObservableImp(IProductObservable):
    def __init__(self) -> None:
        super().__init__()
    
    def addProudctObserver(self, productObserver:IProductObserver):
        self.productObservers.append(productObserver)
    
    def removeProductObserver(self, productObserver:IProductObserver):
        self.productObservers.remove(productObserver)
    
    def setStockCount(self, stockCount):
        if self.stockCount == 0 and stockCount > 0:
            self.stockCount = stockCount
            self.notifyProductObservers()
        else:
            self.stockCount = stockCount
    
    def getStockCount(self):
        return self.stockCount

    def notifyProductObservers(self):
        for productObserver in self.productObservers:
            productObserver.alert(self)