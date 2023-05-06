from flask import Blueprint, render_template, request, jsonify, redirect, url_for, abort
from flask_wtf import FlaskForm
from flask_login import login_required, current_user, logout_user

from extensions import db

from ..operationalEndpoints.meta.models import ScrapperDataSchema, UsedKeywordSchema
from ..operationalEndpoints.meta.orm import get_all_scrappermeta, add_meta, deleteScrapperbyId, get_all_scrappermeta_by_timeframe
from ..blogendpoints.orm import get_all_posts
from ..blogendpoints.models import BlogpostSchema
from ..siteEndpoints.__init__ import checkAuth


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



@blueprint.route('/drawtest', methods=['GET','POST'])
@login_required
def drawtest():
    import base64
    
    if request.method == 'POST':
        image_data = request.POST.get('imageData')
        
        if image_data:
            image_data = image_data.replace('data:image/png;base64,', '')
            with open('image.png', 'wb') as f:
                f.write(base64.b64decode(image_data))
            return  jsonify({'status': 'ok'})
        return jsonify({'status': 'error'})
    else:
        authenticated=checkAuth()
        return render_template('draw.html', authenticated=authenticated)
    
    
    
@blueprint.route('/chat', methods=['GET','POST'])
@login_required
def chat():
    authenticated=checkAuth()
    
    if request.method == 'POST':
        image_data = request.POST.get('imageData')
        return jsonify({'status': 'error'})
    else:
        
        return render_template('chat.html', authenticated=authenticated)
    
    
@blueprint.route('/chatTalk', methods=['POST'])
@login_required
def chatTalk():
    data = request.get_json()
    message = data.get('message')
    return jsonify({'status': 'success', 'message': 'Message sent!'})


