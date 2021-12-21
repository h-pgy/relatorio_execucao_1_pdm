from .utils import solve_folder, solve_path

#define se irá sobrescrever os dados parseados
OVERWRITE = False

#configurações de path

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

#configuracoes subprefeituras

DE_PARA_SUBS = {
    'aricanduva' : 'ARICANDUVA-FORMOSA-CARRAO',
    'butantã' : 'BUTANTA',
    'campo limpo' : 'CAMPO LIMPO',
    'capela do socorro' : 'CAPELA DO SOCORRO',
    'casa verde' : 'CASA VERDE-CACHOEIRINHA',
    'cidade ademar' : 'CIDADE ADEMAR',
    'cidade tiradentes' : 'CIDADE TIRADENTES',
    'ermelino matarazzo' : 'ERMELINO MATARAZZO',
    'freguesia  brasilândia' : 'FREGUESIA-BRASILANDIA',
    'guaianases' : 'GUAIANASES',
    'ipiranga' : 'IPIRANGA',
    'itaim paulista' : 'ITAIM PAULISTA',
    'itaquera' : 'ITAQUERA',
    'jabaquara' : 'JABAQUARA',
    'jaçanã' : 'JACANA-TREMEMBE',
    'lapa' : 'LAPA',
    "m'boi" : "M'BOI MIRIM",
    'mooca' : 'MOOCA',
    'parelheiros' : 'PARELHEIROS',
    'penha' : 'PENHA',
    'perus' : 'PERUS',
    'pinheiros' : 'PINHEIROS',
    'pirituba jaraguá' : 'PIRITUBA-JARAGUA',
    'santana' : 'SANTANA-TUCURUVI',
    'santo amaro' : 'SANTO AMARO',
    'são mateus' : 'SAO MATEUS',
    'são miguel' : 'SAO MIGUEL',
    'sapopemba' : 'SAPOPEMBA',
    'sé' : 'SE',
    'v maria v guilherme' : 'VILA MARIA-VILA GUILHERME',
    'vila mariana' : 'VILA MARIANA',
    'vila prudente' : 'VILA PRUDENTE'
}
