import os
from utils import JUNK_EXTENSIONS, LARGE_FILE_THRESHOLD


def analyze_directory(directory):
    total_size = 0
    total_files = 0
    largest_files = []
    junk_files = {}
    large_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)

                total_size += size
                total_files += 1

                largest_files.append((file_path, size))

                # Junk file detection
                ext = os.path.splitext(file)[1].lower()
                if ext in JUNK_EXTENSIONS:
                    junk_files[ext] = junk_files.get(ext, 0) + size

                # Large file detection
                if size >= LARGE_FILE_THRESHOLD:
                    large_files.append((file_path, size))

            except (OSError, PermissionError):
                continue

    largest_files.sort(key=lambda x: x[1], reverse=True)
    large_files.sort(key=lambda x: x[1], reverse=True)

    return {
        "total_size": total_size,
        "total_files": total_files,
        "largest_files": largest_files[:5],
        "junk_files": junk_files,
        "large_files": large_files
    }
