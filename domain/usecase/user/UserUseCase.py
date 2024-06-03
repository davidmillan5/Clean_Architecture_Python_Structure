from domain.model import User
from infrastructure.drivenadapter.SQLiteRepository.SQLiteRepositoryAdapter import DatabaseAdapter

class UserUseCase:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter

    def create_user(self, id, name, email, password):
        new_user = User(id, name, email, password)
        self.db_adapter.insert_user(new_user)
        return new_user

    def get_user(self, user_id):
        return self.db_adapter.get_user_by_id(user_id)
