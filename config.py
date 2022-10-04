# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DB_PATH = 'sqlite:///dbstorage/dbaircontroller.sqlite'
    DEV = 1
    SQLALCHEMY_DATABASE_URI = DB_PATH     # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'xa>0@NO2Y?#%&(bF8GU)gLhR*pE!3<1MVDwtTAm-PCXyJ9n6K~uzQr5iq_^s'