from flask import Blueprint, request, redirect, render_template, jsonify, url_for

blue_print_name = 'dashboard'
blue_print_prefix = '/dashboard'

app = Blueprint(blue_print_name, __name__, url_prefix=blue_print_prefix)


@app.route('/')
def show_user_dashboard():
    # It accepts the name of the function as its first argument and any number of keyword arguments,
    # each corresponding to a variable part of the URL rule.
    # Unknown variable parts are appended to the URL as query parameters.
    return redirect(url_for('home_page'))