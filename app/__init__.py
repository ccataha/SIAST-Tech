from flask import Flask


from config import Config

from flask_sse import sse
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://siast_user:ninja@localhost/SIAST_USERS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)
app.config.from_object(Config)
app.register_blueprint(sse, url_prefix='/stream')


from app import models, routes

db.create_all()



