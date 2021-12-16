import os
import pandas as pd

def solve_folder(folder, absolut=True):

    if not os.path.exists(folder):
        os.mkdir(folder)
    
    if absolut:
        folder = os.path.abspath(folder)
    return folder

def solve_path(folder, file):

    folder = solve_folder(folder, absolut=False)

    return os.path.abspath(os.path.join(folder, file))

def find_files(folder, extension=None):

    folder = solve_folder(folder)
    files = [solve_path(folder, file) for file in os.listdir(folder)]
    files = [file for file in files if os.path.isfile(file)]
    if extension is None:
        return files

    files_ext = [file for file in files if file.endswith(extension)]

    return files_ext


