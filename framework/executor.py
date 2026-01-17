from framework.prefetch import prefetch_resources
from framework.validations import find_vs_by_name, validate_vs_enabled
from framework.tasks import disable_vs, ssh_stub, rdp_stub


def run_testcase(api, target_vs_name, testcase_name):
    print(f"\n===== Running Testcase: {testcase_name} =====")

    # Pre-Fetch Stage
    vs_list = prefetch_resources(api)

    # Pre-Validation Stage
    uuid = find_vs_by_name(vs_list, target_vs_name)
    validate_vs_enabled(api, uuid, expected_state=True)

    # Mock SSH and RDP checks
    ssh_stub()
    rdp_stub()

    # Task / Trigger Stage
    disable_vs(api, uuid)

    # Post-Validation Stage
    validate_vs_enabled(api, uuid, expected_state=False)

    print(f"===== Testcase {testcase_name} Completed Successfully =====\n")
