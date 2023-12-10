from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from api import login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship
db = SQLAlchemy(engine_options={"pool_pre_ping": True, "pool_recycle":300})

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    full_name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    u_type = db.Column(db.String(9), nullable=False)

    def __repr__(self):
        return f"<{self.u_type}: {self.full_name}>"
    
    def asstring(self):
        return f'User(full_name="{self.full_name}",email="{self.email}",password="{self.password}",u_type="{self.u_type}")'

    def to_object(self):
        obj = {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "u_type": self.u_type
        }
        return obj

# Request model

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    uid = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False) # db.ForeignKey(users.id)
    date = db.Column(db.Date)
    date_sent = db.Column(db.DateTime(timezone=True), server_default=func.now())
    slot_id=db.Column(db.String(3), nullable=False)
    is_approved = db.Column(db.Boolean, nullable=False)

    booker = relationship('User', foreign_keys='Request.uid')

    def __repr__(self):
        return f"<REQUEST from USER {self.uid} for {self.slot_id}"
    
    def asstring(self):
        return f'Request(title="{self.title}",description="{self.description}",uid="{self.uid}",date={self.date}, slot_id="{self.slot_id}", is_approved={self.is_approved})'

    def to_obj(self):
        obj = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "uid": self.uid,
            "date": self.date,
            "date_sent": self.date_sent,
            "slot_id": self.slot_id,
            "is_approved": self.is_approved
        }