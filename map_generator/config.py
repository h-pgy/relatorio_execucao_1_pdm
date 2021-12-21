from .utils import solve_folder, solve_path

ORIGINAL_DATA_DIR = solve_folder('dados_originais')
DATA_SOURCE_DIR = solve_path(ORIGINAL_DATA_DIR, 'dados_mapas')


GENERATED_DATA_DIR = solve_folder('dados_gerados')
SAVE_MAPS_DIR = solve_path(GENERATED_DATA_DIR, 'mapas_gerados')
SAVE_CSV_DIR = solve_path(GENERATED_DATA_DIR, 'dados_extraidos')

#configuracoes do arquivo de Excel
COL_INICIO = 'K'
COL_FIM = 'AP'
HEADER_ROW = 18
DATA_ROW_RANGE = 20, 32

#shapefile a ser baixado
SHAPEFILE_URL = ('http://download.geosampa.prefeitura.sp.gov.br/PaginasPublicas/'
                'downloadArquivo.aspx?orig=DownloadCamadas&arq='
                '01_Limites Administrativos\\Subprefeituras\\Shapefile\\'
                'SIRGAS_SHP_subprefeitura&arqTipo=Shapefile')

SHAPEFILE_PATH = solve_path(ORIGINAL_DATA_DIR, 'dados_geosampa')
