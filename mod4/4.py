from flask import Flask
import os

app = Flask(__name__)


@app.route("/uptime", methods=["GET"])
def max_number():
    UPTIME = os.popen('uptime -p').read()[:-1]
    return f"Current uptime is {UPTIME}"


if __name__ == "__main__":
    app.run(debug=True)
