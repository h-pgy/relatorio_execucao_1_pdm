from .read_xl_data import DataParser
from .config import SHAPEFILE_PATH, OVERWRITE, DE_PARA_SUBS, EPSG
from .utils import open_shp


class DataPrepper:

    DE_PARA_SUBS = DE_PARA_SUBS
    SHAPEFILE_PATH = SHAPEFILE_PATH

    def __init__(self, df = None, geodf=None):

        reader = DataParser(overwrite=OVERWRITE)
        self.read_data = reader

        if geodf is None:
            geodf = open_shp(self.SHAPEFILE_PATH, EPSG)
        self.geodf = geodf

        if df is None:
            df = self.read_data()
        self.df = df

        self.file_names = self.get_filenames(self.df)
        self.cols_not_subs = ('meta_num', 'secretaria', 'obs', 'file_name')

        self.df = self.rename_columns(df)
        self.subs_cols = self.get_subs_cols(self.df)

    def get_filenames(self, df):

        return df['file_name'].unique()
    
    def get_subs_cols(self, df):

        return [col for col in df.columns if col not in self.cols_not_subs]

    def check_de_para_cols(self, df):

        for sub in self.get_subs_cols(df):
            try:
                self.DE_PARA_SUBS[sub]
            except KeyError:
                raise ValueError(f'Subprefeitura {sub} não mapeada! Atualizar configurações.')


    def check_all_subs_present(self, df):

        subs_geo = self.geodf['sp_nome'].unique()
        #aqui preciso buscar novamente as colunas
        subs_df = set(self.get_subs_cols(df))
        for sub in subs_geo:
            if sub not in subs_df:
                raise ValueError(f'Subprefeitura {sub} não encontrada nos dados!')


    def rename_columns(self, df):

        padronizar = {sub : sub.lower().strip() for sub in 
                self.get_subs_cols(df)}

        df = df.rename(padronizar, axis=1)

        self.check_de_para_cols(df)

        df = df.rename(self.DE_PARA_SUBS, axis=1)
        self.check_all_subs_present(df)

        return df

    

    def get_dados_acumulados(self, file_name, df = None):

        if file_name not in self.file_names:
            raise ValueError(f'File name inválido. Valores válidos {self.file_names}')

        if df is None:
            df = self.df

        df_file = df[df['file_name']==file_name].copy()
        df_file = df_file.fillna(0)
        series_acumulados = df_file[self.subs_cols].sum()

        return series_acumulados

    def __call__(self, file_name):

        return self.get_dados_acumulados(file_name)




    

    

