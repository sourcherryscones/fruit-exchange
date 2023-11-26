import os
from flask import request, send_from_directory, jsonify, session, redirect, Blueprint, current_app, render_template
from http import HTTPStatus
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as sgmail

from flask_login import login_required, current_user
from .models import db, User, Request
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    # req = request.json
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    print(username)
    print(passwd)
    usr = User.query.filter_by(full_name=username).first()
    if passwd != usr.password:
        return redirect('/unauth'), HTTPStatus(301)
    session["uid"] = usr.id
    session["fname"] = usr.full_name.split(' ')[0]
    session["utype"] = usr.u_type
    print("UID IS")
    print(session["uid"])
    print("USER FIRST NAME IS:")
    print(session["fname"])
    return redirect('/home'), HTTPStatus(301)


@auth.route('/unauth')
def unauth():
    return '<h1>Wrong credentials</h1>'

@auth.route('/logout')
def logout():
    session.pop("uid", None)
    return redirect('/'), HTTPStatus(301)