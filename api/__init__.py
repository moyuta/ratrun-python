from flask import Flask
from config import Config
from api.database import init_db, db
import secrets
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = secrets.token_hex(32)
    app.config['WTF_CSRF_ENABLED'] = False
    csrf = CSRFProtect(app)
    login_manager = LoginManager(app)
    init_db(app)

    return app

app = create_app()
