"""further details about the process:
https://flask-marshmallow.readthedocs.io/en/latest/#flask_marshmallow.sqla.SQLAlchemyAutoSchema

For installation:
pip install -U flask-sqlalchemy marshmallow-sqlalchemy

Innitialization of DB by Flask does'nt work!!! Therefore the databases have to be initialized via the orm-scripts with the functions createDB() in the seperates orm.py's
"""
from flask import Flask
from flask_cors import CORS


# Get DBs and Marschmallow
#from extensions import db, ma
from extensions import *

# Get Blueprints
from blueprints.operationalEndpoints.geopy import blueprint as geopy_endpoints
from blueprints.operationalEndpoints.meta import blueprint as meta_endpoints
from blueprints.operationalEndpoints.themegraph import blueprint as themegraph_endpoints
from blueprints.siteEndpoints import blueprint as homepage_endpoints
from blueprints.blogendpoints import blueprint as blogendpoints
from blueprints.protectedEndpoints import blueprint as protectedEndpoints

import os

DBPath = os.path.join(os.getcwd(), "db.sqlite")

app = Flask(__name__,
            static_folder="static")

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DBPath}"
app.config['SECRET_KEY'] = 'SCorner'  
app.config['UPLOAD_FOLDER'] = '\\static\\assets\\blog'



# Blueprint registration

app.register_blueprint(geopy_endpoints)
app.register_blueprint(homepage_endpoints)
app.register_blueprint(meta_endpoints)
app.register_blueprint(themegraph_endpoints)
app.register_blueprint(blogendpoints)
app.register_blueprint(protectedEndpoints)



# Order matters: Initialize SQLAlchemy before Marshmallow
db.init_app(app)
ma.init_app(app)
login_manager.init_app(app)



# Innitialization of DB by Flask does'nt work!!! Therefore the databases have to be initialized via the orm-scripts with the functions createDB() in the seperates orm.py's
# with app.app_context():
#    db.create_all()
#    db.session.commit()
# @app.cli.command()
# def createdb():
#    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
