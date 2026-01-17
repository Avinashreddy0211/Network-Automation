def find_vs_by_name(vs_list, target_name):
    """
    Find Virtual Service UUID by its name.
    """
    for vs in vs_list:
        if vs["name"] == target_name:
            print(f"Target Virtual Service found: {target_name}")
            return vs["uuid"]

    raise Exception(f"Virtual Service {target_name} not found")


def validate_vs_enabled(api, uuid, expected_state=True):
    """
    Validate Virtual Service enabled state.
    """
    vs_data = api.get(f"/api/virtualservice/{uuid}")
    actual_s_
