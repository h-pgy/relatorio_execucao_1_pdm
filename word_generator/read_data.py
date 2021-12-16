import pandas as pd
from .utils import find_files
from .config import DATA_SOURCE_DIR, SHEET_RELATORIO, STRUCTURE_DATA_DIR, SHEET_ESTRUTURA

def solve_data_source_file(path, extension):

    files = find_files(path, extension=extension)

    if not files:
        raise RuntimeError(f'Arquivo de fonte de dados não encontrado no diretorio {path}')

    if len(files)>1:
        raise RuntimeError(f'Mais de um arquivo de fonte de dados encontrado no diretorio {path}')
    
    file = files[0]

    return file

def read_execucao(path=DATA_SOURCE_DIR, sheet_name = SHEET_RELATORIO):
    

    file = solve_data_source_file(path, extension = '.xlsx')
    

    return pd.read_excel(file, sheet_name=sheet_name, skiprows=2)

def read_estrutura_pdm(path = STRUCTURE_DATA_DIR, sheet_name= SHEET_ESTRUTURA):

    file = solve_data_source_file(path, extension = '.xlsx')
    

    return pd.read_excel(file, sheet_name=sheet_name, skiprows=1)
