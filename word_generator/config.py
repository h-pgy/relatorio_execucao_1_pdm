from .utils import solve_folder, solve_path

ORIGINAL_DATA_DIR = solve_folder('dados_originais')
DATA_SOURCE_DIR = solve_path(ORIGINAL_DATA_DIR, 'dados_relatorio')
STRUCTURE_DATA_DIR = solve_path(ORIGINAL_DATA_DIR, 'estrutura_pdm')


GENERATED_DATA_DIR = solve_folder('dados_gerados')

SHEET_RELATORIO = 'Relatório'
SHEET_ESTRUTURA = 'principal'