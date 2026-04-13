from flask import Flask, request, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://us3.platform.insight.rapid7.com/1/webhooks/6e244ee7-11b8-4c7e-8402-460d54b0a43d"

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/send', methods=['POST'])
def send():
    email = request.form.get("email")

    payload = {
        "input_data": [
            {
                "emails": email
            }
        ]
    }

    response = requests.post(WEBHOOK_URL, json=payload)

    return f"Request sent! Status: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)