import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://admin:admin123@127.0.0.1:3306/diet-crud')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
