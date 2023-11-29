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

mapbox_token = 'pk.eyJ1IjoiYW5pc2hjZCIsImEiOiJjbG93MG0yNHEwMW9tMmtuYWYydTV5NXQzIn0.gbZ2kS7iaY3BKapisdMUTQ'

with open("india.geojson") as f:
    gj = geojson.load(f)

named_colorscales = px.colors.named_colorscales()

# Convert 'active cases' column to numeric
df['active cases'] = pd.to_numeric(df['active cases'], errors='coerce')

@app.route("/v2", methods=["GET", "POST"])
def v2():
    colorscale = request.form.get('colorscale', 'Viridis')  # Get the selected colorscale

    fig = go.Figure(data=go.Choroplethmapbox(
        geojson=gj, 
        featureidkey="properties.ST_NM",
        locations=df.state, 
        z=df['active cases'],
        colorscale=colorscale,  # Use the selected colorscale
        zmin=0, 
        zmax=df['active cases'].max(), 
        marker_line_width=0.5,  # Set line width
        marker_line_color="black",  # Set line color
        colorbar=dict(
            title='Active Cases',
            tickfont=dict(color='white'),
            titlefont=dict(color='white')
        )
    ))

    fig.update_layout(
        mapbox_style="light",
        mapbox_accesstoken=mapbox_token,
        mapbox_zoom=3,
        mapbox_center = {"lat": 20.5937, "lon": 78.9629},  # Center on India
        margin={"r":0,"t":0,"l":0,"b":0},
    )

    heatmap_html = pyo.plot(fig, output_type='div')
    return render_template("v2.html", heatmap=heatmap_html, colorscales=named_colorscales, selected_colorscale=colorscale)


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
    app.run(debug=True)
