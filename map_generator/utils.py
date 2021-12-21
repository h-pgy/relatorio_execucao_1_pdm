import os
import geopandas as gpd

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


def number_to_letter(number):
    
    if number < 1:
        return ValueError(f'Deve ser maior que 1')
    
    number = number-1
        
    col_letters = (
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        )
    
    number_of_letters = len(col_letters)
    
    if number < number_of_letters:
        return col_letters[number]
    
    
    floor = number//number_of_letters
    if floor > number_of_letters:
        raise NotImplementedError('Maior valor é ZZ')
    rest = number%number_of_letters
    
    letras = [
        col_letters[floor-1],
        col_letters[rest]
    ]
    
    return ''.join(letras)
    
def letter_to_number(letter):
    
    col_letters = (
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        )
    
    letter = list(letter)
    if len(letter)>2:
        raise NotImplementedError('Maior valor é ZZ')
    letter.reverse()
    total = 0
    for i, char in enumerate(letter):
        letter_index = col_letters.index(char)+1
        if i == 0:
            total+=letter_index
        val = i*letter_index * 26
        total += val
    
    return total

def gen_col_range(col_inicio, col_fim):
        
        col_ini_num = letter_to_number(col_inicio)
        col_fim_num = letter_to_number(col_fim)
        
        num_range  = range(col_ini_num, col_fim_num+1)
        
        return [number_to_letter(num) for num in num_range]

def open_shp(path, epsg):

    shp = find_files_recursive(path, extension='.shp')[0]
    geo_df = gpd.read_file(shp)
    geo_df = geo_df.set_crs(epsg=epsg)

    return geo_df

