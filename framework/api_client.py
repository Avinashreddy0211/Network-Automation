import requests

class ApiClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()
