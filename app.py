from flask import Flask as Fk
from flask import render_template
import os 

template_dir = os.path.abspath("./Templates")

app = Fk(__name__,template_folder=template_dir)

#rotas
@app.route("/")
@app.route("/user")
@app.route("/user/<name>")
def Index(name=None):
    return render_template("index.html",name=name)
