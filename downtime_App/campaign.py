import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from downtime_App.db import get_db

bp = Blueprint('campaign', __name__, url_prefix='/campaign')

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('campaign/index.html')

@bp.route('/new', methods=['GET'])
def new():
    return render_template('campaign/new.html')

@bp.route('/update', methods=['GET'])
def update():
    return render_template('campaign/update.html')


@bp.route('/view', methods=['GET'])
def view():
    return render_template('campaign/view.html')

@bp.route('/new_downtime', methods=['GET'])
def new_downtime():
    return render_template('campaign/downtime/new.html')

@bp.route('/update_downtime', methods=['GET'])
def update_downtime():
    return render_template('campaign/downtime/update.html')
