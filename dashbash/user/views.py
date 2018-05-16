from flask import Blueprint, request, render_template, jsonify

blue_print_name = 'user'
# blue_print_version = 'v1'
# blue_print_url_prefix = '/'+blue_print_version+'/user'
blue_print_url_prefix = '/user'

user_blueprint = Blueprint(blue_print_name, __name__, url_prefix=blue_print_url_prefix)


@user_blueprint.route('/')
def hello_world():
    return 'Hello User!'


@user_blueprint.route('/login', methods=['GET', 'POST'])
def oauth_login_providers():
    if request.method == 'POST':
        return 'hi'
    else:
        return 'show login'
