from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired


class BrandForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description")
    logo = TextAreaField("Logo")
    manufacturers = SelectMultipleField("Manufacturers", coerce=int)
    submit = SubmitField("Add Brand")
