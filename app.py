from api import app
from api.database import db
from routes.router import *

# アプリを起動する前にDBを初期化する
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()