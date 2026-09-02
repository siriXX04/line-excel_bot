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

        # รับเฉพาะข้อความ
        if event.get("type") == "message":

            if event["message"]["type"] == "text":

                msg = event["message"]["text"]

                # รับเฉพาะข้อความที่ขึ้นต้นด้วย #ตรวจ
                if msg.startswith("#ตรวจ"):

                    branch = ""
                    status = ""
                    detail = ""

                    for line in msg.split("\n"):

                        if line.startswith("สาขา:"):
                            branch = line.replace("สาขา:", "").strip()

                        elif line.startswith("สถานะ:"):
                            status = line.replace("สถานะ:", "").strip()

                        elif line.startswith("รายละเอียด:"):
                            detail = line.replace("รายละเอียด:", "").strip()

                    print("===== REPORT =====")
                    print("เวลา =", datetime.now())
                    print("สาขา =", branch)
                    print("สถานะ =", status)
                    print("รายละเอียด =", detail)
                    print("==================")

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
