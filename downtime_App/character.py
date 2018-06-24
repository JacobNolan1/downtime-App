import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from downtime_App.db import get_db

bp = Blueprint('character', __name__, url_prefix='/character')

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('character/character/index.html')

@bp.route('/new', methods=['GET'])
def new():
    return render_template('character/character/new.html')

@bp.route('/update', methods=['GET'])
def update():
    return render_template('character/character/update.html')


@bp.route('/view', methods=['GET'])
def view():
    return render_template('character/character/view.html')

@bp.route('/activities', methods=['GET'])
def select_activities():
    return render_template('character/activity_selection/activity_selection.html')
