from flask import Blueprint, jsonify, request, url_for
from ..database import mongo, abc
from flask_oauth import OAuth
from bson import Binary, Code
from bson.json_util import dumps
import bcrypt
import json
import ast

FACEBOOK_APP_ID = '204908786760728'
FACEBOOK_APP_SECRET = 'c21b4d83d095dae720b61eb99e78232b'

mod = Blueprint('route2', __name__)
oauth = OAuth()


@mod.route('/getstuff')
def getstuff():
	obj = {'res': 'success', 'get': 'getstuff'}
	print(abc)
	users = mongo.db.products.find({})
	arr = []
	# for user in users:		
	# 	arr.append(user)		
	# 	print(arr)
	return dumps(users, indent=4, sort_keys=True)

@mod.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		# obj = {'username': 'success', 'get': 'getstuff'}
		# facebook_api = social.facebook.get_api()
		# a = facebook_api.PostUpdate('Success')
		# return jsonify(a)
		ret = mongo.db.users.find({})
		r = ast.literal_eval(dumps(ret))
		return jsonify(r)

	if request.method == 'POST':
		content = request.json
		print(content)	
		# content['password'] = bcrypt.hashpw(content['password'].encode('utf-8'), bcrypt.gensalt(14))
		# mongo.db.users.insert(content)
		user = ast.literal_eval(dumps(mongo.db.users.find({"username": content['username']})))
		res = None
		print(user)
		if bcrypt.hashpw(content['password'].encode('utf-8'), user[0]['password']) == user[0]['password']:
			res = {'success': True}
		else:
			res = {'success': False}
		
		return jsonify(res)
	
	
@mod.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':		
		ret = mongo.db.users.find({})
		print(ret)
		return dumps(ret)

	if request.method == 'POST':
		content = request.json
		print(content)		
		content['password'] = bcrypt.hashpw(content['password'].encode('utf-8'), bcrypt.gensalt(14))
		mongo.db.users.insert(content)
		user = mongo.db.users.find({"username": content['username']})		
		return dumps(user)


