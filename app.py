from models.User import db
from flask import Flask 
from flask import render_template
import os 
from form import NameForms
import config
from flask_migrate import Migrate




app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app,db)



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
