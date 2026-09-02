from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE Bot Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    print(request.json)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
