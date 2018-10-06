from app.infrastructure.user import UserDataSource
from lib.model.user.user import User
from lib.model.user.user import UserID


class UserFindService:
    def __init__(self):
        self.user_datasource = UserDataSource()

    def find(self, user_id: UserID):
        return self.user_datasource.find(user_id)
