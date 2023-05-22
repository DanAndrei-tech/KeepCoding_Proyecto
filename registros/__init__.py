from flask import Flask

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'

ORIGIN_DATA = "data/coches.sqlite"

from registros.routes import *