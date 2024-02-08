# some imports! notably, packages for handling flask routing, sendgrid, and a bit of auth
import os
from flask import request, send_from_directory, jsonify, session, redirect, Blueprint, current_app, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from .models import db, User
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    pass
    # get JSON from request

    # make sure you got some valid input data (ie valid emails, minimum character # for passwords, do the passwords match?)

    # create a user object! store passwords using generate_password_hash :)

    # return json to tell the frontend whether or not you successfully registered!

# route for logging in
@auth.route('/login', methods=['POST'])
def login():
    pass 
    # the frontend will be posting JSON for username and password, so you need to get that from the request

    # check to see if the user exists and has entered the password correctly
     
    #add user id to session OR use flask-login's login_user function

    # return json to tell the frontend whether or not the login happened successfully!


# this is just a place you can redirect if login goes wrong 
@auth.route('/auth_error')
def unauth():
    return '<h1>Something went wrong, please try again!</h1>'

@auth.route('/logout', methods=['POST'])
def logout():
    pass
    # log out! again, can just work with flasks's session or can use flask-login

    # again, send status back to frontend when done!