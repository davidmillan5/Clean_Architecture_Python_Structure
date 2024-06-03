from pymongo import MongoClient
from domain.model import User


class DatabaseAdapter:
    def __init__(self, connection_string, db_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.users_collection = self.db['users']

    def insert_user(self, user):
        self.users_collection.insert_one({
            'name': user.name,
            'email': user.email,
            'password': user.password
        })

    def get_user_by_id(self, user_id):
        user_data = self.users_collection.find_one({'id': user_id})
        if user_data:
            return User(user_data['id'], user_data['name'], user_data['email'], user_data['password'])
        return None

    def get_all_users(self):
        all_users_data = self.users_collection.find()
        all_users = [User(user['id'], user['name'], user['email'], user['password']) for user in all_users_data]
        return all_users

    def close(self):
        self.client.close()
