from flask import Blueprint, jsonify

mod = Blueprint('route1', __name__)

@mod.route('/home')
def home():
	obj = {'res': 'success'}
	return jsonify(obj)