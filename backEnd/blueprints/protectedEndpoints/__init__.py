from flask import Blueprint, render_template, request, jsonify, redirect, url_for, abort
from flask_wtf import FlaskForm
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, verify_jwt_in_request


from extensions import db

from ..operationalEndpoints.meta.models import ScrapperDataSchema, UsedKeywordSchema
from ..operationalEndpoints.meta.orm import get_all_scrappermeta, add_meta, deleteScrapperbyId, get_all_scrappermeta_by_timeframe
from ..blogendpoints.orm import get_all_posts
from ..blogendpoints.models import BlogpostSchema


blueprint = Blueprint('Userpage', __name__, url_prefix='/usr')


scrapperDataSchema = ScrapperDataSchema()
blogpostSchema = BlogpostSchema()


@blueprint.route('/index')
@jwt_required
def index():
    authenticated = False
    verify_jwt_in_request()
    current_user = get_jwt_identity()
    authenticated = True


    posts = [blogpostSchema.dump(p) for p in get_all_posts(db.session)][:10]
    for i in range(len(posts)):
        posts[i]['thumbnailpath'] = posts[i]['thumbnailpath'].split("/",2)
    
    return render_template('index.html', posts = posts, authenticated=authenticated)



@blueprint.route('/blub', methods=['GET'])
def blub():
    if 'Authorization' not in request.headers:
        # Redirect user to login page
        return redirect(url_for('Homepage.login'))

    try:
        access_token = request.headers['Authorization'].split()[1]
        #decoded_token = jwt.decode(access_token, 'SCorner'  )
        current_user = "test"
    except:
        # Invalid token
        return abort(401)

    return jsonify(logged_in_as=current_user), 200