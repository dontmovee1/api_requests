from services.users.api_users import UserApi

class BaseTest:
    def setup_method(self):
        self.api_users = UserApi()