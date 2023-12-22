from Product import BaseProductClass


class ProductClass(BaseProductClass):
    def __init__(self) -> None:
        super().__init__()
    
    def getCost(self):
        return 1000