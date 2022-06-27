import sys; sys.path.append('/path/to/my/pylib')

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@Localhost/mvc'
app.config['SECRET_KEY'] = "random string"

app.config['MAIL_SERVER'] = 'smtp-dreamkeyboard.alwaysdata.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'dreamkeyboard@alwaysdata.net'
app.config['MAIL_PASSWORD'] = 'Dremkbd91'
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True

app.config['BCRYPT_LOG_ROUNDS'] = 6
app.config['BCRYPT_HASH_IDENT'] = '2b'
app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from Newsletter import route


