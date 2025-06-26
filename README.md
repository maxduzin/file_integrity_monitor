# 🛡️ File Integrity Monitor

A simple Python script that monitors any file for unauthorized changes using SHA-256 hashing.

---

## 🔍 How It Works

- You provide the full path to a file.
- The script calculates its initial hash.
- Every few seconds, it re-checks the hash.
- If the hash changes, it alerts you.

---

## 💻 Usage

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/file_integrity_monitor.git
cd file_integrity_monitor
