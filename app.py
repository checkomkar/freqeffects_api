from flask import Blueprint, jsonify

from app import app
app.run(host='0.0.0.0', port=8000, debug=True)