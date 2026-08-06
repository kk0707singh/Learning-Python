# create a new directory:
import os
# new_directory = "package"
# os.mkdir(new_directory)
# print(f'new {new_directory} directory created')

# listing all the files and directory:
items = os.listdir(".")
print(items)

# joining path:
dir_name = "folder"
file_name = "file.py"
full_path = os.path.join(dir_name,file_name)
print(full_path)


dir_name = "folder"
file_name = "file.py"
full_path = os.path.join(os.getcwd(), dir_name,file_name)
print(full_path)


# check for file path exists or not:
path = 'example1.txt'
if os.path.exists(path):
    print(f'this file {path} exists')
else:
    print(f'this file {path} doesnt exists')



# checking if a path is a file or a directory:
path = '/Users/a2251/Desktop/Python Programing/Chapter-12-File-Handeling/example.txt'
if os.path.isfile(path):
    print(f'the path {path} is a file')
elif os.path.isdir(path):
    print(f'the path {path} is a directory')
else:
    print(f'the path {path} is neither a file nor a directory')