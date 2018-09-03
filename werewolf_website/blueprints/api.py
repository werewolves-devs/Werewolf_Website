from flask import Blueprint, jsonify

bp = Blueprint(__name__, __name__)


@bp.route('/version/')
def list_seasons():
    return jsonify({
        'version': '1.0',
        'deprecated': False,
    })
