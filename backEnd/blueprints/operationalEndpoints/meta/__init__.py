from flask import Blueprint, Response, jsonify, request
from .models import ScrapperDataSchema, UsedKeywordSchema, UsedKeyword_7daysSchema
from .orm import get_all_scrappermeta, add_meta, deleteScrapperbyId, get_all_keywords, get_all_keywords_7days, delete_all_keywords, delete_all_keywords_7days, add_keyword, add_keyword_7days
from extensions import db

import json
import datetime

blueprint = Blueprint('metaapi', __name__, url_prefix='/meta')

scrapperDataSchema = ScrapperDataSchema()
usedKeywordSchema = UsedKeywordSchema()
usedKeyword_7daysSchema = UsedKeyword_7daysSchema()


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
