from flask import jsonify, request, render_template
import requests
import json
import datetime
import plotly.offline as pyo
import plotly.express as px
import geojson
import plotly.graph_objects as go
import pandas as pd

azure_ml_endpoint = "http://52.224.185.249:80/api/v1/service/deployment-2/score"
api_key = "QY3IWPTMoJu2gcDIYM81oweqzSTlomXd"

headers = {"Content-Type": "application/json", "Authorization": ("Bearer " + api_key)}


def send_date():
    data = request.get_json()

    # Convert data to JSON
    body = json.dumps(data)

    # Send request to Azure ML
    response = requests.post(azure_ml_endpoint, data=body, headers=headers)

    if response.status_code == 200:
        # Directly forward the response text
        text = response.text
        return jsonify(message="Success", text=text, success=True)
    else:
        return jsonify(
            message="Failed to get response from Azure ML",
            success=False,
            data=data,
            response=response.text,
        )


azure_ml_endpoint2 = "http://52.224.185.249:80/api/v1/service/regional/score"
api_key2 = "zLzYhtMvMoobZO32Qmfe8E1f7LRR1SIe"

headers2 = {"Content-Type": "application/json", "Authorization": ("Bearer " + api_key2)}

df = 0


def send_date_heatmap():
    data = request.get_json()

    # Convert data to JSON
    body = json.dumps(data)

    # Send request to Azure ML
    response = requests.post(azure_ml_endpoint2, data=body, headers=headers2)

    if response.status_code == 200:
        # Directly forward the response text
        text = response.text
        data = json.loads(text)
        length = len(data["Results"]["output1"])
        data = json.dumps(data["Results"]["output1"][length - 1])
        data = data.split(",")
        data = load_data(data)
        df = pd.DataFrame(data)
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        return render_chart(df)
        render_chart(df)
        return jsonify(message="Success", text=text, success=True)
    else:
        return jsonify(
            message="Failed to get response from Azure ML",
            success=False,
            data=data,
            response=response.text,
        )


def load_data(json):

    data = {
        "state": [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Delhi",
            "Goa",
            "Gujarat",
            "Haryana",
            "Himachal Pradesh",
            "Jammu & Kashmir",
            "Jharkhand",
            "Karnataka",
            "Kerala",
            "Madhya Pradesh",
            "Maharashtra",
            "Manipur",
            "Meghalaya",
            "Mizoram",
            "Nagaland",
            "Odisha",
            "Puducherry",
            "Punjab",
            "Rajasthan",
            "Sikkim",
            "Tamil Nadu",
            "Telangana",
            "Tripura",
            "Uttarakhand",
            "Uttar Pradesh",
            "West Bengal",
            "Andaman & Nicobar",
            "Chandigarh",
            "Dadra and Nagar Haveli and Daman and Diu",
            "scratch",
            "Ladakh",
        ],
        "price": [],
    }

    for x in json:
        item = x.split(":")
        price = item[1][1:]
        data["price"].append(price)

    for i in range(2):
        data["price"].pop()

    return data


def render_chart(df):
    mapbox_token = "pk.eyJ1IjoiYW5pc2hjZCIsImEiOiJjbG93MG0yNHEwMW9tMmtuYWYydTV5NXQzIn0.gbZ2kS7iaY3BKapisdMUTQ"

    with open("india.geojson") as f:
        gj = geojson.load(f)

    named_colorscales = px.colors.named_colorscales()

    colorscale = request.form.get(
        "colorscale", "Viridis"
    )  # Get the selected colorscale

    fig = go.Figure(
        data=go.Choroplethmapbox(
            geojson=gj,
            featureidkey="properties.ST_NM",
            locations=df.state,
            z=df["price"],
            colorscale=colorscale,  # Use the selected colorscale
            zmin=0,
            zmax=df["price"].max(),
            marker_line_width=0.5,  # Set line width
            marker_line_color="black",  # Set line color
            colorbar=dict(
                title="Rice Price",
            ),
        )
    )

    fig.update_layout(
        mapbox_style="light",
        mapbox_accesstoken=mapbox_token,
        mapbox_zoom=3,
        mapbox_center={"lat": 20.5937, "lon": 78.9629},  # Center on India
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
    )

    heatmap_html = pyo.plot(fig, output_type="div")
    return render_template(
        "index.html",
        heatmap=heatmap_html,
        colorscales=named_colorscales,
        selected_colorscale=colorscale,
    )
