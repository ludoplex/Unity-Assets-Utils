import shutil
import os

def flatten(PARENT_FOLDER, TARGET_FOLDER):
	for FILE in os.listdir(TARGET_FOLDER):
		if os.path.isfile(f'{TARGET_FOLDER}/{FILE}'):
			shutil.move(f'{TARGET_FOLDER}/{FILE}', f'{PARENT_FOLDER}/{FILE}')
		else:
			flatten(PARENT_FOLDER, f'{TARGET_FOLDER}/{FILE}')

	os.rmdir(TARGET_FOLDER)

def main():
	PARENT_FOLDER = str(input('Path to Folder: '))

	FLAG = str(input(f'Type YES to flatten folder "{PARENT_FOLDER}": '))

	if FLAG != 'YES':
		print('Process Terminated')
		return

	for FOLDER in os.listdir(PARENT_FOLDER):
		if not os.path.isfile(f'{PARENT_FOLDER}/{FOLDER}'):
			flatten(PARENT_FOLDER, f'{PARENT_FOLDER}/{FOLDER}')

if __name__ == '__main__':
    main()