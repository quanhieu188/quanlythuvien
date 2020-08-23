from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key="-\x0f'\x16\xea\x0b\xa8\xde\xc8\xc9\xff\xbdk\x9b\xc5B"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1/librarydb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

admin = Admin(app=app, name="QUAN LY THU VIEN", template_mode="bootstrap3")

login = LoginManager(app=app)