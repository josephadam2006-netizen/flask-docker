import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    APP_NAME = os.getenv("APP_NAME", "Flask Docker App")
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"
