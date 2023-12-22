from abc import ABCMeta, abstractmethod
from Product import BaseProductClass


class BaseFeatureClass(BaseProductClass, metaclass=ABCMeta):
    def __init__(self, baseProduct:BaseProductClass) -> None:
        self.baseProduct = baseProduct