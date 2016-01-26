# Import flask dependencies
from flask import Blueprint, request, jsonify, abort, make_response, render_template
import jsonpickle, pickle, sys

# Import the database object from the main app module
from app import db
from app import redis

# Import module models (i.e. User)
from app.post.model import Post

# Define the blueprint: 'auth', set its url prefix: app.url/auth
post = Blueprint('post', __name__, url_prefix='/post')

# Set the route and accepted methods
@post.route('/view/<int:post_id>', methods=['GET'])
def get_post(post_id):

    rpost = redis.get(str(post_id))
    rpost = None       
    if rpost is None:
        post = Post.query.filter_by(id = post_id).first()
        if post is None:
            abort(404)
        redis.set(str(post_id), pickle.dumps(post)) 
    else:
        post = pickle.loads(rpost)

    return get_view(post)

def get_view(post):
    view = {
	'id'       : post.id,
	'title'    : post.titulo,
	'category' : post.categoria,
	'owner_id' : post.autor,
	'privacy'  : post.privado,
    }
    
    return jsonify(view)
