""" Website Homepage templates
"""

from flask import Blueprint, render_template


blueprint = Blueprint('Homepage', __name__)


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template('index.html')


@blueprint.route('/contact')
def contact_page():
    return render_template('contact.html')


@blueprint.route('/about')
def about_page():
    return render_template('about.html')


@blueprint.route('/dashboardDW')
def dashboardDW_page():
    return render_template('dashboardDW.html')
