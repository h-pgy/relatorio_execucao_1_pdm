from map_generator.read_xl_data import XlDataReader
from map_generator.utils import find_files_recursive
from map_generator.config import DATA_SOURCE_DIR
import os
 
def test_xl_file_name(file):
    
    fname = os.path.split(file)[-1]
    fname = fname.lower().strip()
    files_erradas = ('metas', 'iniciativas', 'controle')
    
    for teste in files_erradas:
        if fname.startswith(teste):
            return False
    
    return True

def get_xl_files(folder = DATA_SOURCE_DIR):
    
    xl_files = find_files_recursive(folder, extension='.xlsx')
    
    correct_files = []
    for file in xl_files:
        
        if test_xl_file_name(file):
            correct_files.append(file)
            
    
    return correct_files


if __name__ == "__main__":

    
    files = get_xl_files(DATA_SOURCE_DIR)
    all_data_yeah = []
    for file in files:
        reader = XlDataReader(file)
        data = reader.parse_all_geodata()
        all_data_yeah.append(data)
        print(f'{file} parseada')
    
    print(data)