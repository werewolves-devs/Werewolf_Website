from flask import Blueprint, render_template

bp = Blueprint(__name__, __name__)


@bp.route('/')
def list_seasons():
    return render_template('season/list.html')
