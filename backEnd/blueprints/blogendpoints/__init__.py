""" Website Homepage templates
"""

from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
#from flask_uploads import Uploadset
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, DataRequired
from werkzeug.utils import secure_filename

from extensions import db
from ..blogendpoints.models import BlogpostSchema
from .orm import add_blogpost, get_all_posts, delete_post_by_Id, get_post_by_id, get_post_by_title


import os

blogpostSchema = BlogpostSchema()


PW = "alghtpoak"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = './static/assets/blog'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class AddBlogpost(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=1, max=200)])
    shortdescription = StringField('Shortdescription', validators=[InputRequired(),
                                             Length(min=1, max=500)])
    
    contenthtml = TextAreaField('Content Html', validators=[DataRequired()])
    
    Tags = StringField('Tags')
    
    autor = StringField('Author')
    
    password = StringField("Password")
    
    submit = SubmitField('Submit')
    
    file = FileField()  # Picturefile
    
    picdescription = StringField('Picture description')



# Form Template
#
#class CourseForm(FlaskForm):
#    title = StringField('Title', validators=[InputRequired(),
#                                             Length(min=10, max=100)])#
#    description = TextAreaField('Course Description',
#                                validators=[InputRequired(),
#                                            Length(max=200)])
#    price = IntegerField('Price', validators=[InputRequired()])
#    level = RadioField('Level',
#                       choices=['Beginner', 'Intermediate', 'Advanced'],
#                       validators=[InputRequired()])
#    available = BooleanField('Available', default='checked')



blueprint = Blueprint('blog', __name__, url_prefix='/blog')


@blueprint.route("/createpost/", methods=["GET", "POST"])
def create_post():
    
    form = AddBlogpost()
    
    if form.validate_on_submit():

        title = request.form.get("title")
        shortdescription = request.form.get("shortdescription")
        contenthtml = request.form.get("contenthtml")
        Tags = request.form.get("Tags")
        autor = request.form.get("autor")
        picdescription = request.form.get("picdescription")
        file = form.file.data
            
        if request.form.get("password") == PW:
            
            if file:
                filename = secure_filename(file.filename)
            
                if allowed_file(filename):
                    filepath = os.path.join(UPLOAD_FOLDER , filename)
                    file.save(os.path.join(UPLOAD_FOLDER , filename))
                    
                    add_blogpost(db.session,
                        title=title,
                        contenthtml=contenthtml,
                        Tags=Tags,
                        autor=autor,
                        thumbnailpath=filepath,
                        picdescription = picdescription,
                        shortdescription=shortdescription)
                else:
                    return "Bad Filename", 404
                
            else:
                add_blogpost(
                    title=title,
                    contenthtml=contenthtml,
                    Tags=Tags,
                    autor=autor,
                    shortdescription=shortdescription)
                
            return redirect(url_for("blog.success", title=title, content=contenthtml))
        
        else:
            return "Wrong password", 404
    
    
    return render_template("blog/createpost.html", form=form)



@blueprint.route("/allposts/", methods=["GET"])
def all_posts():
    posts = get_all_posts(db.session)
    post_list = [blogpostSchema.dump(info) for info in posts]
    return jsonify(post_list)

@blueprint.route("/post/<string:title>", methods=["GET"])
def post(title):
#@blueprint.route("/post/<int:id>", methods=["GET"])
#def post(id):
    #print("ID: ", id)
    #_post = get_post_by_id(db.session, id)
    print("Title ", title)
    _post = get_post_by_title(db.session, title)
    print("Post: ", _post)
    post_schema = [blogpostSchema.dump(p) for p in _post][0]
    print("POST", post_schema)
    post_schema['thumbnailpath'] = post_schema['thumbnailpath'].split("/",2)
    
    
    return render_template("blog/posttemplate.html", post=post_schema)
