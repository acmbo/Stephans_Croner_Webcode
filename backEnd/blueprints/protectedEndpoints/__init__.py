from flask import Blueprint, render_template, request, jsonify, redirect, url_for, abort
from flask_wtf import FlaskForm
from flask_login import login_required, current_user, logout_user

from extensions import db

from ..operationalEndpoints.meta.models import ScrapperDataSchema, UsedKeywordSchema
from ..operationalEndpoints.meta.orm import get_all_scrappermeta, add_meta, deleteScrapperbyId, get_all_scrappermeta_by_timeframe
from ..blogendpoints.orm import get_all_posts
from ..blogendpoints.models import BlogpostSchema


blueprint = Blueprint('Userpage', __name__, url_prefix='/usr')


scrapperDataSchema = ScrapperDataSchema()
blogpostSchema = BlogpostSchema()


@blueprint.route('/blub', methods=['GET'])
def blub():
    return 'You are logged in'


# Define a route for the protected page that requires authentication
@blueprint.route('/protected')
@login_required
def protected():
    return 'You are logged in'


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('Homepage.login'))
