from Features import BaseFeatureClass
from Product import BaseProductClass


class FeatureC(BaseFeatureClass):
    def __init__(self, baseProduct: BaseProductClass) -> None:
        super().__init__(baseProduct)
    
    def getCost(self):
        return 300 + self.baseProduct.getCost()