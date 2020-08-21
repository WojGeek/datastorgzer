import os
from Pylib.utils import dirs
from Pylib.interface import dialog
from sort import directoryTree



'''
Proyecto: Data storage organizer

    Organize files on any data storage
 
'''
excluded = ['.themes','.config','.thunderbird',     # These are the directories
            '.cache','.local','.sane','.mozilla',   # to ignore when transferring
            '.ssh']                                 # files to the destination.


def directory_choice(msg='Directorio ?'):
        #choice = input('Indique la ruta del directorio: ')
        choice = input(msg)
        return choice

def main():
    print(dirs.isAlive())

    source_path = '/media/willians/_DATA_ntfs_sda3/Willians'
    #source_path = directory_choice('Especifique la ruta del directorio origen: ')

    # Seguro de proseguir?
    #print(f'Ha elegido el {source_path} para organizar')

    destination_path = '/media/willians/32E5585F137BEDC8'
    #destination_path = directory_choice('Indique la ruta destino: ')
    #print(f'Ha indicado como directorio destino la ruta en {destination_path}')

    if dialog.accept():
        #stats = dirs.getList(source_path, excluded, destination_path)
        stats = directoryTree(source_path, excluded, destination_path)
        print(f'Total Sub-directorios: {stats[0]}')
        print(f'Total directorios excluidos: {stats[1]}')


if __name__ == '__main__':
    main() 
