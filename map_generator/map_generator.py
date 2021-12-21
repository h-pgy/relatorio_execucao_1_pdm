from map_generator.data_prep import DataPrepper
from map_generator.download_shape import DownloadGeosampa
from map_generator.utils import open_shp
from map_generator.config import SHAPEFILE_PATH, EPSG, SAVE_MAPS_DIR
import pandas as pd
import matplotlib.pyplot as plt
import os
from functools import partial


def cmap_plot(geodf, col, fname, fpath, base_layer=None):

    fig, ax = plt.subplots(figsize=(10, 15))

    if geodf[col].max() < 8:
        geodf.plot(ax = ax, column=col, cmap='Blues',
                    legend=True,
                    edgecolor='0.5',
                    vmin=0)
    else:
        geodf.plot(ax = ax, column=col, cmap='Blues',
                    legend=True,
                    edgecolor='0.5',
                    legend_kwds = {'format':"%.0f"},
                    vmin=0)

    if base_layer is not None:
        base_layer['geometry'].boundary.plot(ax=ax,
                        color='black')

    plt.axis('off')

    fig.savefig(os.path.join(fpath, fname))

    plt.clf()
    plt.close(fig)


class MapGenerator:

    SAVE_MAPS_DIR = SAVE_MAPS_DIR

    def __init__(self):

        self.geodf = self.get_shp_file()
        self.prepp_data = DataPrepper(geodf=self.geodf)
        self.file_names = self.prepp_data.file_names
        self.plot_map = partial(cmap_plot,col='valor_acumulado')

    def get_shp_file(self):

        shp = open_shp(SHAPEFILE_PATH, EPSG)
        if shp is None:
            self.download_shp = DownloadGeosampa()
            self.download_shp()
        shp = open_shp(SHAPEFILE_PATH, EPSG)

        return shp

    def get_data(self, file_name):

        data = self.prepp_data(file_name)
        #transforming series into dataframe
        data = data.reset_index()
        data = data.rename({'index' : 'sp_nome',
                        0 : 'valor_acumulado'}, axis = 1)

        return data
    
    def merge_data(self, data):

        merged = pd.merge(self.geodf, data, on ='sp_nome')

        return merged

    def plot_data(self, file_name):

        data = self.get_data(file_name)
        merged = self.merge_data(data)

        self.plot_map(geodf=merged, fname=file_name, 
                    fpath=self.SAVE_MAPS_DIR)



    