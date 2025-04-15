class UserService:
    def __init__(self, db):
        self.db = db

    def register_user(self, user_id, name):
        self.db.add_user(user_id, name)

    def get_user_name(self, user_id):
        return self.db.get_user(user_id)