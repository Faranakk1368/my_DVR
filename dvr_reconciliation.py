def reconcile_data(data):
    """
    Simple reconciliation example.
    For example, fill missing 'status' field withh 'OK'.
    """
    if "status" not in data:
        data["status"] = "OK"
    return data
