import os
from utils import JUNK_EXTENSIONS


def clean_junk_files(directory):
    freed_space = 0

    for root, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in JUNK_EXTENSIONS:
                try:
                    file_path = os.path.join(root, file)
                    size = os.path.getsize(file_path)
                    os.remove(file_path)
                    freed_space += size
                except (OSError, PermissionError):
                    continue

    return freed_space


def delete_selected_large_files(selected_files):
    freed_space = 0

    for file_path, size in selected_files:
        try:
            os.remove(file_path)
            freed_space += size
        except (OSError, PermissionError):
            continue

    return freed_space
