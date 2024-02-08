import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config
from flask_cors import CORS
login_manager = LoginManager()
cors = CORS()

def create_app(conf_class=Config):
    # raise Exception("CREATE APP HAPPENED")
    from .models import User, Request , db
    templates=os.path.join(os.path.dirname(__file__), '../client/build')
    statics = os.path.join(os.path.dirname(__file__), '../client/build/assets')
    app = Flask(__name__) # , template_folder=templates, static_folder=statics, static_url_path='/')
    cors.init_app(app)
    app.config.from_object(conf_class)
    db.init_app(app)
    login_manager.init_app(app)

    

    # blueprint setup
    # notice that in auth.py and main.py, we create Blueprint objects that we then register here as part of the application
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from .main import main as main_bp
    app.register_blueprint(main_bp)


    return app

