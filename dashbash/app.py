from flask import Flask, render_template

app_name = 'dashbash'
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('err_404.html')
