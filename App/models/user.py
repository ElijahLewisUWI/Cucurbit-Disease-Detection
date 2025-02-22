from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    uploads = db.relationship('Upload', backref='user', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'email': self.email
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

