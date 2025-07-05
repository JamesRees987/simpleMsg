from flask import Blueprint, render_template
from forms import TestForm

route = Blueprint('route', __name__)

@route.route('/', methods=['GET', 'POST'])
def home():
    form = TestForm()
    if form.validate_on_submit():
        name = form.name.data
        print(name)
    
    return render_template("home.html", form=form)