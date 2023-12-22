# Importing Dependencies #
from Product import *
from Features import *


# Creating Objects #
baseProduct = ProductClass()

# Invoking Functionalities #
print("Base Product Cost:", baseProduct.getCost())
print("Base Product + Feature A Cost:", FeatureA(baseProduct).getCost())
print("Base Product + Feature A + Feature B Cost:", FeatureB(FeatureA(baseProduct)).getCost())
print("Base Product + Feature A + Feature B + Feature C Cost:", FeatureC(FeatureB(FeatureA(baseProduct))).getCost())