import requests
from io import BytesIO
from zipfile import ZipFile
from functools import partial
from .utils import find_files_recursive
from .config import SHAPEFILE_URL, SHAPEFILE_PATH

class DownloadGeosampa:

    url = SHAPEFILE_URL
    extract_path = SHAPEFILE_PATH

    def __init__(self):

        self.find_shape = partial(find_files_recursive, extension='.shp')

    def download(self, url=None):

        if url is None:
            url = self.url
        
        with requests.get(url) as r:
            if not r.status_code == 200:
                raise RuntimeError('Não conseguiu fazer o download do shapefile.'
                                f'Baixar e extrair ele manualmente no diretório {SHAPEFILE_PATH}')
            download = r.content
        
        return download
    
    def unzip(self, download_content, extract_path = None):

        if extract_path is None:
            extract_path = self.extract_path

        io = BytesIO(download_content)
        zip_file = ZipFile(io)
        zip_file.extractall(extract_path)

        print(f'Arquivos baixados e extraídos com sucesso no diretório: {extract_path}')

    def check_if_already_saved(self, path = None):

        if path is None:
            path = self.extract_path

        shps = self.find_shape(path)

        if len(shps)>0:
            return True
        return False

    def __call__(self):

        if not self.check_if_already_saved():
            print(f'Nenhum arquivo shape encontrado em {self.extract_path}',
                'Iniciando o download.')
            content = self.download()
            self.unzip(content)
        else:
            print(f'Arquivo shape encontrado em {self.extract_path}',
                'Download não será realizado.')