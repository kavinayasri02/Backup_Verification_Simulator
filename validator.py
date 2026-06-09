def validate_backups(files):
    if len(files) == 0:
        return {
            "status": "FAILED",
            "message": "No backup files found."
        }

    return {
        "status": "SUCCESS",
        "message": f"{len(files)} backup file(s) found."
    }