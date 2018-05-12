from flask_sqlalchemy import SQLAlchemy
from dashbash.app import app

DB_DIALECT = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_USERNAME = app.config['DB_USER']
DB_PASSWORD = app.config['DB_PASSWORD']
DB_HOSTNAME = app.config['DB_HOST']
DB_PORT = app.config['DB_PORT']
DB_NAME = app.config['DB_NAME']

DB_URL = DB_DIALECT + '+' + DB_DRIVER + '://' + DB_USERNAME + '@' + DB_HOSTNAME + ':' + DB_PORT + '/' + DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

psg_db = SQLAlchemy(app)

