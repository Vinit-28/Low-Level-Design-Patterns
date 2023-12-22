from Observer import IProductObserver
from Observable import IProductObservable


class MobileAlertProductObserver(IProductObserver):
    def __init__(self, contact) -> None:
        super().__init__()
        self.contact = contact
    
    def alert(self, productObservable:IProductObservable):
        message = f"Product is in Stock now with qty {productObservable.getStockCount()}"
        self.sendSMS(message)

    def sendSMS(self, message):
        print(f"Message '{message}' sent to {self.contact}.")