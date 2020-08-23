from app import app, login
from flask import render_template, redirect, request
from app.models import *
from flask_login import login_user
import hashlib


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/login-admin", methods=["post", "get"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                                 User.password == password).first()
        if user:
            login_user(user=user)
    return redirect("/admin")


@login.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run()
