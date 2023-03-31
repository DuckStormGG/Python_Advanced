import os
import sys
import time
import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False


class InputForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=1, max=30)])


@app.route("/run-python", methods=["POST"])
def run_python():
    form = InputForm()
    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        cmd = f'prlimit --nproc=1:1 python3 -c "{code}"'
        program = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        try:
            out , err = program.communicate(timeout = timeout)
            return out , err
        except subprocess.TimeoutExpired:
            program.kill()
    return f"{form.errors}", 400


if __name__ == "__main__":
    app.run(debug=True)
