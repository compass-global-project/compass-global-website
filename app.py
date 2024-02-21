from flask import Flask, render_template, jsonify, request
import requests
import json
import static.controller.controller as controller
from urllib.request import urlopen
import json
import pandas as pd
import plotly.offline as pyo
import plotly.express as px
import geojson
import plotly.graph_objects as go

app = Flask(__name__, static_folder="static")

azure_ml_endpoint = "http://52.224.185.249:80/api/v1/service/deployment-2/score"
api_key = "QY3IWPTMoJu2gcDIYM81oweqzSTlomXd"

headers = {"Content-Type": "application/json", "Authorization": ("Bearer " + api_key)}

df = pd.read_csv("data.csv")

mapbox_token = "pk.eyJ1IjoiYW5pc2hjZCIsImEiOiJjbG93MG0yNHEwMW9tMmtuYWYydTV5NXQzIn0.gbZ2kS7iaY3BKapisdMUTQ"

with open("india.geojson") as f:
    gj = geojson.load(f)

named_colorscales = px.colors.named_colorscales()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_text", methods=["GET"])
def get_text():
    return jsonify(text="This is some text from the server")


@app.route("/send-date", methods=["POST"])
def send_date_api():
    return controller.send_date()


@app.route("/send-heatmap-dates", methods=["POST"])
def send_heatmap_api():
    return controller.send_date_heatmap()


if __name__ == "__main__":
    app.run(debug=True)
