def prefetch_resources(api):
    """
    Fetch tenants, virtual services, and service engines.
    Print counts as part of pre-fetch stage.
    """
    tenants = api.get("/api/tenant")["results"]
    virtual_services = api.get("/api/virtualservice")["results"]
    service_engines = api.get("/api/serviceengine")["results"]

    print(f"Tenants fetched: {len(tenants)}")
    print(f"Virtual Services fetched: {len(virtual_services)}")
    print(f"Service Engines fetched: {len(service_engines)}")

    return virtual_services
