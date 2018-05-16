from flask import Blueprint, request, redirect, render_template, jsonify, url_for
from dashbash.dashboard.models import Notes, Tags
#from dashbash.database import psg_db as db

blue_print_name = 'dashboard'
blue_print_prefix = '/dashboard'

dashboard_blue_print = Blueprint(blue_print_name, __name__, url_prefix=blue_print_prefix)


@dashboard_blue_print.route('/')
def show_user_dashboard():
    # It accepts the name of the function as its first argument and any number of keyword arguments,
    # each corresponding to a variable part of the URL rule.
    # Unknown variable parts are appended to the URL as query parameters.
    return redirect(url_for('home_page'))


@dashboard_blue_print.route('/note', method=['POST'])
def insert_note():
    if request.method == 'POST':
        if 'title' in request.form:
            try:
                tag_list = request.form['tags'].split()
                for tag in tag_list:
                    Tags.create(tag=tag)
                    Notes.create(title=request.form['title'], content=request.form['content'])
                    # note_record.children.append(tag_record)

            except KeyError:
                pass
            return jsonify({"status": "success", "msg": "Note Inserted"}), 200
        else:
            return jsonify({"status": "error", "msg": "Note title required"}), 400
    else:
        return jsonify({"status": "error", "msg": "Unsupported method"}), 403
