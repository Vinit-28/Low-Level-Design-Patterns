# Importing Dependencies #
from Observable import *
from Observer import *


# Declaraing Objects #
iphoneObservable = ProductObservableImp()
mobileAlertObserver = MobileAlertProductObserver(contact='9680018733')
emailAlertObserver = EmailAlertProductObserver(email='observer@gmail.com')

# Invoking Functionalities #
iphoneObservable.addProudctObserver(mobileAlertObserver)
iphoneObservable.setStockCount(stockCount=100)
iphoneObservable.setStockCount(stockCount=0)
iphoneObservable.addProudctObserver(emailAlertObserver)
iphoneObservable.setStockCount(stockCount=10)
