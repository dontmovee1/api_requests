import os

import requests



HOST="https://release-gs.qa-playground.com/api/v1"
response = requests.post(
    url=f"{HOST}/setup",
    headers={
"Authorization": f"Bearer {os.getenv('API_TOKEN')}",
    }

)
print(response.status_code)