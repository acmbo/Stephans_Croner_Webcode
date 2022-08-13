"""DB Models for Flask Marschmallow

for further information see : https://flask-marshmallow.readthedocs.io/en/latest/
"""
from extensions import ma
from extensions import Blogpost

class BlogpostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Blogpost

    id = ma.auto_field()
    title = ma.auto_field()
    contenthtml = ma.auto_field()
    date = ma.auto_field()
    Tags = ma.auto_field()
    autor = ma.auto_field()
    thumbnailpath = ma.auto_field()
    shortdescription = ma.auto_field()


