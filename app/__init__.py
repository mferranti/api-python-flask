# Import flask and template operators
from flask import Flask, render_template, abort, make_response, jsonify

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from redis import Redis

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

redis = Redis()

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Import a module / component using its blueprint handler variable (mod_post)
from app.post.controller import post as post_module

# Register blueprint(s)
app.register_blueprint(post_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
