from flask import Flask
from flask import request, render_template
from flask.ext.classy import FlaskView
from dashbash.app import app_name, app

app = Flask(app_name)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def oauth_login_providers():
    if request.method == 'POST':
        return 'hi'
    else:
        return 'show login'
