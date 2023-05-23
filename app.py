from flask import Flask as Fk
from flask import render_template
import os 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


template_dir = os.path.abspath("./Templates")

app = Fk(__name__,template_folder=template_dir)

app.config["SECRET_KEY"] = "dsfdfdfdfdffdsdsd45454"
class NameForms(FlaskForm):
    name = StringField("Qual é o seu nome ?",validators=[DataRequired()])
    Submit = SubmitField("submit")

#rotas
@app.route("/",methods=['GET','POST'])
@app.route("/user",methods=['GET','POST'])
@app.route("/user/<name>",methods=['GET','POST'])
def Index(name=None):

    name = None
    form = NameForms()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "


    return render_template("index.html",name=name,form=form)
