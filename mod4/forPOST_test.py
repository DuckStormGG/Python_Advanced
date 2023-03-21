

from flask import Flask
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired,  Email, ValidationError, Optional

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False


def number_length(max: int, message: Optional = None):
    def _number_length(form, field):
        length = (field.data // (10 ** (max-1)))
        if length+1 != max :
            raise ValidationError("Invalid phone")

    return _number_length


class NumberLength:
    def __init__(self, max):
        self.max = max

    def __call__(self, form, field):
        length = (field.data // (10 ** (self.max - 1)))
        print(self.max)
        print(length)
        if length + 1 != self.max:
            raise ValidationError("Invalid phone")


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    # phone = IntegerField(validators=[InputRequired(), number_length(10)])
    phone = IntegerField(validators=[InputRequired(), NumberLength(10)])
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
