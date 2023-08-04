import os

CHECK = str(input('Enter new Path: '))
CACHE = str(input('Enter old Path: '))

for FILE in os.listdir(CHECK):
	if os.path.exists(f'{CACHE}/{FILE}'):
		os.remove(f'{CHECK}/{FILE}')