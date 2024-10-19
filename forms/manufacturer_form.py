from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired


class ManufacturerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description")
    country = TextAreaField("Country")
    certificates = TextAreaField("Certificates")
    brands = SelectMultipleField("Brands", coerce=int)
    submit = SubmitField("Add Manufacturer")
