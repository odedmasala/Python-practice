import os
import sys
import json



class ProductsBLL:
    def __init__(self):

        self.__path = os.path.join(sys.path[0], 'data\products.json')

    def get_all_products(self):

        with open(self.__path, 'r') as f:
            data = json.load(f)
        return data

p1 = ProductsBLL()
print(p1.get_all_products())