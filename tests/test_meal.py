import pytest
from app import app, db
from models.meal import Meal


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_create_meal(client):
    response = client.post('/meals', json={
        'name': 'Salada',
        'description': 'Salada de frutas',
        'date_time': '2024-08-13T12:00:00',
        'in_diet': True
    })
    assert response.status_code == 201


def test_get_meal(client):
    with app.app_context():
        meal = Meal(name='Salada', description='Salada de frutas', in_diet=True)
        db.session.add(meal)
        db.session.commit()

        meal_id = meal.id

    with app.app_context():
        # Usando Session.get() em vez de Meal.query.get()
        meal = db.session.get(Meal, meal_id)

    response = client.get(f'/meals/{meal_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Salada'


def test_update_meal(client):
    with app.app_context():
        meal = Meal(name='Salada', description='Salada de frutas', in_diet=True)
        db.session.add(meal)
        db.session.commit()

        meal_id = meal.id

    with app.app_context():
        # Usando Session.get() em vez de Meal.query.get()
        meal = db.session.get(Meal, meal_id)

    response = client.put(f'/meals/{meal_id}', json={
        'name': 'Salada Atualizada',
        'description': 'Salada de frutas com mel',
        'date_time': '2024-08-13T12:00:00',
        'in_diet': False
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Meal updated successfully'


def test_delete_meal(client):
    with app.app_context():
        meal = Meal(name='Salada', description='Salada de frutas', in_diet=True)
        db.session.add(meal)
        db.session.commit()

        meal_id = meal.id

    with app.app_context():
        # Usando Session.get() em vez de Meal.query.get()
        meal = db.session.get(Meal, meal_id)

    response = client.delete(f'/meals/{meal_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Meal deleted successfully'
