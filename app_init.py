import os
import logging
from flask import Flask
from sqlalchemy.engine import Engine
from sqlalchemy import event

from abilities import apply_sqlite_migrations
from models import db
from routes import register_routes


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def create_initialized_flask_app():
    app = Flask(__name__, static_folder='static')

    # Set Flask secret key
    app.config['SECRET_KEY'] = 'supersecretflaskskey'

    # Initialize database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    db.init_app(app)

    # Apply database migrations
    with app.app_context():
        apply_sqlite_migrations(db.engine, db.Model, 'migrations')

    register_routes(app)

    return app