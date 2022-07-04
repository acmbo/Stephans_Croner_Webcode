"""further details about the process:
https://flask-marshmallow.readthedocs.io/en/latest/#flask_marshmallow.sqla.SQLAlchemyAutoSchema

For installation:
pip install -U flask-sqlalchemy marshmallow-sqlalchemy
"""

from flask import Flask

# Get DBs and Marschmallow
from extensions import db, ma

# Get Blueprints
from blueprints.operationalEndpoints.geopy import blueprint as geopy_endpoints
from blueprints.operationalEndpoints.meta import blueprint as meta_endpoints
from blueprints.operationalEndpoints.themegraph import blueprint as themegraph_endpoints
from blueprints.siteEndpoints import blueprint as homepage_endpoints

import os

geopyDBPath = os.path.join(os.getcwd(), "blueprints",
                           "operationalEndpoints", "geopy", "geopydb.sqlite")
metaDBPath = os.path.join(os.getcwd(), "blueprints",
                          "operationalEndpoints", "meta", "metadb.sqlite")

app = Flask(__name__,
            static_folder="static")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{geopyDBPath}"
#app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{metaDBPath}"
# SQLALCHEMY_BINDS = {
#    'geopy': f"sqlite:///{geopyDBPath}",
#    'meta': f"sqlite:///{metaDBPath}",
# }

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_BINDS"] = {
    'geopy': f"sqlite:///{geopyDBPath}",
    'meta': f"sqlite:///{metaDBPath}",
}


# Blueprint registration

# with app.app_context():
app.register_blueprint(geopy_endpoints)
app.register_blueprint(homepage_endpoints)
app.register_blueprint(meta_endpoints)
app.register_blueprint(themegraph_endpoints)


# Order matters: Initialize SQLAlchemy before Marshmallow

db.init_app(app)
ma.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
