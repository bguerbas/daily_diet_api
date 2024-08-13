import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@127.0.0.1:3306/diet-crud'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

