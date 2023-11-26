import os
from flask import request, send_from_directory, jsonify, session, redirect, Blueprint, current_app, render_template
from http import HTTPStatus
from datetime import date, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as sgmail

from flask_login import login_required, current_user
from .models import db, User, Request
admin = Blueprint('admin', __name__)



