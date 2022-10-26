from flask import Flask
import json
from bson import ObjectId

from routers.personsRouter import persons

class JSONencoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)



# Create app
app = Flask(__name__)

app.json_encoder = JSONencoder

app.register_blueprint(persons, url_prefix="/persons")

app.run("localhost", 8000)