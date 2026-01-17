def disable_vs(api, uuid):
    """
    Disable the Virtual Service by sending PUT request.
    """
    payload = {"enabled": False}
    result = api.put(f"/api/virtualservice/{uuid}", payload)
    print(f"VS disabled. Current enabled state: {result['enabled']}")


def ssh_stub():
    """
    Mock SSH connection.
    """
    print("MOCK_SSH: Connecting to host...")


def rdp_stub():
    """
    Mock RDP connection.
    """
    print("MOCK_RDP: Validating remote connection...")
