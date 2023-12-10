from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from api import login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship
import datetime
from dataclasses import dataclass
db = SQLAlchemy(engine_options={"pool_pre_ping": True, "pool_recycle":300})

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

@dataclass
class User(UserMixin, db.Model):
    id:int = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    full_name:str = db.Column(db.String(50), nullable=False, unique=True)
    email:str = db.Column(db.String(100), nullable=False, unique=True)
    password:str = db.Column(db.String(200), nullable=False)
    u_type:str = db.Column(db.String(9), nullable=False)

    def __repr__(self):
        return f"<{self.u_type}: {self.full_name}>"
    
    def asstring(self):
        return f'User(full_name="{self.full_name}",email="{self.email}",password="{self.password}",u_type="{self.u_type}")'


# Request model

@dataclass
class Request(db.Model):
    id:int = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title:str = db.Column(db.String(50), nullable=False)
    description:str = db.Column(db.String(100))
    uid:int = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False) # db.ForeignKey(users.id)
    date:datetime.date = db.Column(db.Date)
    date_sent:datetime.datetime = db.Column(db.DateTime(timezone=True), server_default=func.now())
    slot_id:int =db.Column(db.String(3), nullable=False)
    is_approved:bool = db.Column(db.Boolean, nullable=False)

    booker = relationship('User', foreign_keys='Request.uid')

    def __repr__(self):
        return f"<REQUEST from USER {self.uid} for {self.slot_id}"
    
    def asstring(self):
        return f'Request(title="{self.title}",description="{self.description}",uid="{self.uid}",date={self.date}, slot_id="{self.slot_id}", is_approved={self.is_approved})'