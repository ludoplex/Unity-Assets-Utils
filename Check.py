import os

currentPath = str(input('Path to Assets: '))
FILTER = str(input('Enter Filter: '))

for FILE in os.listdir(currentPath):
    with open(os.path.join(currentPath, FILE), 'rb') as in_file:
        asset = in_file.read()

    if FILTER.encode('utf-8') in asset:
        file_stats = os.stat(currentPath + '/' + FILE)    
        print(f'{FILE}: {file_stats.st_size / 1024:.2f}KB')