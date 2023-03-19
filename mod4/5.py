import shlex

from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def max_number():
    args: list[str] = request.args.getlist('arg')
    result = os.popen('ps ' + " ".join(['-' + arg for arg in args])).read()
    return "<pre>" + shlex.quote(result) + "<pre>"


if __name__ == "__main__":
    app.run(debug=True)
