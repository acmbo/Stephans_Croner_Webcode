""" Website Homepage templates
"""

from flask import Blueprint, render_template, request

from extensions import db
from ..operationalEndpoints.meta.models import ScrapperDataSchema, UsedKeywordSchema
from ..operationalEndpoints.meta.orm import get_all_scrappermeta, add_meta, deleteScrapperbyId, get_all_scrappermeta_by_timeframe
from functools import lru_cache
import datetime
import requests

blueprint = Blueprint('Homepage', __name__)

scrapperDataSchema = ScrapperDataSchema()

@lru_cache(maxsize=2)
def get_last_update(day):
    """Get current data of datetime. Uses cache for performance saving.

    Args:
        currentdayofmonth (int): current day of the month as int.

    Returns:
        str: Description how much time passed as string
    """
    # Add Data for Table and Submission section
    metainfo = get_all_scrappermeta_by_timeframe(db.session, days=7)
    metainfo_list = [scrapperDataSchema.dump(info) for info in metainfo]
    metainfo_list.reverse()
    
    if len(metainfo_list) > 0:
        submissionInfo = metainfo_list[0]

        timedelta = datetime.datetime.now() - \
            datetime.datetime.fromisoformat(submissionInfo['entrydate'])

        return str(timedelta.days) + " days ago"
    else:
        
        return "No Data"



@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template('index.html')


@blueprint.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == 'GET':
        return render_template('contact.html')
    
    elif request.method == 'POST':
        print(request.form)
        return render_template('statusTemplates/contact.html')



@blueprint.route('/about')
def about_page():
    return render_template('about.html')


@blueprint.route('/dashboardDW')
def dashboardDW_page():
    metainfo = get_all_scrappermeta_by_timeframe(db.session, days=7)
    # Add Data for Table and Submission section    metainfo = get_all_scrappermeta_by_timeframe(db.session, days=7)
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




@blueprint.route('/dashboardDWabout')
def dashboardDWabout_page():
    return render_template('dashboardDWabout.html')



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
    
    lastupdate = str(get_last_update(datetime.datetime.now().day))
        
    url = 'http://stephanscorner.de/themegraph/keywordsrawmonth/'
    r = requests.get(url)
    data = r.json()
    wordclouddata = data["Keywords"]

    time_mode = "Last Month"

    return render_template('dashboardDWpostings.html', wordclouddata=wordclouddata, time_mode=time_mode, lastupdate=lastupdate)


@blueprint.route('/dashboardDWthemegraphmonth')
def dashboardDWthemegraph_page():
    lastupdate = str(get_last_update(datetime.datetime.now().day))
        
    time_mode = "Last Month"
    return render_template('dashboardDWthemegraph.html', time_mode=time_mode, lastupdate=lastupdate)


# Weekly Postings
@blueprint.route('/dashboardDWpostingsweek')
def dashboardDWpostingsWeek_page():
    
    lastupdate = str(get_last_update(datetime.datetime.now().day))
    
    url = 'http://stephanscorner.de/themegraph/keywordsrawweek/'
    r = requests.get(url)
    data = r.json()
    wordclouddata = data["Keywords"]
    time_mode = "Last Week"
    return render_template('dashboardDWpostings.html', wordclouddata=wordclouddata, time_mode=time_mode, lastupdate=lastupdate)


@blueprint.route('/dashboardDWthemegraphweek')
def dashboardDWthemegraphWeek_page():
    lastupdate = str(get_last_update(datetime.datetime.now().day))        
    time_mode = "Last Week"
    return render_template('dashboardDWthemegraph.html', time_mode=time_mode, lastupdate=lastupdate)
