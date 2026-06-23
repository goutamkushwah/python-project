from flask import Flask, render_template, request

from length import convert_length
from weight import convert_weight
from temperature import convert_temperature

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/length", methods=["GET", "POST"])
def length():

    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert_length(value, from_unit, to_unit)
        print("Result:", result)

    return render_template("Length.html", result=result)


@app.route("/weight", methods=["GET", "POST"])
def weight():

    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert_weight(value, from_unit, to_unit)

    return render_template("Weight.html", result=result)


@app.route("/temperature", methods=["GET", "POST"])
def temperature():

    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert_temperature(value, from_unit, to_unit)

    return render_template("temprature.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)