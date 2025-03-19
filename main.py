import os, random



#   _____             __ _        
#  / ____|           / _(_)       
# | |     ___  _ __ | |_ _  __ _  
# | |    / _ \| '_ \|  _| |/ _` | 
# | |___| (_) | | | | | | | (_| | 
#  \_____\___/|_| |_|_| |_|\__, | 
#                           __/ | 
#                          |___/  


# Toggle debug print statements 
debug = False

# Defind main directory path where the folders and files should be created
# This sets the main_path to a folder named "create_here" that should be located in the same directory as this script
main_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "create_here")

# Toggle clearing the contents of the main_path before creating new folders/files
clear_folders = True  

# Number of primary folders to create
primary_folders_num = 1  

# Number of subfolders to create within each primary folder
subfolders_per_primary_num = 1

# Number of files to generate in each folder (both primary and subfolders if enabled)
files_per_folder = 1  

# If True, files will be created inside primary folders
create_files_in_primaryfolders = True

# If True, files will be created inside subfolders
create_files_in_subfolders = True  

# List of names to use for primary folders
# If the first list (empty list `[]`) is used, it defaults to the second list containing predefined folder names
primary_folder_names = [] or ['primary_folder', 'test', 'temp', 'example', 'placeholder', 'sample', 
                              'demo', 'backup', 'archive', 'working', 'trial', 'prototype', 'folder']

# List of names to use for subfolders
# Similar to primary folder names, defaults to the second list if the first list is empty
subfolders_name = [] or ['sub_folder', 'test', 'temp', 'example', 'placeholder', 'sample', 
                         'demo', 'backup', 'archive', 'working', 'trial', 'prototype', 'folder']

# List of possible file names to use when generating files
file_names = [] or ['test', 'temp', 'example', 'placeholder', 'draft', 'sample', 'demo', 
                    'backup', 'archive', 'working', 'trial', 'prototype']

# List of file extensions for generating files
file_extensions = [] or ['txt', 'json', 'js', 'html', 'css', 'csv', 'xml', 'md', 'yml', 
                         'log', 'temp', 'sql']

#   _____             __ _          ____                 
#  / ____|           / _(_)        / __ \                
# | |     ___  _ __ | |_ _  __ _  | |  | |_   _____ _ __ 
# | |    / _ \| '_ \|  _| |/ _` | | |  | \ \ / / _ \ '__|
# | |___| (_) | | | | | | | (_| | | |__| |\ V /  __/ |   
#  \_____\___/|_| |_|_| |_|\__, |  \____/  \_/ \___|_|   
#                           __/ |                        
#                          |___/                         







def convert_backslash_to_forwardslash(input_string):
	return input_string.replace("\\", "/")

def check_file_folder_existence(input_string_path=False):
	if not isinstance(input_string_path, str):
		print(f"Invalid input. Expected a string, got: {type(input_string_path).__name__}")
		return

	if input_string_path == None or input_string_path == '' or input_string_path == False:
		print(f"Status: Invalid | Input String: '{input_string_path}' | Input String Bool: {bool(input_string_path)}")
		return

	if os.path.exists(input_string_path):
		return {"exists": True, "type": f"{'folder' if os.path.isdir(input_string_path) else 'file'}", "path": f"{os.path.abspath(input_string_path)}", "name": f"{os.path.basename(input_string_path)}"}
	else:
		return {"exists": False, "path": f"{os.path.abspath(input_string_path)}", "name": f"{os.path.basename(input_string_path)}"}

def create_folder(folder_name=False, folder_path=False):

	if not isinstance(folder_name, str):
		return {'error': True, 'message': f"input folder_name not string"}

	if folder_name == None or folder_name == '' or folder_name == False:
		return {'error': True, 'message': f"invalid folder_name input"}

	if folder_path == None or folder_path == '' or folder_path == False:
		return {'error': True, 'message': f"invalid folder_path input"}

	if folder_path and not os.path.exists(folder_path):
		return {'error': True, 'message': f"invalid folder path input or folder doesnt exist: '{folder_path}'"}

	full_path = os.path.join(folder_path, folder_name)
	try:
		if not os.path.exists(full_path):
			os.makedirs(full_path, exist_ok=True)
			return {'error': False, 'message': f"successfully created folder '{folder_name}'", 'folder_path': convert_backslash_to_forwardslash(full_path)}
		else:
			return {'error': True, 'message': f"folder exists already: '{folder_name}'"}
	except PermissionError:
		return {'error': True, 'message': f"permission denied. unable to create folder '{folder_name}'"}
	except Exception as error:
		return {'error': True, 'message': f"Error occurred: {error}"}

def delete_folder(folder_path_to_delete=False):
		
	if not isinstance(folder_path_to_delete, str):
		return {'error': True, 'message': "Input folder_path_to_delete not a string."}

	if folder_path == None or folder_path == '' or folder_path == False:
		return {'error': True, 'message': f"invalid folder_path input"}

	if not os.path.isdir(folder_path_to_delete):
		return {'error': True, 'message': f"Folder doesn't exist: '{folder_path_to_delete}'"}

	try:
		for root, dirs, files in os.walk(folder_path_to_delete, topdown=False):
			for file in files:
				file_path = os.path.join(root, file)
				os.remove(file_path)
			for dir in dirs:
				os.rmdir(os.path.join(root, dir))

		os.rmdir(folder_path_to_delete)
		return {'error': False, 'message': "Successfully deleted folder", 'folder_path': convert_backslash_to_forwardslash(folder_path_to_delete)}

	except PermissionError:
		return {'error': True, 'message': f"Permission denied. Unable to delete folder '{folder_path_to_delete}'"}
	except Exception as error:
		return {'error': True, 'message': f"Error occurred: {error}"}

def create_file(file_name, file_path=None):
	if not isinstance(file_name, str):
		return {'error': True, 'message': f"input file_name not string"}
	
	if file_name == None or file_name == '' or file_name == False:
		return {'error': True, 'message': f"invalid file_name input"}

	if file_path == None or file_path == '' or file_path == False:
		return {'error': True, 'message': f"invalid file_path input"}	
	
	if file_path and not os.path.exists(file_path):
		return {'error': True, 'message': f"file path doesn't exist: '{file_path}'"}
	
	full_path = os.path.join(file_path or os.getcwd(), file_name)
	try:
		if not os.path.exists(full_path):
			with open(full_path, 'w') as file:
				pass  # Creates an empty file
			return {'error': False, 'message': f"successfully created file '{file_name}'", 'file_path': convert_backslash_to_forwardslash(full_path)}
		else:
			return {'error': True, 'message': f"file already exists: '{file_name}'"}
	except PermissionError:
		return {'error': True, 'message': f"permission denied. Unable to create file '{file_name}'"}
	except Exception as error:
		return {'error': True, 'message': f"error occurred: {error}"}

def delete_file(file_path):
	if not isinstance(file_path, str):
		return {'error': True, 'message': "input file_path not a string."}

	if file_path == None or file_path == '' or file_path == False:
		return {'error': True, 'message': f"invalid file_path input"}

	if not os.path.isfile(file_path):
		return {'error': True, 'message': f"file doesn't exist: '{file_path}'"}

	try:
		os.remove(file_path)
		return {'error': False, 'message': "successfully deleted file", 'file_path': convert_backslash_to_forwardslash(file_path)}
	except PermissionError:
		return {'error': True, 'message': f"permission denied. Unable to delete file '{file_path}'"}
	except Exception as error:
		return {'error': True, 'message': f"error occurred: {error}"}

def create_file_func(file_list, path_to_create_in):
	file_path_list = []
	if isinstance(file_list, list):
		for file in file_list:
			create_file_result = create_file(file, path_to_create_in)
			if create_file_result['error'] == True:
				if debug:
					print(f"Error: {create_file_result['error']} | Message: {create_file_result['message']}")
			elif create_file_result['error'] == False:
				if debug:
					print(f"Message: {create_file_result['message']} | File Path: {create_file_result['file_path']}")
				file_path_list.append(create_file_result['file_path'])
		if debug:
			print(f"File Path List: {file_path_list}")
		return

	elif isinstance(file_list, str):
		create_file_result = create_file(file_name, path_to_create_in)
		if create_file_result['error'] == True:
			print(f"Error: {create_file_result['error']} | Message: {create_file_result['message']}")

		elif create_file_result['error'] == False:
			print(f"Message: {create_file_result['message']} | File Path: {create_file_result['file_path']}")
			file_path_list.append(create_file_result['file_path'])
		if debug:
			print(f"File Path List: {file_path_list}")
		return

	print(f"Invalid Input type: {type(file_list)}")

def delete_file_func(path_to_file_to_delete):

	delete_file_result = delete_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), path_to_file_to_delete))

	if delete_file_result['error'] == True:
		if debug:
			print(f"Error: {delete_file_result['error']} | Message: {delete_file_result['message']}")

	elif delete_file_result['error'] == False:
		if debug:
			print(f"Message: {delete_file_result['message']} | File Path: {delete_file_result['file_path']}")

def create_folder_func(folder_name_list, create_folder_path):
	folder_path_list = []

	if isinstance(folder_name_list, list):
		for folder_name in folder_name_list:
			create_folder_result = create_folder(folder_name, create_folder_path)
			if create_folder_result['error'] == True:
				if debug:
					print(f"Error: {create_folder_result['error']} | Message: {create_folder_result['message']}")
			elif create_folder_result['error'] == False:
				if debug:
					print(f"Message: {create_folder_result['message']} | Folder Path: {create_folder_result['folder_path']}")
				folder_path_list.append(create_folder_result['folder_path'])
		if debug:
			print(f"Folder Path List: {folder_path_list}")
		return folder_path_list

	elif isinstance(folder_name_list, str):
		create_folder_result = create_folder(folder_name_list, create_folder_path)

		if create_folder_result['error'] == True:
			if debug:
				print(f"Error: {create_folder_result['error']} | Message: {create_folder_result['message']}")
		elif create_folder_result['error'] == False:
			if debug:
				print(f"Message: {create_folder_result['message']} | Folder Path: {create_folder_result['folder_path']}")
			folder_path_list.append(create_folder_result['folder_path'])
		if debug:
			print(f"Folder Path List: {folder_path_list}")
		return folder_path_list

def delete_folder_func(folder_to_delete_path):
	delete_folder_result = delete_folder(folder_path)
	if delete_folder_result['error']:
		print(f"Error: {delete_folder_result['error']} | Message: {delete_folder_result['message']}")
	else:
		print(f"Message: {delete_folder_result['message']} | Folder Path: {delete_folder_result['folder_path']}")

def check_file_folder_existence_func(input_path):
	check_result = check_file_folder_existence(input_path)

	if check_result['exists']:
		print(f"Exists: {check_result['exists']} | Type: {check_result['type']} | Path: {check_result['path']} | {check_result['type']} Name: {check_result['name']}")
	else:
		print(f"Exists: {check_result['exists']} | Path: {check_result['path']} | Name: {check_result['name']}")

def print_script_filepath():
	script_file_path = os.path.abspath(__file__)
	script_file_name = os.path.basename(os.path.abspath(__file__))

	script_directory_path = os.path.dirname(os.path.abspath(__file__))
	script_directory_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

	print(f"Script file name: {script_file_name}")
	print(f"Script directory name: {script_directory_name}\n")

	print(f"Script file path: {script_file_path}")
	print(f"Script directory path: {script_directory_path}")

def format_file_names(file_list):
	final_list = [
		"_".join(entry.split()[:-1]) + f"_{index}{entry.split()[-1]}"
		for index, entry in enumerate(file_list, start=1)
	]

	print("\n[ Final list ]")
	print("\n".join(final_list))

def generate_files(files_to_create, file_names, file_extensions):
	file_count = 0
	file_list = []
	for i in range(1, files_to_create + 1):
		file_count += 1
		random_file = f"{random.choice(file_names)}_{file_count}.{random.choice(file_extensions)}"
		file_list.append(random_file)
	return file_list

def generate_folders(folders_to_create, folder_names):
	folder_count = 0
	folder_list = []
	for i in range(1, folders_to_create + 1):
		folder_count += 1
		random_folder = f"{random.choice(folder_names)}_{folder_count}"
		folder_list.append(random_folder)
	return folder_list

def clear_folder_contents(folder_path):
	# Iterate through each item in the directory
	for entry in os.scandir(folder_path):
		try:
			# If it's a file, delete it
			if entry.is_file():
				os.remove(entry.path)
			# If it's a directory, delete it and its contents
			elif entry.is_dir():
				clear_folder_contents(entry.path)  # Recursively clear subfolders
				os.rmdir(entry.path)  # Remove the empty directory
		except Exception as e:
			if debug:
				print(f"Error deleting {entry.path}: {e}")

	if debug:
		print(f"Contents of '{folder_path}' cleared.")

def print_tree(directory, prefix="", exclude_dirs=None, exclude_files=None, exclude_content_dirs=None):
	if exclude_dirs is None:
		exclude_dirs = set()
	if exclude_files is None:
		exclude_files = set()
	if exclude_content_dirs is None:
		exclude_content_dirs = set()

	items = os.listdir(directory)
	for i, item in enumerate(items):
		path = os.path.join(directory, item)
		is_last = i == len(items) - 1
		connector = "└── " if is_last else "├── "
		new_prefix = prefix + ("	" if is_last else "│   ")
		
		if os.path.isdir(path):
			# Check if directory should be excluded from content listing
			if item in exclude_content_dirs:
				print(prefix + connector + item + "/")
			elif item not in exclude_dirs:
				print(prefix + connector + item + "/")
				print_tree(path, new_prefix, exclude_dirs, exclude_files, exclude_content_dirs)
		else:
			# Skip files specified in exclude_files
			if item not in exclude_files:
				print(prefix + connector + item)


if clear_folders:
    clear_folder_contents(main_path)

print("[ Before creation ]")
exclude_dirs = {}
exclude_files = {}
exclude_content_dirs = {""}
print(f"{os.path.basename(main_path)}/")

print_tree(main_path, exclude_dirs=exclude_dirs, exclude_files=exclude_files, exclude_content_dirs=exclude_content_dirs)
print('\n')



primary_folder_total = primary_folders_num
sub_folder_total = subfolders_per_primary_num * primary_folders_num
file_total = (sub_folder_total * files_per_folder) + primary_folder_total

print(f"Creating {primary_folder_total} total primary folders | {sub_folder_total} subfolders | {file_total} total files")

primary_generated_folders_list = generate_folders(primary_folders_num, primary_folder_names)
primary_folder_path_list = create_folder_func(primary_generated_folders_list, main_path)

for primary_folder_path in primary_folder_path_list:
    sub_generated_folders_list = generate_folders(subfolders_per_primary_num, subfolders_name)
    sub_folder_path_list = create_folder_func(sub_generated_folders_list, primary_folder_path)

    if create_files_in_primaryfolders:
        primary_generated_file_list = generate_files(files_per_folder, file_names, file_extensions)
        create_file_func(primary_generated_file_list, primary_folder_path)

    for subfolder_path in sub_folder_path_list:
        if create_files_in_subfolders:
            sub_generated_file_list = generate_files(files_per_folder, file_names, file_extensions)
            create_file_func(sub_generated_file_list, subfolder_path)

print("Done creating all files")

print("\n\n[ After creation ]")
print(f"{os.path.basename(main_path)}/")
print_tree(main_path, exclude_dirs=exclude_dirs, exclude_files=exclude_files, exclude_content_dirs=exclude_content_dirs)
