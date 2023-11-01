from flask import Flask, render_template, jsonify, request
import requests
import json

app = Flask(__name__, static_folder='static')

azure_ml_endpoint = 'http://52.224.185.249:80/api/v1/service/deployment-2/score'
api_key = 'QY3IWPTMoJu2gcDIYM81oweqzSTlomXd'

headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get_text", methods=['GET'])
def get_text():
    return jsonify(text="This is some text from the server")

@app.route("/api/connect", methods=['POST'])
def connect():

    # Prepare the data for Azure ML
    data =  {
  "Inputs": {
    "input1": [
      {
        "symboling": 3,
        "normalized-losses": 1.0,
        "make": "alfa-romero",
        "fuel-type": "gas",
        "aspiration": "std",
        "num-of-doors": "two",
        "body-style": "convertible",
        "drive-wheels": "rwd",
        "engine-location": "front",
        "wheel-base": 88.6,
        "length": 168.8,
        "width": 64.1,
        "height": 48.8,
        "curb-weight": 2548,
        "engine-type": "dohc",
        "num-of-cylinders": "four",
        "engine-size": 130,
        "fuel-system": "mpfi",
        "bore": 3.47,
        "stroke": 2.68,
        "compression-ratio": 1.0,
        "horsepower": 1.0,
        "peak-rpm": 1.0,
        "city-mpg": 21,
        "highway-mpg": 27,
        "price": 1.0
      },
      {
        "symboling": 3,
        "normalized-losses": 1.0,
        "make": "alfa-romero",
        "fuel-type": "gas",
        "aspiration": "std",
        "num-of-doors": "two",
        "body-style": "convertible",
        "drive-wheels": "rwd",
        "engine-location": "front",
        "wheel-base": 88.6,
        "length": 168.8,
        "width": 64.1,
        "height": 48.8,
        "curb-weight": 2548,
        "engine-type": "dohc",
        "num-of-cylinders": "four",
        "engine-size": 130,
        "fuel-system": "mpfi",
        "bore": 3.47,
        "stroke": 2.68,
        "compression-ratio": 1.0,
        "horsepower": 1.0,
        "peak-rpm": 1.0,
        "city-mpg": 21,
        "highway-mpg": 27,
        "price": 1.0
      },
      {
        "symboling": 1,
        "normalized-losses": 1.0,
        "make": "alfa-romero",
        "fuel-type": "gas",
        "aspiration": "std",
        "num-of-doors": "two",
        "body-style": "hatchback",
        "drive-wheels": "rwd",
        "engine-location": "front",
        "wheel-base": 94.5,
        "length": 171.2,
        "width": 65.5,
        "height": 52.4,
        "curb-weight": 2823,
        "engine-type": "ohcv",
        "num-of-cylinders": "six",
        "engine-size": 152,
        "fuel-system": "mpfi",
        "bore": 2.68,
        "stroke": 3.47,
        "compression-ratio": 1.0,
        "horsepower": 1.0,
        "peak-rpm": 1.0,
        "city-mpg": 19,
        "highway-mpg": 26,
        "price": 1.0
      },
      {
        "symboling": 2,
        "normalized-losses": 1.0,
        "make": "audi",
        "fuel-type": "gas",
        "aspiration": "std",
        "num-of-doors": "four",
        "body-style": "sedan",
        "drive-wheels": "fwd",
        "engine-location": "front",
        "wheel-base": 99.8,
        "length": 176.6,
        "width": 66.2,
        "height": 54.3,
        "curb-weight": 2337,
        "engine-type": "ohc",
        "num-of-cylinders": "four",
        "engine-size": 109,
        "fuel-system": "mpfi",
        "bore": 3.19,
        "stroke": 3.4,
        "compression-ratio": 1.0,
        "horsepower": 1.0,
        "peak-rpm": 1.0,
        "city-mpg": 24,
        "highway-mpg": 30,
        "price": 1.0
      },
      {
        "symboling": 2,
        "normalized-losses": 1.0,
        "make": "audi",
        "fuel-type": "gas",
        "aspiration": "std",
        "num-of-doors": "four",
        "body-style": "sedan",
        "drive-wheels": "4wd",
        "engine-location": "front",
        "wheel-base": 99.4,
        "length": 176.6,
        "width": 66.4,
        "height": 54.3,
        "curb-weight": 2824,
        "engine-type": "ohc",
        "num-of-cylinders": "five",
        "engine-size": 136,
        "fuel-system": "mpfi",
        "bore": 3.19,
        "stroke": 3.4,
        "compression-ratio": 1.0,
        "horsepower": 1.0,
        "peak-rpm": 1.0,
        "city-mpg": 18,
        "highway-mpg": 22,
        "price": 1.0
      }
    ]
  },
  "GlobalParameters": {}
}
    # Convert data to JSON
    body = json.dumps(data)

    # Send request to Azure ML
    response = requests.post(azure_ml_endpoint, data=body, headers=headers)

    if response.status_code == 200:
        # Directly forward the response text
        text = response.text
        return jsonify(message="Success", text=text, success=True)
    else:
        return jsonify(message="Failed to get response from Azure ML", success=False)

if __name__ == '__main__':
   app.run()
