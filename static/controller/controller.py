from flask import jsonify, request
import requests
import json
import datetime

azure_ml_endpoint = 'http://52.224.185.249:80/api/v1/service/deployment-2/score'
api_key = 'QY3IWPTMoJu2gcDIYM81oweqzSTlomXd'

headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}


def send_date():
    data = request.get_json()

    if 'startDate' not in data or 'endDate' not in data:
        return jsonify(message="Both start and end dates must be provided", success=False)

    startDate_str = data['startDate']
    endDate_str = data['endDate']

    # Convert data to JSON
    body = json.dumps(data)

    # Send request to Azure ML
    response = requests.post(azure_ml_endpoint, data=body, headers=headers)

    if response.status_code == 200:
        # Directly forward the response text
        text = response.text
        return jsonify(message="Success", text=text, success=True)
    else:
        return jsonify(message="Failed to get response from Azure ML", success=False, data=data, response=response.text)