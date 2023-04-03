from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '41ac0aad7dcefe9f83423ac962f2377a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hcxvvibhxowkdb:ee97bc39811c8be83131f4a7ad352cf8e3f93435af0e6821f21a1b10756fde84@ec2-44-215-1-253.compute-1.amazonaws.com:5432/db2p65rbhfglo1'
db = SQLAlchemy(app)

from MyApp import routes