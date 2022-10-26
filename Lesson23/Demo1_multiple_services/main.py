from flask import Flask
from flask_cors import CORS

from routers.usersRouter import users
from routers.productsRouter import products
# Create an application
app = Flask(__name__)

CORS(app)
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(products, url_prefix='/products')
app.run("localhost", 8000)