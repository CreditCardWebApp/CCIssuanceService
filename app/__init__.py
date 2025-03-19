from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = None

def create_app():
    global app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from . import routes
        # Create tables
        db.create_all()

    return app