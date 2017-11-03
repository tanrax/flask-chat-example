# -*- coding: utf-8 -*-
# Librarys
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
app = Flask(__name__)

# Settings
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Variables
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Chat(db.Model):
    '''
    Table chat
    '''
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    text = db.Column(db.Text)
    channel = db.Column(db.Integer)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Chat {0}>'.format(self.username)


if __name__ == "__main__":
    manager.run()
