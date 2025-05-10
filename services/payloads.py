from faker import Faker
import uuid

fake=Faker()


class Payloads:
    create_user={
  "email": fake.email(),
  "password": fake.password(length=10),
  "name": fake.first_name(),
  "nickname": fake.user_name()
}
class GamePayloads:
        @property
        def game(self):
            return {
                "category_uuids": [str(uuid.uuid4())],
                "price": fake.random_number(digits=4),
                "title": fake.catch_phrase(),
                "uuid": str(uuid.uuid4())
            }