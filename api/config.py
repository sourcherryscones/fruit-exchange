import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}  
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_SENDER = os.environ.get('MAIL_SENDER')
    MAIL_DEFAULT_SENDER = os.environ.get('DFLT_SENDER')
    MAIL_PASSWORD = os.environ.get('MAIL_PW')
    ALLOWED_EXTENSIONS={"pdf","png","jpg","jpeg"}
    BUCKET_NAME=os.environ.get('BUCKET_NAME')
    AWS_AK=os.environ.get('AWS_AK')
    AWS_SK=os.environ.get('AWS_SK')

