import os
import platform
import subprocess
import cat_service

def main():
	print_the_header()

	folder = get_or_create_output_folder()
	print('Found or created folder: ' + folder)
	download_cats(folder)
	display_cats(folder)



def print_the_header():
	print('\n----------------------------')
	print('          LOL CATZ')
	print('----------------------------')


def get_or_create_output_folder():
	base_folder = os.path.dirname(__file__)
	folder = 'cat_pictures'
	full_path = os.path.join(base_folder, folder)

	if not os.path.exists(full_path) or not os.path.isdir(full_path):
		print('Creating new directory at {}'.format(full_path))
		os.mkdir(full_path)

	return full_path


def download_cats(folder):
	print('Contacting server to download cats...')
	cat_count = 30

	for i in range(1, cat_count+1):
		name = 'lolcat_{}'.format(i)
		print('Downloading cat ' + name)
		cat_service.get_cat(folder, name)
	print('Done')


def display_cats(folder):
	# open folder
	print('Dispaying cats in OS window.')
	print(folder)
	print(platform.system())
	if platform.system() == 'Darwin':
		subprocess.call(['open', folder])
	elif platform.system() == 'Windows':
		subprocess.call(['explorer', folder])
	elif platform.system() == 'Linux':
		subprocess.call(['xdg-open', folder])
	else:
		print("We don't support your os: " + platform.system())


if __name__ == '__main__':
	main()
