from flask import Blueprint, jsonify, request, url_for
from ..database import mongo, abc
from flask_oauth import OAuth
from bson import Binary, Code
from bson.json_util import dumps
import bcrypt
import json
import ast

mod = Blueprint('orderedItems', __name__)

@mod.route('/orderedItems', ['GET', 'POST'])
def getstuff():	
	if request.method == 'GET':
		users = mongo.db.orderedItems.find({})		
		return dumps(users)