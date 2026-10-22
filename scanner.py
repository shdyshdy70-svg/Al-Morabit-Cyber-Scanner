import os
import hashlib
from datetime import datetime

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def scan_file(file_path):
    if not os.path.isfile(file_path):
        print("[-] File not found!")
        return

    file_hash = calculate_hash(file_path)

    print("\n========== SCAN REPORT ==========")
    print(f"File: {os.path.basename(file_path)}")
    print(f"SHA256: {file_hash}")
    print(f"Scan time: {datetime.now()}")
    print("Status: File fingerprint calculated")
    print("=================================")


print("=================================")
print("    AL-MORABIT CYBER SCANNER")
print("            Version 1.0")
print("=================================")

path = input("Enter file path to scan: ")
scan_file(path)
