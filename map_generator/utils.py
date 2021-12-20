import os

def solve_folder(folder, absolut=True):

    if not os.path.exists(folder):
        os.mkdir(folder)
    
    if absolut:
        folder = os.path.abspath(folder)
    return folder

def solve_path(folder, file):

    folder = solve_folder(folder, absolut=False)

    path = os.path.abspath(os.path.join(folder, file))

    return solve_folder(path)

def find_files(folder, extension=None):

    folder = solve_folder(folder)
    files = [solve_path(folder, file) for file in os.listdir(folder)]
    files = [file for file in files if os.path.isfile(file)]
    if extension is None:
        return files

    files_ext = [file for file in files if file.endswith(extension)]

    return files_ext

def list_subfolders(folder):

    subfolders = [
                    os.path.join(folder, subfolder)
                    for subfolder in os.listdir(folder) 
                    if os.path.isdir(
                        os.path.join(folder, subfolder
                        ))
                        ]
    
    return subfolders

def find_files_recursive(folder, files = None, extension=None):

    if files is None:
        files = []

    found_files = find_files(folder, extension=extension)
    files.extend(found_files)
    subfolders = list_subfolders(folder)
    
    for folder in subfolders:

        find_files_recursive(folder, files=files, extension=extension)

    return files


