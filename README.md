# 📁 Automated File and Folder Generator

## 📜 Description
This Python script automates the creation of directories and files in a specified directory.  Users can configure the number of primary folders, subfolders, and files to generate. Additionally, it provides options to clear existing content before generation and define custom names for folders and files.  

### ⚠️ **Note:** This program has only been tested on Windows 11.
### 🔬 **Intended for Testing:** This tool is mainly for testing purposes. It can be useful for scenarios where multiple folders and files need to be created quickly for development, organization, or other use cases.  

## ✨ Features
- 📂 Create a specified number of primary folders and subfolders.
- 📄 Generate multiple files with customizable names and extensions.
- 🗑️ Clear folder contents before running (optional).
- 📝 Display the directory structure before and after file creation.
- 🔧 Supports defining custom folder names and file extensions.

## ⚙️ Configuration
### The script provides configurable options in the `config` section:

- 🐞 `debug`: Toggle debug print statements.
- 📍 `main_path`: Defines the main directory for file/folder generation.
- 🧹 `clear_folders`: Option to clear contents before creating new files/folders.
- 📂 `primary_folders_num`: Number of primary folders to create.
- 📁 `subfolders_per_primary_num`: Number of subfolders per primary folder.
- 📄 `files_per_folder`: Number of files to generate in each folder.
- 📌 `create_files_in_primaryfolders`: Enable/disable file creation in primary folders.
- 📌 `create_files_in_subfolders`: Enable/disable file creation in subfolders.
- 📁 `primary_folder_names`: List of custom names for primary folders.
- 📂 `subfolders_name`: List of custom names for subfolders.
- 📝 `file_names`: List of possible names for generated files.
- 🔖 `file_extensions`: List of file extensions for generated files.

## 📂 Example Output

### 🛠️ [ Before Creation ]  
📁 `create_here/`  

📌 Creating **1** total primary folder | **1** subfolder | **2** total files  
✅ Done creating all files  

---

### 📂 [ After Creation ]  
📁 `create_here/`  
  ├── 📁 **primary_folder/**  
  │   ├── 📄 **test.txt**  
  │   ├── 📂 **sub_folder/**  
  │       ├── 📄 **example.json**  



## ▶️ Usage
1. ✅ Ensure Python is installed on your system.
2. 🛠️ Modify the configuration variables at the top of the script.
3. 🚀 Run the script using:
   ```sh
   python script.py
