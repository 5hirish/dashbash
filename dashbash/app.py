from flask import Flask, render_template, jsonify, json

# ********** Views **************

from dashbash.views import user_view
from dashbash.views import dashboard_view

app_name = 'dashbash'
app = Flask(__name__)

if app.env == 'development' or app.env == 'testing':
    # Rename the dashbash/config/config_dev.py.example to config_dev.py
    app.config.from_object('dashbash.config.config_dev')

# app.logger.info('ENV:{0}'.format(app.config['ENV']))


@app.errorhandler(404)
def not_found(error):
    return render_template('err_404.html'), 404


# Load User Before request
@app.before_request
def get_current_user():
    pass


@app.route('/')
def home_page():
    home_data = {
        'title': 'DashBash',
        'text': 'Welcome to your Dasboard'
    }

    return render_template('index.html', title='DashBash', result=json.dumps(home_data))

# ********** BluePrints ***********


app.register_blueprint(user_view.app)
app.register_blueprint(dashboard_view.app)
