from flask import Blueprint, render_template

route = Blueprint('route', __name__)

@route.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")