from flask import Blueprint, Response, jsonify, request, abort

blueprint = Blueprint('graphapi', __name__, url_prefix='/themegraph')


@blueprint.route('/')
def example():
    # abort(404)
    return '{"test":"Hello World"}'
