import sys
sys.dont_write_bytecode = True

from flask import Flask
from route import route
import os

app = Flask(__name__)
app.secret_key = os.environ["simpleMsgFlaskKey"]

from flask_bootstrap import Bootstrap4
from flask_wtf import CSRFProtect

Bootstrap4(app)
csrf = CSRFProtect(app)

app.register_blueprint(route)

if __name__ == '__main__':
    app.run(debug=True)
