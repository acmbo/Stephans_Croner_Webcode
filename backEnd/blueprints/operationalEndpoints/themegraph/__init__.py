from time import time
from flask import Blueprint, jsonify, request, Response
from os.path import exists
import json

from itsdangerous import exc

from .models import ThemeGraphDailySchema, ThemeGraphWeeklySchema, ThemeGraphMonthlySchema
from extensions import db, ThemeGraphDaily, ThemeGraphMonthly, ThemeGraphWeekly
from .orm import get_all_edges, add_edge, deleteedges

blueprint = Blueprint('graphapi', __name__, url_prefix='/themegraph')

themeGraphDailySchema = ThemeGraphDailySchema()
themeGraphWeeklySchema = ThemeGraphWeeklySchema()
themeGraphMonthlySchema = ThemeGraphMonthlySchema()


@blueprint.route('/')
def example():
    # abort(404)
    return '{"test":"Hello World"}'


# Raw Keyword API

@blueprint.route("/keywordsrawweek/", methods=['GET'])
def keywordsrawweek_open():
    if exists('data/kwRawWeek.txt'):
        with open('data/kwRawWeek.txt', 'r') as f:
            content = {"Keywords": f.read()}
        return jsonify(content)
    return jsonify({"Keywords": ""})


@blueprint.route("/keywordsrawmonth/", methods=['GET'])
def keywordsrawmonth_open():
    if exists('data/kwRawMonth.txt'):
        with open('data/kwRawMonth.txt', 'r') as f:
            content = {"Keywords": f.read()}
        return jsonify(content)
    return jsonify({"Keywords": ""})


@blueprint.route("/keywordsrawweek/", methods=['POST', 'DELETE'])
def keywordsrawweek_closed():
    # Here check for right input
    if request.method == 'POST':

        check = True

        if check == True:
            kws = request.form.get('keywords')

            with open('data/kwRawWeek.txt', 'w') as f:
                f.write(kws)

            return "", 204
        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':
        open('data/kwRawWeek.txt', 'w').close()
        return "", 204


@blueprint.route("/keywordsrawmonth/", methods=['POST', 'DELETE'])
def keywordsrawmonth_closed():
    # Here check for right input
    if request.method == 'POST':

        check = True

        if check == True:
            kws = request.form.get('keywords')

            with open('data/kwRawMonth.txt', 'w') as f:
                f.write(kws)

            return "", 204
        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':
        open('data/kwRawMonth.txt', 'w').close()
        return "", 204


# -------------------------- Graphs----------------------------------


@blueprint.route("/themeGraphDaily/", methods=['GET'])
def themeGraphDaily_open():
    """
    Returns:
        json or bad request: scrappermeta information from db
    """
    timeperiod = "daily"

    with open('data/themeGraphDaily.json', 'r') as f:
        data = json.load(f)

    return jsonify(data)


@blueprint.route("/themeGraphDaily/", methods=['POST', 'DELETE'])
def themeGraphDaily_closed():

    # if request.method == 'POST':
    # Here check for right input
    timeperiod = "daily"

    if request.method == 'POST':

        check = True

        data = request.json

        data = json.dumps(data)

        with open('data/themeGraphDaily.json', 'w') as f:
            f.write(data)
        return "", 204

    if request.method == 'DELETE':
        data = {}
        data = json.dumps(data)
        with open('data/themeGraphDaily.json', 'w') as f:
            f.write(data)
        return "", 204


@blueprint.route("/themeGraphMonthly/", methods=['GET'])
def themthemeGraphMonthlyeGraphMonthly_open():
    """
    Returns:
        json or bad request: scrappermeta information from db
    """
    with open('data/themeGraphMonthly.json', 'r') as f:
        data = json.load(f)

    return jsonify(data)


@blueprint.route("/themeGraphMonthly/", methods=['POST', 'DELETE'])
def themeGraphMonthly_closed():

    # if request.method == 'POST':
    # Here check for right input
    timeperiod = "monthly"
    if request.method == 'POST':

        check = True

        data = request.json

        data = json.dumps(data)

        with open('data/themeGraphMonthly.json', 'w') as f:
            f.write(data)
        return "", 204

    if request.method == 'DELETE':
        data = {}
        data = json.dumps(data)
        with open('data/themeGraphMonthly.json', 'w') as f:
            f.write(data)
        return "", 204


@blueprint.route("/themeGraphWeekly/", methods=['GET'])
def themeGraphWeekly_open():
    """
    Returns:
        json or bad request: scrappermeta information from db
    """
    with open('data/themeGraphWeekly.json', 'r') as f:
        data = json.load(f)

    return jsonify(data)


@blueprint.route("/themeGraphWeekly/", methods=['POST', 'DELETE'])
def themeGraphWeekly_closed():

    # if request.method == 'POST':
    # Here check for right input
    timeperiod = "weekly"
    if request.method == 'POST':

        check = True

        data = request.json

        data = json.dumps(data)

        with open('data/themeGraphWeekly.json', 'w') as f:
            f.write(data)
        return "", 204

    if request.method == 'DELETE':
        data = {}
        data = json.dumps(data)
        with open('data/themeGraphWeekly.json', 'w') as f:
            f.write(data)
        return "", 204


@blueprint.route("/testjson/", methods=['GET'])
def testendpoint_open():
    """
    Returns:
        json or bad request: scrappermeta information from db
    """
    try:
        with open('data/testjson.json', 'r') as f:
            data = json.load(f)
    except:
        data = {}

    return jsonify(data)


@blueprint.route("/testjson/", methods=['POST', 'DELETE'])
def testendpoint_closed():

    if request.method == 'POST':

        data = request.json

        data = json.dumps(data)

        with open('data/testjson.json', 'w+') as f:
            f.write(data)
        return "", 204

    if request.method == 'DELETE':
        data = {}
        data = json.dumps(data)
        with open('data/testjson.json', 'w+') as f:
            f.write(data)
        return "", 204
