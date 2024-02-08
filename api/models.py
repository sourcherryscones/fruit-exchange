# again, helpful imports; the UserMixin class from flask-login allows the login_user function in auth.py to work, as does the login_manager variable from __init__.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from api import login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship
import datetime
from dataclasses import dataclass
db = SQLAlchemy(engine_options={"pool_pre_ping": True, "pool_recycle":300})

# if you're not using flask-login you can ignore this
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

@dataclass
class User(UserMixin, db.Model):
    pass
    # what fields will you need, and of which types?


# Request model

@dataclass
class ProduceType(db.Model):
    # what fields will you need in order to store all relevant info about each fruit tree/plant?
    # are there any that you'll need to connect to the user table? if so, the below line of code shows us how to create that relation:
    field_that_will_contain_a_user_object = relationship('User', foreign_keys='ProduceType.name_of_field_IN_THE_PRODUCETYPE_CLASS_that_you_want_to_refer_to_a_User_object')

   
# add __repr__ functions as they're convenient for you :)