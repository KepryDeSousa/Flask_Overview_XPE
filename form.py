from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class NameForms(FlaskForm):
    name = StringField("Qual é o seu nome ?",validators=[DataRequired()])
    Submit = SubmitField("submit")
