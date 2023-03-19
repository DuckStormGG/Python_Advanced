from flask import Flask, request
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange, Email, ValidationError, Optional

app = Flask(__name__)


def number_length(min: int, max: int, message: Optional = None):
    def _number_length(form, field):
        if min > field.data or field.data > max:
            raise ValidationError("Invalid phone")

    return _number_length


class NumberLength:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __call__(self, form, field):
        if self.min > field.data or field.data > self.max:
            raise ValidationError("Invalid phone")


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    # phone = IntegerField(validators=[InputRequired(), number_length(1000000000, 9999999999)])
    phone = IntegerField(validators=[InputRequired(), NumberLength(1000000000,9999999999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField(validators=[InputRequired()])


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f'{email}  +7{phone}'
    return f"{form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
