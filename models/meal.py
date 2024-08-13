from datetime import datetime
from database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    in_diet = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Meal {self.name}>'



