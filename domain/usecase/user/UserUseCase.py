from domain.model import User

class UserUseCase:
    def create_user(self, id, name, email, password):
        new_user = User(id, name, email, password)
        return new_user

