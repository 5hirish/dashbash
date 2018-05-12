from flask import Blueprint, request, redirect, render_template, jsonify, url_for

blue_print_name = 'dashboard'
blue_print_prefix = '/dashboard'

app = Blueprint(blue_print_name, __name__, url_prefix=blue_print_prefix)


@app.route('/')
def show_user_dashboard():
    return redirect(url_for('home_page'))