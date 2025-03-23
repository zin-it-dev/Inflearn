import os, secrets, cloudinary

from dotenv import load_dotenv
from flask import Config
from datetime import timedelta

load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(os.path.dirname(__file__), "static")


class BaseConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex()
    JWT_SECRET_KEY = os.getenv("SUPPER_SECRET_KEY") or secrets.token_hex()
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    DB_NAME = os.getenv("DB_NAME") or "inflearn.db"
    DB_SERVER = os.getenv("DB_SERVER") or "192.168.1.56"
    DB_USERNAME = os.getenv("DB_USERNAME") or "root"
    DB_PASSWORD = os.getenv("DB_PASSWORD") or "12345678"
    FLASK_ADMIN_SWATCH = "lux"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME")

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return (
            os.getenv("SQLALCHEMY_DATABASE_URI")
            or f"mysql+pymysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_SERVER}/{self.DB_NAME}?charset=utf8mb4"
        )

    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    )


class ProductionConfig(BaseConfig):
    DB_SERVER = "192.168.19.32"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "database", BaseConfig.DB_NAME)
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(Config):
    TESTING = True
    DB_SERVER = "localhost"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


settings = dict(development=DevelopmentConfig)
