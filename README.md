# Flask chat


## Use

* Flask (Obvious!)
* Flask-SQLAlchemy (ORM for database)
* Flask-socketio (Generation of forms and validations)

## Install

```bash
cp envExample .env
pip3 install -r requirements.txt
python3 models.py db init
python3 models.py db migrate
python3 models.py db upgrade
```

## Run

```bash
python3 main.py
```
