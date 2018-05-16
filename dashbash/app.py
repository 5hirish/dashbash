from flask import Flask, render_template

# ********** Views **************

from dashbash.user.views import user_blueprint
from dashbash.dashboard.views import dashboard_blueprint
from dashbash.home.views import home_blueprint
from dashbash.settings import ProdConfig
from dashbash.extensions import db, debug_toolbar, migrate

app_name = 'dashbash'


# app.logger.info('ENV:{0}'.format(app.config['ENV']))


def create_app(config_object=ProdConfig):
    app = Flask(__name__)

    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    # register_shellcontext(app)
    # register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    # bcrypt.init_app(app)
    # cache.init_app(app)
    db.init_app(app)
    # csrf_protect.init_app(app)
    # login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    # webpack.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(home_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(dashboard_blueprint)
    # app_dasbash.register_blueprint(user_blue_print)
    # app_dasbash.register_blueprint(dashboard_blue_print)
    return None


def register_error_handlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

# @app_dasbash.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404


# Load User Before request
# @app_dasbash.before_request
# def get_current_user():
#     pass


# @app_dasbash.route('/')
# def home_page():
#     home_data = {
#         'title': 'DashBash',
#         'text': 'Welcome to your Dasboard'
#     }
#
#     return render_template('index.html', title='DashBash', result=json.dumps(home_data))

