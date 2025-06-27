import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:jroshan%4098@localhost/crud_demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key-here'