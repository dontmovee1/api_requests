import allure
import requests
from utils.helper import Helper
from services.payloads import Payloads
from services.endpoints import Endpoints
from config.headers import Headers
from services.users.models.user_model import UserModel

class UserApi(Helper):
    def __init__(self):
        super().__init__()
        self.payloads=Payloads()
        self.endpoints=Endpoints()
        self.headers=Headers()
    @allure.step("Create user")
    def create_user(self):
        response=requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        print(response.json())
        assert response.status_code==200, response.json()
        self.atach_response(response.json())
        model=UserModel(**response.json())
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self,uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.atach_response(response.json())
        model = UserModel(**response.json())
        return model

