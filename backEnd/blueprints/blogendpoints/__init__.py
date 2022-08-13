""" Website Homepage templates
"""

from flask import Blueprint, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SubmitField)
from wtforms.validators import InputRequired, Length, DataRequired

from extensions import db
from ..blogendpoints.models import BlogpostSchema

import datetime
import requests


blogpostSchema = BlogpostSchema()


PW = "alghtpoak"


class AddBlogpost(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=1, max=200)])
    contenthtml = TextAreaField('Content Html', validators=[DataRequired()])
    
    Tags = StringField('Tags')
    
    autor = StringField('Author')
    
    thumbnail = StringField('thumbnail')
    
    password = StringField("Password")
    
    submit = SubmitField('Submit')



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


@blueprint.route("/post/", methods=["GET", "POST"])
def create_post():
    
    form = AddBlogpost()
    
    if form.validate_on_submit():

        title = request.form.get("title")
        contenthtml = request.form.get("contenthtml")
        Tags = request.form.get("Tags")
        autor = request.form.get("autor")
        thumbnail = request.form.get("thumbnail")
        
        if request.form.get("password") == PW:
            
            return redirect(url_for("blog.success", title=title, content=contenthtml))
        
        else:
            return "Wrong password", 404
    
    
    return render_template("blog/add.html", form=form)



#@blueprint.route("/post/<string:title>", methods=["GET"])
@blueprint.route("/post/abc", methods=["GET"])
def success():
    title = request.args['title'] 
    content  = request.args['content'] 
    return render_template("blog/posttemplate.html", title=title, content=content)
