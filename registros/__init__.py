from flask import Flask

app = Flask(__name__)

ORIGIN_DATA = "data/coches.sqlite"

from registros.routes import *