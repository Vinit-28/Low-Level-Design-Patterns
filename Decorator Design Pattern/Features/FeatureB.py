from Features import BaseFeatureClass
from Product import BaseProductClass


class FeatureB(BaseFeatureClass):
    def __init__(self, baseProduct: BaseProductClass) -> None:
        super().__init__(baseProduct)
    
    def getCost(self):
        return 200 + self.baseProduct.getCost()