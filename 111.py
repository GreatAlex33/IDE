import os

print(os.listdir()) # ['SnapchatLoader', 'FBLoader', 'tmp.py', '.gitignore', 'venv', '.git']

if 'tmp.py' not in os.listdir():
    print("Файл отсутствует в данной директории")