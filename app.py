from flask import Flask, flash, redirect, render_template, request, send_from_directory
import os, cs50
from dotenv import dotenv_values

app = Flask(__name__)

config = dotenv_values(".env")

app.secret_key = config.get('SECRET_KEY')

db = cs50.SQL('sqite:///database.db')

#create the user table

db.execute("CREATE TABLE [IF NOT EXISTS] Users (userId INTEGER AUTOINCREMENT PRIMARY KEY, username TEXT NOT NULL UNIQUE, hash TEXT NOT NULL )")
db.execute("CREATE TABLE [IF NOT EXISTS] User_Profile (firstname TEXT, lastname TEXT, email TEXT, gender TEXT, date_of_birth DATETIME, phone_number INTEGER, userId INTEGER)")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/")
def index():
    return render_template("index.html", title="Hello")


@app.route("/delete")
def delete():
    return True


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("forms/login_form.html")


@app.route("/logout")
def logout():
    return True


@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if request.method == "GET":
        return render_template("forms/reset_password_form.html")


@app.route("/set-password")
def set_new_password():
    if request.method == "GET":
        return render_template("set_password_form.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("forms/registration_form.html")


@app.route("/verification", methods=["GET", "POST"])
def verification():
    if request.method == "GET":
        return render_template("forms/account_verification_form.html")
