from flask import Blueprint, Response, jsonify, request, abort

blueprint = Blueprint('metaapi', __name__, url_prefix='/meta')


@blueprint.route('/')
def example():
    # abort(404)
    return '{"test":"Hello World"}'
