JUNK_EXTENSIONS = {
    ".tmp",
    ".log",
    ".bak",
    ".cache"
}

# 100 MB threshold
LARGE_FILE_THRESHOLD = 100 * 1024 * 1024


def format_size(size_bytes):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return "Unknown size"
