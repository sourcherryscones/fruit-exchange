# some imports! notably, packages for handling flask routing, sendgrid, and a bit of auth
import os
from flask import request, send_from_directory, jsonify, session, redirect, Blueprint, current_app, render_template
from http import HTTPStatus
from datetime import date, timedelta
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as sgmail
from flask_cors import cross_origin

from flask_login import login_required, current_user
from .models import db, User, ProduceType
main = Blueprint('main', __name__)

# the below two routes ('/' and '/<path:path>') connect flask and svelte, so leave these alone :)

@main.route('/', methods=['GET'])
def base():
    print('made it to base!')
    print(current_app.root_path)
    print(current_app.instance_path)
    return send_from_directory('../client', 'index.html')

@main.route('/<path:path>')
def home(path):
    print("PATH THING WAS CALLED")
    print(path)
    return send_from_directory('../client', path)

@main.route('/get_all_produce')
def get_all_produce():
    pass
    # gee i wonder what this one does

@main.route('/add_produce_type', methods=['POST'])
def add_produce_type():
    pass
    # create a new ProduceType object
    # note that you'll need the current user's user id, either from session or flask_login's current_user variable, to create an entry in the ProduceType table!

# you can use jinja templates if you want to test some small part of the backend, as in the route below:
@main.route('/test_route')
@cross_origin
def test_route():
    return render_template('test_route.html')

# what other routes will you need? walk through the application like a user would: once logged in, what actions should I be able to take?
