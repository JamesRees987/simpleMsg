from flask import Blueprint

auth = Blueprint('route', __name__)

@auth.route('/auth/signIn')
def signIn():
    pass

@auth.route('/auth/signUp')
def signUp():
    pass

@auth.route('/auth/signOut')
def signOut():
    pass