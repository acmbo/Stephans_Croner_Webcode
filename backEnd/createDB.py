from extensions import *

from blueprints.blogendpoints.orm import createMetaDb
createMetaDb(Base)
from blueprints.operationalEndpoints.meta.orm import createMetaDb
createMetaDb(Base)
from blueprints.operationalEndpoints.themegraph.orm import createMetaDb
createMetaDb(Base)