# Prevent pycache files because its messy
import sys
sys.dont_write_bytecode = True

from flask import Flask
from route import route

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.register_blueprint(route)

if __name__ == '__main__':
    app.run(debug=True)
