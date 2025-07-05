from flask import Blueprint, render_template
from forms import SignInForm, SignUpForm

auth = Blueprint('auth', __name__)

@auth.route('/signIn')
def signIn():
    form = SignInForm()
    return render_template("auth/signIn.html", form=form)

@auth.route('/signUp')
def signUp():
    form = SignUpForm()
    return render_template("auth/signUp.html", form=form)

@auth.route('/auth/signOut')
def signOut():
    pass