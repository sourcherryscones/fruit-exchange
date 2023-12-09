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
    req = request.json
    print(request.json)
    username = req['username']
    passwd = req['password']
    print("USERNAME IS")
    print(username)
    print("PASSWORD IS")
    print(passwd)
    usr = User.query.filter_by(full_name=username).first()
    if not usr:
        return jsonify({"success": False, "error": "USER DOES NOT EXIST"})
    if passwd != usr.password:
        return jsonify({"success": False, "error": "PASSWORD DOES NOT MATCH"})
    session["uid"] = usr.id
    print("UID HAS BEEN PUT INTO SESSION")
    session["fname"] = usr.full_name.split(' ')[0]
    session["utype"] = usr.u_type
    print("UID IS")
    print(session["uid"])
    print("USER FIRST NAME IS:")
    print(session["fname"])
    # return redirect('/home'), HTTPStatus(301)
    return jsonify({"success": True, "firstname": session["fname"]})


@auth.route('/unauth')
def unauth():
    return '<h1>Wrong credentials</h1>'

@auth.route('/logout', methods=['POST'])
def logout():
    print("MADE IT TO LOGOUT ROUTE OH MY GOSH")
    req = request.json
    print(req['logout'])
    if "uid" in session:
        print("UID AS READ BY LOGOUT IS")
        print(session['uid'])
    else:
        print('no uid in there')
    if req['logout'] == True and "uid" in session:
        print("user was logged in")
        session.pop("uid", None)
        return redirect('/'), HTTPStatus(301)
    failmsg = jsonify({'logout': False})
    print(failmsg)
    return failmsg