from flask import Flask, render_template, jsonify, request
import static.controller.controller as controller

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

@app.route("/send-date", methods=['POST'])
def send_date_api():
    return controller.send_date()

if __name__ == '__main__':
   app.run()
