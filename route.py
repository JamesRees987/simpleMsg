from flask import Blueprint, render_template

route = Blueprint('route', __name__)

@route.route('/')
def home():
    return render_template("home.html")