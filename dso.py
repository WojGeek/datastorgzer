import os
from Pylib.utils import dirs
from Pylib.interface import dialog


'''
Proyecto: Data storage arrangement

    Organize files on any data storage
 
'''
excluded = ['.themes','.config',
            '.thunderbird','.cache',
            '.local','.sane','.mozilla',
            '.ssh']

def directory_choice():
        choice = input('Indique la ruta del directorio: ')
        return choice

def main():
    print(dirs.isAlive())

    dir_path = '/home/wp/msa'
    #dir_path = directory_choice()

    # Seguro de proseguir?
    print(f'Ha elegido el {dir_path} para organizar')

    dest_path = '/tmp/'
    print(f'Ha indicado como directorio destino la ruta en {dest_path}')

    if dialog.accept():
        stats = dirs.getList(dir_path, excluded, dest_path)
        print(f'Total Sub-directorios: {stats[0]}')
        print(f'Total directorios excluidos: {stats[1]}')
    
    
        
 

if __name__ == '__main__':
    main() 
