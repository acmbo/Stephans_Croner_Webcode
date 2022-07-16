""" Website Homepage templates
"""

from flask import Blueprint, render_template
from extensions import db
from ..operationalEndpoints.meta.models import ScrapperDataSchema, UsedKeywordSchema
from ..operationalEndpoints.meta.orm import get_all_scrappermeta, add_meta, deleteScrapperbyId
import datetime

blueprint = Blueprint('Homepage', __name__)

scrapperDataSchema = ScrapperDataSchema()


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

    # Add Data for Table and Submission section
    metainfo = get_all_scrappermeta(db.session)
    metainfo_list = [scrapperDataSchema.dump(info) for info in metainfo]

    for entry in metainfo_list:
        entry['entrydate'] = entry['entrydate'].split("T")[0]
        entry['amount_of_db_entries'] = int(entry['amount_of_db_entries'])
        entry['errors'] = int(entry['errors'])

    submissionInfo = metainfo_list[len(metainfo_list)-1]
    print(datetime.datetime.fromisoformat(submissionInfo['entrydate']))
    timedelta = datetime.datetime.now() - \
        datetime.datetime.fromisoformat(submissionInfo['entrydate'])

    lastupdate = timedelta.days
    metainfo_list.reverse()
    return render_template('dashboardDW.html', table_data=metainfo_list, submissionInfo=submissionInfo, lastupdate=lastupdate)
