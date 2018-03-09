from flask import Flask
from .database import *
app = Flask(__name__)

from app.route1.routes import mod
from app.route2.routes import mod

# app.config['MONGO_DBNAME'] = 'test'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'
app.config['MONGO_DBNAME'] = 'freqeffects'
app.config['MONGO_URI'] = 'mongodb://freqeffects:digjam@ds243055.mlab.com:43055/freqeffects'

mongo.init_app(app)


app.register_blueprint(route1.routes.mod)
app.register_blueprint(route2.routes.mod, url_prefix='/api')