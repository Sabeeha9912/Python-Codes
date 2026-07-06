import os
import re
def search_in_files(directory, pattern):
    found = False
    regex = re.compile(pattern, re.IGNORECASE)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".txt", ".log")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line_number, line in enumerate(f, start=1):
                            if regex.search(line):
                                found = True
                                print(f"[+] {file_path} | Line {line_number}: {line.strip()}")
                except Exception as e:
                    print(f"[!] Cannot read {file_path}: {e}")
    if not found:
        print("[-] No matches found.")
# CHANGE THIS TO YOUR REAL PATH
directory_path = r"C:\Users\YourName\Documents\logs"
search_pattern = "error"
search_in_files(directory_path, search_pattern)
