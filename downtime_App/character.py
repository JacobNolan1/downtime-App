import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from downtime_App.auth import login_required
from downtime_App.db import get_db

bp = Blueprint('character', __name__, url_prefix='/character')

@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():

	db = get_db()

	if request.method == 'GET':
		characters = db.execute(
		'SELECT * FROM character'
		).fetchall()
		return render_template('character/character/index.html', characters=characters)

	if request.method == 'POST':
		postAction = request.form.get('post_action')
		characterID = request.form.get('character_ID')
		characterName = request.form.get('character_name')
		characterDescription = request.form.get('character_description')
		charStr = request.form.get('char_str')
		charDex = request.form.get('char_dex')
		charCon = request.form.get('char_con')
		charInt = request.form.get('char_int')
		charWis = request.form.get('char_wis')
		charCha = request.form.get('char_cha')
		
		userID = session.get('user_id')

		if postAction == "new":
			if postAction != "" and characterName != "" and characterDescription != "" and charStr != "" and \
				charDex != "" and charCon != "" and charInt != "" and charWis != "" and charCha != "":
				avaliableDowntime = 0
				usedDowntime = 0
				db.execute('INSERT INTO character (user_id, character_name, character_description, character_str, \
					character_dex, character_con, character_int, character_wis, character_cha, \
					avaliable_downtime, used_downtime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)' \
					,(userID, characterName, characterDescription, charStr, charDex, charCon, \
					charInt, charWis, charCha, avaliableDowntime, usedDowntime))
				db.commit()
			else:
				error = "Not all feilds were entered correctly"
				flash(error)
				return redirect(url_for('character.new'))
		return render_template('character/character/index.html')

@bp.route('/new', methods=['GET'])
@login_required
def new():
	return render_template('character/character/new.html')

@bp.route('/update', methods=['GET'])
@login_required
def update():
	return render_template('character/character/update.html')


@bp.route('/view/<characterID>', methods=['GET'])
@login_required
def view(characterID):
	db = get_db()
	userID = session.get('user_id')
	
	#sqlite3.ProgrammingError: Incorrect number of bindings supplied fixed by changing characterID to a tuple (characterID,)
	character = db.execute(
	'SELECT * FROM character WHERE character_id =?',(characterID,) 
	).fetchone()
	if(userID == character['user_id']):
		return render_template('character/character/view.html', character=character)
	else:
		#make this call 404 abort
		error = "You are not authorised to access this character"
		flash(error)
		return redirect(url_for('character.index'))	

@bp.route('/activities', methods=['GET'])
@login_required
def select_activities():
	return render_template('character/activity_selection/activity_selection.html')
