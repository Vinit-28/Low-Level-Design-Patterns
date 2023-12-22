from Observer import IProductObserver
from Observable import IProductObservable


class EmailAlertProductObserver(IProductObserver):
    def __init__(self, email) -> None:
        super().__init__()
        self.email = email
    
    def alert(self, productObservable:IProductObservable):
        message = f"Product is in Stock now with qty {productObservable.getStockCount()}"
        self.sendEmail(message)

    def sendEmail(self, message):
        print(f"Email with message '{message}' sent to {self.email}.")