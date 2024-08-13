from flask import request, jsonify
from flask_restful import Resource
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash  # Import para hashing de senha

from database import db  # Certifique-se de importar o db
from models.user import User


class UserResource(Resource):
    def post(self, action):
        if action == 'register':
            return self.register()

        elif action == 'login':
            return self.login()

        elif action == 'logout':
            return self.logout()

        return jsonify({'message': 'Invalid action'}), 400

    @staticmethod
    def register():
        data = request.json

        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'message': 'Username and password required'}), 400

        if User.query.filter_by(username=data.get('username')).first():
            return jsonify({'message': 'Username already exists'}), 409

        hashed_password = generate_password_hash(data.get('password'), method='sha256')
        new_user = User(username=data.get('username'), password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully!'}), 201

    @staticmethod
    def login():
        data = request.json

        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'message': 'Username and password required'}), 400

        user = User.query.filter_by(username=data.get('username')).first()

        if user and check_password_hash(user.password, data.get('password')):
            login_user(user)
            return jsonify({'message': 'Logged in successfully!'}), 200

        return jsonify({'message': 'Invalid credentials'}), 401

    @login_required
    def logout(self):
        logout_user()
        return jsonify({'message': 'Logged out successfully!'}), 200
