import os

path ="./"

file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".py")]

print(f"file list: {file_list}".format(file_list))
print(f"file_list_py: {file_list_py}".format(file_list_py))