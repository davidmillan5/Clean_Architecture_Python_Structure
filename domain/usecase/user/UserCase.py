from domain.model import User


class UserCase:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter

    def create_user(self, id, name, email, password):
        new_user = User(id, name, email, password)
        self.db_adapter.insert_user(new_user)
        return new_user

    def get_user(self, user_id):
        return self.db_adapter.get_user_by_id(user_id)

    def get_all_users(self):
        return self.db_adapter.get_all_users()
