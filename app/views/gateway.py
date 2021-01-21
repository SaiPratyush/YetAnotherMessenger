"""Gateway for server."""

from flask import request, jsonify, Blueprint

gateway_bp = Blueprint('gateway', __name__)


@gateway_bp.route('/signup', methods=['POST'])
def signup():
    """
    returns acknowledgement of success or failure of signup
    :return: json
    """
    json = request.get_json()
    print(json)

    return jsonify({'you sent this': json['text']})
