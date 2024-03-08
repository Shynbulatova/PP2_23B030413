# Python Directories and Files exercises
# Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            directories.append(entry)
            all_directories_files.append(entry + " (directory)")
            for sub_entry in os.listdir(full_path):
                all_directories_files.append(os.path.join(entry, sub_entry))
        else:
            files.append(entry)
            all_directories_files.append(entry)

    return directories, files, all_directories_files

path = input("Enter the path: ")

directories, files, all_directories_files = list_directories_files(path)

print("\nDirectories:")
print("\n".join(directories))

print("\nFiles:")
print("\n".join(files))

print("\nAll Directories and Files:")
print("\n".join(all_directories_files))



# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os

def check_access(path):
    access_info = {
        "existence": os.path.exists(path),
        "readability": os.access(path, os.R_OK),
        "writability": os.access(path, os.W_OK),
        "executability": os.access(path, os.X_OK)
    }
    return access_info

path = input("Enter the path: ")

access_info = check_access(path)

print("\nAccess information for", path)
print("Existence:", "Yes" if access_info["existence"] else "No")
print("Readability:", "Yes" if access_info["readability"] else "No")
print("Writability:", "Yes" if access_info["writability"] else "No")
print("Executability:", "Yes" if access_info["executability"] else "No")



# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    else:
        return False, None, None

path = input("Enter the path: ")

exists, filename, directory = path_info(path)

if exists:
    print("Path exists.")
    print("Filename:", filename)
    print("Directory:", directory)
else:
    print("Path does not exist.")



# Write a Python program to count the number of lines in a text file.
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

filename = input("Enter the filename: ")

try:
    line_count = count_lines(filename)
    print("Number of lines in the file:", line_count)
except FileNotFoundError:
    print("File not found.")



# Write a Python program to write a list to a file.
def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

my_list = ["apple", "banana", "orange", "grape"]
filename = input("Enter the filename to write the list to: ")

write_list_to_file(my_list, filename)
print("List has been written to the file.")



# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write(f"This is the content of {filename}.")

generate_files()
print("Text files created successfully.")



# Write a Python program to copy the contents of a file to another file
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)

source_filename = input("Enter the source filename: ")
destination_filename = input("Enter the destination filename: ")

try:
    copy_file(source_filename, destination_filename)
    print("File contents copied successfully.")
except FileNotFoundError:
    print("One or both files not found.")
except IOError:
    print("Error occurred while copying the file contents.")



# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

def check_access(path):
    return os.path.exists(path) and os.access(path, os.W_OK)

def delete_file(path):
    if check_access(path):
        try:
            os.remove(path)
            print("File deleted successfully.")
        except OSError as e:
            print(f"Error: {e.strerror}")
    else:
        print("File cannot be deleted. Access denied or path does not exist.")

file_path = input("Enter the path of the file to delete: ")

delete_file(file_path)
