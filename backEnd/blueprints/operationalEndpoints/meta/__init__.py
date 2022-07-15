from flask import Blueprint, Response, jsonify, request, abort
from itsdangerous import exc
from .models import ScrapperDataSchema, UsedKeywordSchema
from .orm import get_all_scrappermeta, add_meta, deleteScrapperTable
from extensions import db

import datetime

blueprint = Blueprint('metaapi', __name__, url_prefix='/meta')

scrapperDataSchema = ScrapperDataSchema()


@blueprint.route('/')
def example():
    # abort(404)
    return '{"test":"Hello World"}'


@blueprint.route("/scrapper/", methods=['GET'])
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
        print(request)

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

        status = deleteScrapperTable(db.session)
        return "", 204
