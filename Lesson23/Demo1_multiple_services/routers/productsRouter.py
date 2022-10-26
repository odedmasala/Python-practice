from flask import Blueprint, jsonify
from BLL.productsBLL import ProductsBLL

products_BLL = ProductsBLL()

products = Blueprint('products', __name__)


# Get all products
@products.route("/", methods=['GET'])
def get_all_products():
    products = products_BLL.get_all_products()
    return products

