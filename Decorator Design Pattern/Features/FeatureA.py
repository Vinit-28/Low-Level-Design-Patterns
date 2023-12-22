from Features import BaseFeatureClass
from Product import BaseProductClass


class FeatureA(BaseFeatureClass):
    def __init__(self, baseProduct: BaseProductClass) -> None:
        super().__init__(baseProduct)
    
    def getCost(self):
        return 100 + self.baseProduct.getCost()