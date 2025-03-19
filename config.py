import os

class Config:
    # Update the URI to connect to your MySQL database
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://ccapp:ccapp1608@mysql:3306/credit_cards_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
