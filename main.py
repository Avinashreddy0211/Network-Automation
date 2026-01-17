import yaml
from concurrent.futures import ThreadPoolExecutor

from framework.auth import register, login
from framework.api_client import ApiClient
from framework.executor import run_testcase


def load_yaml(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)


def main():
    # Load configurations
    config = load_yaml("config/config.yaml")
    testcases_config = load_yaml("config/testcases.yaml")

    base_url = config["base_url"]
    username = config["credentials"]["username"]
    password = config["credentials"]["password"]
    target_vs_name = config["target_vs_name"]

    testcases = testcases_config["testcases"]

    # Register and Login
    register(base_url, username, password)
    token = login(base_url, username, password)

    # Initialize API client
    api = ApiClient(base_url, token)

    # Execute testcases in parallel
    with ThreadPoolExecutor(max_workers=len(testcases)) as executor:
        for tc in testcases:
            executor.submit(run_testcase, api, target_vs_name, tc["name"])


if __name__ == "__main__":
    main()
