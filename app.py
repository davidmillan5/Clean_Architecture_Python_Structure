from flask import Flask, request, jsonify
from domain.usecase.user.UserCase import UserCase
from infrastructure.drivenadapter.MongoDbRepository.MongoDbRepositoryAdapter import DatabaseAdapter

app = Flask(__name__)

# Initialize the database adapter and use case
db_adapter = DatabaseAdapter('mongodb+srv://cmillan:wmE7VAUHLBQhs2YG@cluster0.vs4hkru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0','users')
user_use_case = UserCase(db_adapter)


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


@app.route('/users', methods=['GET'])
def get_all_users():
    # Get all users from the database using the user use case
    all_users = user_use_case.get_all_users()

    # Convert the list of users into JSON format and return the response
    return jsonify(all_users), 200


if __name__ == '__main__':
    app.run(debug=True)
