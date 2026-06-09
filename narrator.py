def generate_report(result):
    return (
        f"Status  : {result['status']}\n"
        f"Message : {result['message']}"
    )