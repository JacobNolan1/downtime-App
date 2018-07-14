import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
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

		
		if characterName != "" and characterDescription != "" and charStr != "" and \
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

		characters = db.execute(
		'SELECT * FROM character'
		).fetchall()
		return render_template('character/character/index.html', characters=characters)

@bp.route('/new', methods=['GET'])
@login_required
def new():
	return render_template('character/character/new.html')

@bp.route('/update/<characterID>', methods=('GET','POST'))
@login_required
def update(characterID):
	db = get_db()
	userID = session.get('user_id')
	#sqlite3.ProgrammingError: Incorrect number of bindings supplied fixed by changing characterID to a tuple (characterID,)
	character = db.execute(
	'SELECT * FROM character WHERE character_id =?',(characterID,) 
	).fetchone()
	if(userID == character['user_id']):
		if request.method == 'GET':
			return render_template('character/character/update.html', character=character)
		if request.method == 'POST':
			characterID = request.form.get('character_ID')
			characterName = request.form.get('character_name')
			characterDescription = request.form.get('character_description')
			charStr = request.form.get('char_str')
			charDex = request.form.get('char_dex')
			charCon = request.form.get('char_con')
			charInt = request.form.get('char_int')
			charWis = request.form.get('char_wis')
			charCha = request.form.get('char_cha')
			db.execute('UPDATE character SET character_name=?, character_description=?, \
				character_str=?, character_dex=?, character_con=?, character_int=?, \
				character_wis=?, character_cha=? WHERE character_id=?',(characterName, characterDescription, charStr, charDex, charCon, charInt, charWis, charCha, characterID))
			db.commit()
			return redirect(url_for('character.index'))
	else:
		#make this call 404 abort
		error = "You are not authorised to access this character"
		flash(error)
		return redirect(url_for('character.index'))	


@bp.route('/view/<characterID>', methods=('GET','POST'))
@login_required
def view(characterID):
	db = get_db()
	userID = session.get('user_id')
	
	#sqlite3.ProgrammingError: Incorrect number of bindings supplied fixed by changing characterID to a tuple (characterID,)
	character = db.execute(
	'SELECT * FROM character WHERE character_id =?',(characterID,) 
	).fetchone()

	if(userID == character['user_id']):
		if request.method == 'GET':
			return render_template('character/character/view.html', character=character)
		if request.method == 'POST':
			if "Update" in request.form:
				return redirect(url_for('character.update', characterID = characterID))	
			elif "Delete" in request.form:
				db.execute('DELETE FROM character WHERE character_id=?',(characterID,))
				db.commit()
			return redirect(url_for('character.index'))	
	else:
		#make this call 404 abort
		error = "You are not authorised to access this character"
		flash(error)
		return redirect(url_for('character.index'))	
	
@bp.route('/activities/<characterID>', methods=('GET','POST'))
@login_required
def select_activities(characterID):
	db = get_db()
	userID = session.get('user_id')
	
	#sqlite3.ProgrammingError: Incorrect number of bindings supplied fixed by changing characterID to a tuple (characterID,)
	character = db.execute(
	'SELECT * FROM character WHERE character_id =?',(characterID,) 
	).fetchone()

	if(userID == character['user_id']):
		if request.method == 'GET':
			return render_template('character/activity_selection/activity_selection.html', character=character)
		if request.method == 'POST':
			return redirect(url_for('character.index'))	
	else:
		#make this call 404 abort
		error = "You are not authorised to access this character"
		flash(error)
		return redirect(url_for('character.index'))	

@bp.route('/activities/ajax', methods=('GET', 'POST'))
def ajax_select_activities2():
	selectedCategory = request.args.get("selected_category")
	selectedActivity = request.args.get("selected_activity")
	return loadActivityTemplate(selectedCategory, selectedActivity)
	return render_template('character/activity_selection/activities/general/training.html')

def loadActivityTemplate(selectedCategory, selectedActivity):
	if selectedCategory == "General":
		generalActivities = {'BuyMagic': 'general/buymagic.html','SellMagic': 'general/sellmagic.html','BuyNonMagic': 'general/buynonmagic.html','SellNonMagic': 'general/sellnonmagic.html', 'Relax': 'general/relax.html', 'Research': 'general/research.html', 'Training': 'general/training.html'}
		return findActivityTemplate(selectedActivity, generalActivities)
	elif selectedCategory == "Job":
		jobActivities = {'Guard': 'job/guard.html'}
		return findActivityTemplate(selectedActivity, jobActivities)
	elif selectedCategory == "Town":
		townActivities = {'Gamble': 'town/gamble.html'}
		return findActivityTemplate(selectedActivity, townActivities)
	elif selectedCategory == "City":
		cityActivities = {'Gamble': 'city/gamble.html'}
		return findActivityTemplate(selectedActivity, cityActivities)
	elif selectedCategory == "Wilderness":
		wildernessActivities = {'Hunt': 'wilderness/hunt.html'}
		return findActivityTemplate(selectedActivity, wildernessActivities)
	elif selectedCategory == "Dungeon":
		dungeonActivities = {'Explore': 'dungeon/explore.html'}
		return findActivityTemplate(selectedActivity, generalActivities)
	else:
		return None

def findActivityTemplate(selectedActivity, activityList):
	for activity in activityList:
		if selectedActivity == activity:
			linkToTemplate = 'character/activity_selection/activities/'+ activityList[activity]
			return render_template(linkToTemplate)
	return None

