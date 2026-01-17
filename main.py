import sys
import os
from analyzer import analyze_directory
from cleaner import clean_junk_files, delete_selected_large_files
from utils import format_size


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.exists(directory):
        print("Error: Directory does not exist.")
        sys.exit(1)

    print(f"\nScanning directory: {directory}\n")

    report = analyze_directory(directory)

    print(f"Total files scanned: {report['total_files']}")
    print(f"Total size: {format_size(report['total_size'])}\n")

    print("Top 5 largest files:")
    for idx, (path, size) in enumerate(report['largest_files'], start=1):
        print(f"{idx}. {path} - {format_size(size)}")

    print("\nJunk files found:")
    for ext, size in report['junk_files'].items():
        print(f"{ext} : {format_size(size)}")

    # Junk cleanup
    if report["junk_files"]:
        choice = input("\nDelete junk files? (y/n): ").lower()
        if choice == "y":
            freed = clean_junk_files(directory)
            print(f"Junk cleanup completed. Space freed: {format_size(freed)}")

    # Large file cleanup
    if report["large_files"]:
        print("\nLarge files detected:")
        for i, (path, size) in enumerate(report["large_files"], start=1):
            print(f"{i}. {path} - {format_size(size)}")

        print("\nEnter file numbers to delete (comma-separated), or press Enter to skip:")
        user_input = input("> ").strip()

        if user_input:
            indexes = []
            try:
                indexes = [int(i) - 1 for i in user_input.split(",")]
                selected = [report["large_files"][i] for i in indexes if 0 <= i < len(report["large_files"])]

                freed = delete_selected_large_files(selected)
                print(f"Large file deletion completed. Space freed: {format_size(freed)}")
            except ValueError:
                print("Invalid input. Skipping large file deletion.")

    print("\nOperation completed.")


if __name__ == "__main__":
    main()
