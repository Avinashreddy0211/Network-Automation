import requests

def register(base_url, username, password):
    """
    Registers a new user on the mock API server.
    """
    url = f"{base_url}/register"
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload)

    # If user already exists, API returns 409. Ignore it.
    if response.status_code in [400, 409]:
        print("User already registered. Continuing to login.")
        return

    response.raise_for_status()
    print("User registered successfully.")



def login(base_url, username, password):
    """
    Logs in and returns authentication token.
    """
    url = f"{base_url}/login"
    response = requests.post(url, auth=(username, password))
    response.raise_for_status()

    token = response.json().get("token")
    if not token:
        raise Exception("Login failed: Token not received")

    print("Login successful. Token acquired.")
    return token
