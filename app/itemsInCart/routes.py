from flask import Blueprint, jsonify, request, url_for
from ..database import mongo, abc
from flask_oauth import OAuth
from bson import Binary, Code
from bson.json_util import dumps
import bcrypt
import json
import ast


mod = Blueprint('cartItems', __name__)

@mod.route('/addToCart', methods=['GET', 'POST'])
def addToCart():
	if request.method == 'GET':		
		ret = mongo.db.itemsInCart.find({})
		print(ret)
		r = ast.literal_eval(dumps(ret))
		return jsonify(r)

	if request.method == 'POST':
		content = request.json
		print(content)
		res = ast.literal_eval(dumps(mongo.db.itemsInCart.find({"username": content['username'], "objId": content['objId']})))
		length = len(res)
		if length > 0:			
			mongo.db.itemsInCart.update({"username": content['username'], "objId": content['objId']}, {'$set': {"quantity": content['quantity']}})
		else:
			mongo.db.itemsInCart.insert_one({"username": content['username'], "objId": content['objId'], "quantity": content['quantity']})
			# res = ast.literal_eval(dumps())
			
		return jsonify(res)
	
