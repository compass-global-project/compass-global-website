from flask import Flask, render_template, jsonify, request
import requests
import json
import static.controller.controller as controller

from urllib.request import urlopen
import json

import pandas as pd

import plotly.express as px

app = Flask(__name__, static_folder="static")

azure_ml_endpoint = "http://52.224.185.249:80/api/v1/service/deployment-2/score"
api_key = "QY3IWPTMoJu2gcDIYM81oweqzSTlomXd"

headers = {"Content-Type": "application/json", "Authorization": ("Bearer " + api_key)}

df = pd.read_csv("data.csv")
import geojson


with open("india.geojson") as f:
    gj = geojson.load(f)

fig = px.choropleth(
    df,
    geojson=gj,
    featureidkey="properties.ST_NM",
    locations="state",
    color="active cases",
    color_continuous_scale="Reds",
)

fig.update_geos(fitbounds="locations", visible=False)


@app.route("/heatmap")
def heat_map():
    fig.show()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_text", methods=["GET"])
def get_text():
    return jsonify(text="This is some text from the server")


@app.route("/send-date", methods=["POST"])
def send_date_api():
    return controller.send_date()


if __name__ == "__main__":
    app.run()
