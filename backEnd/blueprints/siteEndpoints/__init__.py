""" Website Homepage templates
"""

from flask import Blueprint, render_template
from extensions import db
from ..operationalEndpoints.meta.models import ScrapperDataSchema, UsedKeywordSchema
from ..operationalEndpoints.meta.orm import get_all_scrappermeta, add_meta, deleteScrapperbyId, get_all_scrappermeta_by_timeframe
import datetime
import requests

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
    metainfo = get_all_scrappermeta_by_timeframe(db.session, days=7)
    metainfo_list = [scrapperDataSchema.dump(info) for info in metainfo]
    metainfo_list.reverse()

    for entry in metainfo_list:
        entry['entrydate'] = entry['entrydate'].split("T")[0]
        entry['amount_of_db_entries'] = int(entry['amount_of_db_entries'])
        entry['errors'] = int(entry['errors'])

    if len(metainfo_list) > 0:
        submissionInfo = metainfo_list[0]

        timedelta = datetime.datetime.now() - \
            datetime.datetime.fromisoformat(submissionInfo['entrydate'])

        lastupdate = timedelta.days
    else:
        submissionInfo = {"scrapper_name": "None",
                          "entrydate": "None",
                          "amount_of_db_entries": 0,
                          "errors": 0, }

        lastupdate = 0

    time_mode = "Weekly"

    return render_template('dashboardDW.html', table_data=metainfo_list, submissionInfo=submissionInfo, lastupdate=lastupdate, time_mode=time_mode)


@blueprint.route('/dashboardDWAll')
def dashboardDWAll_page():

    # Add Data for Table and Submission section
    metainfo = get_all_scrappermeta(db.session)
    metainfo_list = [scrapperDataSchema.dump(info) for info in metainfo]
    metainfo_list.reverse()

    for entry in metainfo_list:
        entry['entrydate'] = entry['entrydate'].split("T")[0]
        entry['amount_of_db_entries'] = int(entry['amount_of_db_entries'])
        entry['errors'] = int(entry['errors'])

    submissionInfo = metainfo_list[0]

    timedelta = datetime.datetime.now() - \
        datetime.datetime.fromisoformat(submissionInfo['entrydate'])

    lastupdate = timedelta.days

    time_mode = "All"

    return render_template('dashboardDW.html', table_data=metainfo_list, submissionInfo=submissionInfo, lastupdate=lastupdate, time_mode=time_mode)


# Monthly Postings
@blueprint.route('/dashboardDWpostingsmonth')
def dashboardDWpostings_page():
    url = 'http://stephanscorner.de/themegraph/keywordsrawmonth/'
    r = requests.get(url)
    data = r.json()
    wordclouddata = data["Keywords"]

    time_mode = "Last Month"

    return render_template('dashboardDWpostings.html', wordclouddata=wordclouddata, time_mode=time_mode)


@blueprint.route('/dashboardDWthemegraphmonth')
def dashboardDWthemegraph_page():
    time_mode = "Last Month"
    return render_template('dashboardDWthemegraph.html', time_mode=time_mode)


# Weekly Postings
@blueprint.route('/dashboardDWpostingsweek')
def dashboardDWpostingsWeek_page():
    url = 'http://stephanscorner.de/themegraph/keywordsrawweek/'
    r = requests.get(url)
    data = r.json()
    wordclouddata = data["Keywords"]
    time_mode = "Last Week"
    return render_template('dashboardDWpostingsweek.html', wordclouddata=wordclouddata, time_mode=time_mode)


@blueprint.route('/dashboardDWthemegraphweek')
def dashboardDWthemegraphWeek_page():
    time_mode = "Last Week"
    return render_template('dashboardDWthemegraphweek.html', time_mode=time_mode)
