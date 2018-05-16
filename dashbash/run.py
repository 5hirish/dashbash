import sys
from flask.helpers import get_debug_flag
from dashbash.app import create_app
from dashbash.settings import DevConfig, ProdConfig

if __name__ == '__main__':

    app_config = DevConfig if get_debug_flag() else ProdConfig
    app = create_app(app_config)

    # the toolbar is only enabled in debug mode:
    app.debug = True
    # set a 'SECRET_KEY' to enable the Flask session cookies in debug toolbar
    # The toolbar will automatically be injected into HTML responses when debug mode is on.
    # In production, setting `app.debug = False` will disable the toolbar.

    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    app.logging.basicConfig(level=app.logging.DEBUG, stream=sys.stdout,
                                    format=logformat, datefmt="%Y-%m-%d %H:%M:%S")

    # app.logging.getLogger('urllib3').setLevel(app.logging.CRITICAL)
    app.logger = app.logging.getLogger(__name__)

    # Werkzeug, WSGI utility library for Python, enable module reloader
    app.run(use_reloader=True, reloader_interval=0, use_debugger=True, reloader_type='watchdog')
