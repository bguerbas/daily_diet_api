from flask import Flask
from database import db
from routes.meal import meal_routes

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
app.register_blueprint(meal_routes)

initialized = False


@app.before_request
def initialize_once():
    global initialized
    if not initialized:
        print('Creating database...')
        with app.app_context():
            db.create_all()
            initialized = True


if __name__ == '__main__':
    initialize_once()
    app.run(debug=True)

