from os import environ
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from models import db, Chat

load_dotenv(find_dotenv())
app = Flask(__name__)

# Config
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
if environ.get('DEBUG') == 'True':
    app.config['DEBUG'] = True
else:
    app.config['DEBUG'] = False
app.config['PORT'] = 80

# Socketio
DOMAIN = environ.get('DOMAIN')
socketio = SocketIO(app)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE')
db.init_app(app)


@app.route('/<int:channel>/<name>/')
def open_chat(channel, name):
    my_chat = Chat.query.filter_by(channel=channel).all()
    return render_template(
        'chat.html',
        domain=DOMAIN,
        chat=my_chat,
        channel=channel,
        username=name
    )


@socketio.on('new_message')
def new_message(message):
    # Send message to alls users
    emit('new_message', {
        'username': message['username'],
        'text': message['text']
    },
        broadcast=True
    )
    # Save message
    my_new_chat = Chat(
        username=message['username'],
        text=message['text'],
        channel=message['channel']
    )
    db.session.add(my_new_chat)
    try:
        db.session.commit()
    except:
        db.session.rollback()


if __name__ == '__main__':
    socketio.run(app)
