from flask import Blueprint, Response, jsonify, request
from .models import ScrapperDataSchema, UsedKeywordSchema, UsedKeyword_7daysSchema, Postings_weeklySchema, Postings_montlySchema, Postings_yearSchema
from .orm import get_all_scrappermeta, add_meta, deleteScrapperbyId, get_all_keywords, get_all_keywords_7days
from .orm import delete_all_keywords, delete_all_keywords_7days, add_keyword, add_keyword_7days
from .orm import get_all_postings_7days, get_all_postings_Month, add_posting_7days, add_posting_month, delete_all_postings_7days, delete_all_postings_month
from .orm import get_all_postings_Year, add_posting_year, delete_all_postings_year
from extensions import db

import json
import datetime

blueprint = Blueprint('metaapi', __name__, url_prefix='/meta')

scrapperDataSchema = ScrapperDataSchema()
usedKeywordSchema = UsedKeywordSchema()
usedKeyword_7daysSchema = UsedKeyword_7daysSchema()
postings_weeklySchema = Postings_weeklySchema()
postings_montlySchema = Postings_montlySchema()
postings_yearSchema = Postings_yearSchema()


@blueprint.route('/')
def example():
    # abort(404)
    return '{"test":"Hello World"}'


@blueprint.route("/scrapperdata/", methods=['GET'])
def scrappermeta_open():
    """


    Returns:
        json or bad request: scrappermeta information from db
    """
    if request.method == 'GET':

        metainfo = get_all_scrappermeta(db.session)
        metainfo_list = [scrapperDataSchema.dump(info) for info in metainfo]

        return jsonify(metainfo_list)


@blueprint.route("/scrapper/", methods=['POST', 'DELETE'])
def scrappermeta_closed():

    # if request.method == 'POST':
    # Here check for right input
    if request.method == 'POST':

        check = True

        try:
            scrapper_name = request.form.get('name')
            amount_of_db_entries = int(request.form.get('entries'))
            entrydate = datetime.datetime.fromisoformat(
                request.form.get('date'))
            errors = int(request.form.get('errors'))

        except Exception as e:
            print(f'{e}')
            return Response(f"Bad Post",
                            status=400,)

        if check == True:
            add_meta(db.session,
                     scrapper_name,
                     amount_of_db_entries,
                     entrydate,
                     errors)
            return "", 204

        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':
        id = request.form.get('id')
        status = deleteScrapperbyId(db.session, id)
        return "", 204


@blueprint.route("/keywordsmonth/", methods=['GET'])
def keywordsmonth_open():
    """


    Returns:
        json or bad request: scrappermeta information from db
    """
    if request.method == 'GET':

        kwinfo = get_all_keywords(db.session)
        kwinfo_list = [usedKeywordSchema.dump(info) for info in kwinfo]

        return jsonify(kwinfo_list)


@blueprint.route("/keywordsweek/", methods=['GET'])
def keywords7days_open():
    """


    Returns:
        json or bad request: scrappermeta information from db
    """
    if request.method == 'GET':

        kwinfo = get_all_keywords_7days(db.session)
        kwinfo_list = [usedKeyword_7daysSchema.dump(info) for info in kwinfo]

        return jsonify(kwinfo_list)


@blueprint.route("/keywordsmonth/", methods=['POST', 'DELETE'])
def keywordsmonth_closed():

    # if request.method == 'POST':
    # Here check for right input
    if request.method == 'POST':

        check = True

        if check == True:
            data = request.json

            for key, val in data.items():
                add_keyword(db.session,
                            keyword=key,
                            amount_of_uses=val)

            return "", 204

        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':
        status = delete_all_keywords(db.session)
        return "", 204


@blueprint.route("/keywordsweek/", methods=['POST', 'DELETE'])
def keywords7days_closed():

    # if request.method == 'POST':
    # Here check for right input
    if request.method == 'POST':

        check = True

        if check == True:
            data = request.json
            for key, val in data.items():
                add_keyword_7days(db.session,
                                  keyword=key,
                                  amount_of_uses=val)
            return "", 204

        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':
        status = delete_all_keywords_7days(db.session)
        return "", 204


@blueprint.route("/postingsweek/", methods=['GET'])
def postingsweek_open():

    if request.method == 'GET':

        posts = get_all_postings_7days(db.session)
        posts_list = [postings_weeklySchema.dump(info) for info in posts]

        return jsonify(posts_list)


@blueprint.route("/postingsweek/", methods=['POST', 'DELETE'])
def postingsweek_closed():

    if request.method == 'POST':

        check = True

        if check == True:
            post = int(request.form.get('post'))
            date = datetime.datetime.fromisoformat(
                request.form.get('date'))

            add_posting_7days(db.session, post, date)
            return "", 204

        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':
        status = delete_all_postings_7days(db.session)
        return "", 204


@blueprint.route("/postingsmonth/", methods=['GET'])
def postingsmonth_open():

    if request.method == 'GET':

        posts = get_all_postings_Month(db.session)
        posts_list = [postings_weeklySchema.dump(info) for info in posts]

        return jsonify(posts_list)


#get_all_postings_7days, get_all_postings_Month, add_posting_7days, add_posting_month, delete_all_postings_7days, delete_all_postings_month


@blueprint.route("/postingsmonth/", methods=['POST', 'DELETE'])
def ppostingsmonth_closed():

    if request.method == 'POST':

        check = True

        if check == True:
            post = int(request.form.get('post'))
            date = datetime.datetime.fromisoformat(
                request.form.get('date'))

            add_posting_month(db.session, post, date)
            return "", 204

        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':
        status = delete_all_postings_month(db.session)
        return "", 204


@blueprint.route("/postingsyear/", methods=['GET'])
def postingsyear_open():

    if request.method == 'GET':

        posts = get_all_postings_Year(db.session)
        posts_list = [postings_yearSchema.dump(info) for info in posts]

        return jsonify(posts_list)


#get_all_postings_7days, get_all_postings_Month, add_posting_7days, add_posting_month, delete_all_postings_7days, delete_all_postings_month


@blueprint.route("/postingsyear/", methods=['POST', 'DELETE'])
def ppostingsyear_closed():

    if request.method == 'POST':

        check = True

        if check == True:
            post = int(request.form.get('post'))
            date = datetime.datetime.fromisoformat(
                request.form.get('date'))

            add_posting_year(db.session, post, date)
            return "", 204

        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':
        status = delete_all_postings_year(db.session)
        return "", 204
