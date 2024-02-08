import os
from flask import request, send_from_directory, jsonify, session, redirect, Blueprint, current_app, render_template
from http import HTTPStatus
from datetime import date, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as sgmail
from flask_cors import cross_origin

from flask_login import login_required, current_user
from .models import db, User, Request
from .schedule import SCHEDULE_TEMPLATE, MAX_ROOMS
from copy import deepcopy
main = Blueprint('main', __name__)

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


@main.route('/home')
def holamundo():
    if not "uid" in session:
        return '<h1>You must log in to book a conference room!</h1>', HTTPStatus(401)
    return render_template('bookroom.html', fname=session["fname"])


@main.route('/getschedule')
@cross_origin()
def get_schedule():
    temp = deepcopy(SCHEDULE_TEMPLATE)
    td = date.today()
    last_monday = td - timedelta(days=td.weekday())
    # print(last_monday)
    allreqs = Request.query.all() # filter by dates from mon to fri
    freqs = {"M1": 0, "M2": 0,"M3": 0, "M4": 0,"M5": 0, "M6": 0,"M7": 0, "ML": 0,
             "T1": 0, "T2": 0,"T3": 0, "T7": 0, "TL":0, 
             "W4": 0, "W5": 0,"W6": 0, "WL": 0,
             "R1": 0, "R2": 0,"R3": 0, "R7": 0, "RL":0,
             "F4": 0, "F5": 0,"F6": 0, "FL": 0,}
    
    for r in allreqs:
        if r.is_approved == True:
            freqs[r.slot_id] = freqs[r.slot_id] + 1

    for day in temp:

        for slot in day:
            slot["freq"] = freqs[slot["slot_id"]]
            slot["date"] = last_monday.isoformat()
            slot["day"] = last_monday.weekday()
            if freqs[slot["slot_id"]] >= MAX_ROOMS:
                slot["bookable"] = False
            else:
                slot["bookable"] = True
            
        last_monday = last_monday + timedelta(days=1)
    
    # print("TEMP IS")
    # print(temp)

    return temp
            


@main.route('/bookroom')
@cross_origin
def bookroom():
    return render_template('bookroom.html')

@main.route('/book', methods=['POST'])
def book():
    req = request.json
    title=req['title']
    description=req['description']
    userid=1

    fecha=date.fromisoformat(req['date'])
    slot_id=req['slot_id'] ########################
    newreq = Request(title=title, description=description,uid=userid,date=fecha,slot_id=slot_id,is_approved=False)
    print("request is")
    print(newreq)
    db.session.add(newreq)
    db.session.flush()
    db.session.commit()
    print("Request sent!")
    resp = jsonify(newreq)
    print(resp)
    return resp

@main.route('/allreqs')
def getallreqs():
    if not "utype" in session or session["utype"] != "ADMIN":
        return redirect('/unauth'), HTTPStatus(301)
    allreqs = Request.query.all()
    return render_template('admindash.html',reqs=allreqs)


@main.route('/approve', methods=["PATCH"])
def approve_request():
    req = request.json
    slot_id = req["slot_id"]
    slot_date = req["date"]
    slot_booker = req["uid"]
    print(slot_id)
    print(slot_date)
    print(slot_booker)

    tba = Request.query.filter_by(uid=slot_booker, date=slot_date, slot_id=slot_id).first()
    if tba:
        tba.is_approved = True
        db.session.commit()

    return jsonify({"approved": True})
