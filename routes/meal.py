from flask import Blueprint, request, jsonify, abort
from database import db
from models.meal import Meal

meal_routes = Blueprint('meal_routes', __name__)


@meal_routes.route('/meals', methods=['POST'])
def create_meal():
    data = request.json
    meal = Meal(
        name=data['name'],
        description=data.get('description', ''),
        date_time=data['date_time'],
        in_diet=data['in_diet']
    )
    db.session.add(meal)
    db.session.commit()
    return jsonify({'message': 'Meal created successfully'}), 201


@meal_routes.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = db.session.get(Meal, meal_id)
    if meal is None:
        abort(404)
    return jsonify({
        'name': meal.name,
        'description': meal.description,
        'date_time': meal.date_time,
        'in_diet': meal.in_diet
    })


@meal_routes.route('/meals', methods=['GET'])
def list_meals():
    meals = Meal.query.all()
    return jsonify([{
        'name': meal.name,
        'description': meal.description,
        'date_time': meal.date_time,
        'in_diet': meal.in_diet
    } for meal in meals])


@meal_routes.route('/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    meal = db.session.get(Meal, meal_id)
    if meal is None:
        abort(404)
    data = request.json
    meal.name = data['name']
    meal.description = data.get('description', meal.description)
    meal.date_time = data['date_time']
    meal.in_diet = data['in_diet']
    db.session.commit()
    return jsonify({'message': 'Meal updated successfully'})


@meal_routes.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = db.session.get(Meal, meal_id)
    if meal is None:
        abort(404)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({'message': 'Meal deleted successfully'})
