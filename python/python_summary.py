import os

def count_files(directory):
    file_count = 0
    for root, dirs, files in os.walk(directory):
        file_count += len(files)
    return file_count

directory = r'C:\Users\Orel\OneDrive\שולחן העבודה\DevOps\git repositories'
print(count_files(directory))

