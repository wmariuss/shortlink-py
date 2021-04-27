from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EnterShortURLForm(FlaskForm):
    url = StringField("Enter a URL", validators=[DataRequired()])
    submit = SubmitField("Get the short URL")


class ReturnToMainButton(FlaskForm):
    submit = SubmitField("Go back to main")
