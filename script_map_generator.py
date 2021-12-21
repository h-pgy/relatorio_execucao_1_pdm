from map_generator import MapGenerator

if __name__ == "__main__":


    print('Iniciando script!')
    mapgen = MapGenerator()

    for file in mapgen.file_names:
        print(f'Plotando arquivo {file}')
        mapgen.plot_data(file)
        
    print('Script finalizado!')