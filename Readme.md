# Disk Usage Analyzer & Cleaner

## 1. Problem Statement
Over time, a system accumulates unnecessary temporary files, log files, backup files, cached data, and large unused files such as old installers, archives, and media files. These files consume significant disk space and are often scattered across directories, making manual identification and cleanup inefficient and error-prone.

I personally face this issue while working on multiple projects and frequently downloading large files. Manually scanning folders to identify junk files or large unused files is time-consuming and risky. This motivated me to create a simple command-line utility that can analyze disk usage and allow safe, controlled cleanup.

---

## 2. Solution Overview
This project is a command-line based disk analysis and cleanup tool that:
- Scans a given directory recursively
- Calculates total disk usage and file count
- Identifies the largest files in the directory
- Detects common junk files (temporary, log, cache files)
- Safely deletes junk files after user confirmation
- Allows **careful, user-selected deletion of large files**

The tool uses only Python standard libraries and emphasizes safety, clarity, and user control.

---

## 3. Features
- Recursive directory scanning
- Total file count and size calculation
- Top 5 largest files detection
- Junk file identification based on file extensions
- Interactive junk file deletion
- **Large file detection based on size threshold**
- **Manual selection of large files for deletion**
- Cross-platform support (Windows / Linux / macOS)

---

## 4. Technologies Used
- Programming Language: **Python 3**
- Standard Libraries Used:
  - `os`
  - `sys`
  - `pathlib`

---

## 5. How to Run the Program


### Step 1: Ensure Python is Installed
Check Python installation: python --version

---

### Step 2: Navigate to Project Directory
cd D:\Path

### Step 3: Run the Program
python main.py <directory_path>

Or to scan the current directory: python main.py .
