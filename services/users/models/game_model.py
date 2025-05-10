from pydantic import BaseModel
from typing import List

class GameModel(BaseModel):
    category_uuids: List[str]
    price: int
    title: str
    uuid: str

class GameListModel(BaseModel):
    games: List[GameModel]
    meta: dict