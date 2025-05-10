
import os
from dotenv import load_dotenv

load_dotenv()

class Headers:
    basic = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "API-1"
    }
    search={
            "Authorization": f"Bearer {os.getenv('SEARCH_TOKEN')}",
            "X-Task-Id": "API-2"
    }