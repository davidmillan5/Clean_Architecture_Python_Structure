from flask import Flask, request, jsonify
from domain.usecase.user import UserUseCase
from infrastructure.drivenadapter.SQLiteRepository.SQLiteRepositoryAdapter import DatabaseAdapter

app = Flask(__name__)

# Initialize the database adapter and use case
db_adapter = DatabaseAdapter('users.db')
user_use_case = UserUseCase


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = user_use_case.create_user(
        id=data['id'],
        name=data['name'],
        email=data['email'],
        password=data['password']
    )
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'password': user.password
    }), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_use_case.get_user(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password
        })
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
