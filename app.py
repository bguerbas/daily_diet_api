from flask import Flask
from flask_restful import Api

from database import db
from config import Config
from resources.diet import DietResource
from resources.user import UserResource

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

api = Api(app)

api.add_resource(DietResource, '/meal', '/meal/<int:id>')
api.add_resource(UserResource, '/user/<string:action>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
