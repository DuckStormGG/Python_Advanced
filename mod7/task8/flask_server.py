from flask_wtf import FlaskForm
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/logs", methods=["POST"])
def logs():
    form = request.form.to_dict()
    with open("main_logs.log", "a") as file:
        file.write(f"{form['levelname']}|{form['name']}|{form['asctime']}|{form['lineno']}|{form['msg']}\n")


@app.route("/get_logs", methods=["GET"])
def get_logs():
    with open("main_logs.log", "r") as file:
        return "<pre>" + file.read() + "<pre>"


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)