from flask import Flask, render_template

# ********** Views **************

from dashbash.views import user_view
from dashbash.views import dashboard_view

app_name = 'dashbash'
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('err_404.html'), 404


# Load User Before request
@app.before_request
def get_current_user():
    pass


@app.route('/')
def home_page():
    return render_template('index.html')

# ********** BluePrints ***********


app.register_blueprint(user_view.app)
app.register_blueprint(dashboard_view.app)
