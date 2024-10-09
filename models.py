from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://img.freepik.com/free-vector/paw-print-hand-drawn_78370-6307.jpg"

def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.create_all()



class Pet(db.Model):
    """Adoptable pet"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    
    name = db.Column(db.Text,
                     nullable=False)
    
    species = db.Column(db.Text,
                     nullable=False)
    
    photo_url = db.Column(db.String)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    
    def image_url(self):
        """Return image for pet"""

        return self.photo_url or DEFAULT_IMG