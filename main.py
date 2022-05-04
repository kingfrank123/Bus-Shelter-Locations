import tickets
from flask import Flask
from flask import render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/map.js")
def map():
    return send_from_directory('static', "map.js")


@app.route("/graph.js")
def graph():
    return send_from_directory('static', "graph.js")


@app.route("/tickets")
def data():
    return tickets.info("https://data.cityofnewyork.us/resource/t4f2-8md7.json")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
