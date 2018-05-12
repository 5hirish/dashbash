from dashbash.app import app
from flask_debugtoolbar import DebugToolbarExtension

if __name__ == '__main__':

    # the toolbar is only enabled in debug mode:
    app.debug = True
    # set a 'SECRET_KEY' to enable the Flask session cookies in debug toolbar
    app.config['SECRET_KEY'] = 'shirish-dashbash'
    # The toolbar will automatically be injected into HTML responses when debug mode is on.
    # In production, setting `app.debug = False` will disable the toolbar.
    toolbar = DebugToolbarExtension(app)
    # Werkzeug, WSGI utility library for Python, enable module reloader
    app.run(use_reloader=True)
