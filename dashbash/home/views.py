from flask import Blueprint, request, jsonify

blue_print_name = 'home'
blue_print_url_prefix = '/'

home_blueprint = Blueprint(blue_print_name, __name__, url_prefix=blue_print_url_prefix)


@home_blueprint.route('/')
def home_page():
    return jsonify({'title': 'DashBash', 'testimony': ['Very Cool', 'Loved It']})
