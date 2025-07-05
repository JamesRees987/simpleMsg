import sys
sys.dont_write_bytecode = True

from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.environ["simpleMsgFlaskKey"]

from flask_bootstrap import Bootstrap4
from flask_wtf import CSRFProtect

Bootstrap4(app)
csrf = CSRFProtect(app)

from routes.views import route
from routes.auth import auth

app.register_blueprint(route)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)
