from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE Bot Running"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    for event in data.get("events", []):

        if event.get("type") == "message":

            if event["message"]["type"] == "text":

                msg = event["message"]["text"]

                # บันทึกเฉพาะข้อความรายงาน
                if msg.startswith("#ตรวจ"):

                    print("========== REPORT ==========")
                    print("เวลา:", datetime.now())
                    print(msg)
                    print("===========================")

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
``
