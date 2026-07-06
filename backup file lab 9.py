# backup file
import time
file = input("Enter a file name: ")
with open(file, "rb") as f:
    data = f.read()
timestamp = time.strftime("%Y%m%d_%H%M%S")
backup_file = f"backup_{timestamp}_{file}"
with open(backup_file, "wb") as bf:
    bf.write(data)
print("Backup created:", backup_file)

