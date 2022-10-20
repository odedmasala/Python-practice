from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [{"id": 1, "model": "Mazda"}, {"id": 2, "model": "Toyoda"}, {"id": 3, "model": "BNW"}, {
    "id": 4, "model": "Mercedes"}, {"id": 5, "model": "honda"}, {"id": 6, "model": "nissan"}]


@app.route("/cars", methods=["GET"])
def get_all_cars():
    return jsonify(cars)


PORT = 8000
none = None
app.run("localhost", int(PORT))
# (method) run: (host: str | None = None, port: int | None = None, debug: bool | None = None, load_dotenv: bool = True, **options: Any) -> None
