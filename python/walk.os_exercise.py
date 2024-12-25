import os

for path, dirs, files in os.walk(r'C:\Users\Orel\OneDrive\שולחן העבודה\DevOps\git repositories'):
    for file in files:
        full_path = os.path.join(path, file)
        print(full_path)