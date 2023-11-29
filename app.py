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

app = Flask(__name__, static_folder="static")

azure_ml_endpoint = "http://52.224.185.249:80/api/v1/service/deployment-2/score"
api_key = "QY3IWPTMoJu2gcDIYM81oweqzSTlomXd"

headers = {"Content-Type": "application/json", "Authorization": ("Bearer " + api_key)}

df = pd.read_csv("data.csv")


with open("india.geojson") as f:
    gj = geojson.load(f)


#@app.route("/")
def v2():
    fig = px.choropleth_mapbox(
        df,
        geojson=gj,
        featureidkey="properties.ST_NM",
        locations="state",
        color="active cases",
        color_continuous_scale="Reds",
        mapbox_style="carto-positron",
        zoom=3,
        center={"lat": 20.5937, "lon": 78.9629},  # Center on India
        opacity=0.5,
        labels={"active cases": "Active Cases"},
    )

    fig.update_layout(
        autosize=True,
        margin=dict(t=0, b=0, l=0, r=0),
        paper_bgcolor="rgba(0,0,0,0)",  # Change this to your desired color
        plot_bgcolor="rgba(0,0,0,0)",  # Change this to your desired color
        coloraxis_colorbar=dict(
            tickfont=dict(color="white"),  # Change this to your desired color
            titlefont=dict(color="white"),  # Change this to your desired color
        ),
    )
    heatmap_html = pyo.plot(fig, output_type="div")
    return render_template("index.html", heatmap=heatmap_html)


@app.route("/")
def home():
    fig = px.choropleth_mapbox(
        df,
        geojson=gj,
        featureidkey="properties.ST_NM",
        locations="state",
        color="active cases",
        color_continuous_scale="Reds",
        mapbox_style="carto-positron",
        zoom=3,
        center={"lat": 20.5937, "lon": 78.9629},  # Center on India
        opacity=0.5,
        labels={"active cases": "Active Cases"},
    )

    fig.update_layout(
        autosize=True,
        margin=dict(t=0, b=0, l=0, r=0),
        paper_bgcolor="rgba(0,0,0,0)",  # Change this to your desired color
        plot_bgcolor="rgba(0,0,0,0)",  # Change this to your desired color
        coloraxis_colorbar=dict(
            tickfont=dict(color="white"),  # Change this to your desired color
            titlefont=dict(color="white"),  # Change this to your desired color
        ),
    )
    heatmap_html = pyo.plot(fig, output_type="div")
    return render_template("index.html", heatmap=heatmap_html)


@app.route("/get_text", methods=["GET"])
def get_text():
    return jsonify(text="This is some text from the server")


@app.route("/send-date", methods=["POST"])
def send_date_api():
    return controller.send_date()


if __name__ == "__main__":
    app.run()
