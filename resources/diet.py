from flask import request, jsonify
from flask_restful import Resource
from flask_login import login_required, current_user

from database import db
from models.diet import Diet


class DietResource(Resource):
    @login_required
    def get(self, id=None):
        if id:
            meal = Diet.query.filter_by(id=id, user_id=current_user.id).first()
            if not meal:
                return jsonify({'message': 'Meal not found'}), 404
            return jsonify({
                'id': meal.id,
                'name': meal.name,
                'description': meal.description,
                'created_at': meal.created_at,
                'updated_at': meal.updated_at,
                'off_the_diet': meal.off_the_diet
            })
        else:
            meals = Diet.query.filter_by(user_id=current_user.id).all()
            return jsonify([{
                'id': meal.id,
                'name': meal.name,
                'description': meal.description,
                'created_at': meal.created_at,
                'updated_at': meal.updated_at,
                'off_the_diet': meal.off_the_diet
            } for meal in meals])

    @login_required
    def post(self):
        data = request.json
        new_meal = Diet(
            name=data.get('name'),
            description=data.get('description'),
            off_the_diet=data.get('off_the_diet'),
            user_id=current_user.id
        )
        db.session.add(new_meal)
        db.session.commit()
        return jsonify({'message': 'Meal registered successfully!'}), 201

    @login_required
    def put(self, id):
        data = request.json
        meal = Diet.query.filter_by(id=id, user_id=current_user.id).first()
        if not meal:
            return jsonify({'message': 'Meal not found'}), 404

        meal.name = data.get('name', meal.name)
        meal.description = data.get('description', meal.description)
        meal.off_the_diet = data.get('off_the_diet', meal.off_the_diet)

        db.session.commit()
        return jsonify({'message': 'Meal updated successfully!'})

    @login_required
    def delete(self, id):
        meal = Diet.query.filter_by(id=id, user_id=current_user.id).first()
        if not meal:
            return jsonify({'message': 'Meal not found'}), 404

        db.session.delete(meal)
        db.session.commit()
        return jsonify({'message': 'Meal deleted successfully!'})
