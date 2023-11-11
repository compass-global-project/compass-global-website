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


@app.route("/heatmap")
def heat_map():
    df = pd.read_csv(
        "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv"
    )

    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey="properties.ST_NM",
        locations="state",
        color="active cases",
        color_continuous_scale="Reds",
    )

    fig.update_geos(fitbounds="locations", visible=False)
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
