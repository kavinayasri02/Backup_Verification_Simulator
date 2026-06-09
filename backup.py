import os

BACKUP_FOLDER = "data/backups"


def get_backup_files():
    if not os.path.exists(BACKUP_FOLDER):
        return []

    backup_files = []

    for file in os.listdir(BACKUP_FOLDER):
        path = os.path.join(BACKUP_FOLDER, file)

        if os.path.isfile(path):
            backup_files.append(file)

    return backup_files