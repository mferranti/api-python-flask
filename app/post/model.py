# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
import jsonpickle
import pickle

# Define a Post model
class Post(db.Model):

    __tablename__ = 'posts'

    id           = db.Column(db.Integer, primary_key=True)
    titulo       = db.Column(db.String(128),  nullable=False)
    categoria    = db.Column(db.String(128),  nullable=False)
    autor        = db.Column(db.Integer, nullable=False)
    fecha_creado = db.Column(db.DateTime,  default=db.func.current_timestamp())
    privado      = db.Column(db.SmallInteger)

    # New instance instantiation procedure
    def __init__(self, id, title, category, owner_id, privacy):

        self.id        = id
        self.titulo    = title
        self.categoria = category
        self.autor     = owner_id
        self.privado   = privacy

    def __repr__(self):
	return pickle.dumps(self)

