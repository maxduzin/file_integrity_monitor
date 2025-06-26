"""
File Integrity Monitor
Author: Your Name

This script monitors a file for changes by comparing its hash over time.
If the hash changes, it alerts the user that the file has been modified.
"""

import hashlib
import time
import os
import sys

def hash_file(filepath):
    """Compute SHA-256 hash of a file."""
    try:
        with open(filepath, "rb") as f:
            file_hash = hashlib.sha256()
            while chunk := f.read(4096):
                file_hash.update(chunk)
            return file_hash.hexdigest()
    except FileNotFoundError:
        print(f"[X] File not found: {filepath}")
        return None
    except PermissionError:
        print(f"[X] Permission denied when accessing: {filepath}")
        return None

def monitor_file(filepath, interval=2):
    """Monitor a file and alert if it changes."""
    print(f"[*] Monitoring file: {filepath}")
    print(f"[*] Press Ctrl+C to stop\n")

    original_hash = hash_file(filepath)
    if not original_hash:
        return

    print(f"[+] Initial hash: {original_hash}")

    try:
        while True:
            current_hash = hash_file(filepath)
            if not current_hash:
                break
            if current_hash != original_hash:
                print(f"[!] File has been modified! New hash: {current_hash}")
                original_hash = current_hash
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[+] Monitoring stopped by user.")

def main():
    print("=== File Integrity Monitor ===")
    filepath = input("Enter the full path to the file to monitor: ").strip()

    if not os.path.isfile(filepath):
        print(f"[X] Error: {filepath} is not a valid file.")
        return

    monitor_file(filepath)

if __name__ == "__main__":
    main()
