from datetime import datetime
from pytz import timezone
from incidentlogger import db, login_manager
from flask_login import UserMixin

tz = timezone('EST')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')    
    password = db.Column(db.String(60), nullable=False)
    incidents = db.relationship('Incident', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now(tz))
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.Text, nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    current_assignee = db.Column(db.String(100), nullable=False)
    history = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Incident('{self.title}', '{self.date_posted}')"