import os
from flask import Flask

app = Flask(__name__)


@app.route("/is_working")
def is_working():
    return "IS WORKING!"


def run_app(port):
    while os.popen(f"lsof -i :{port}").read() != "":
        test = os.popen(f"lsof -i :{port}").read()
        list = test.split('\n')
        del list[0]
        tokill = list[0].split()[1]
        os.kill(int(tokill), 9)
    app.run(port=port)
    print(os.popen(f"lsof -i :{port}").read())


if __name__ == "__main__":
    run_app(5000)

