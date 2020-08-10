import os
#from pathlib import Path
from mod.utils import dirs
from mod import dialog

'''
Proyecto: dsa

    Organize files on any data storage
 
'''
excluded = ['.themes','.config',
            '.thunderbird','.cache','.local','.sane','.mozilla']

def directory_choice():
        choice = input('Indique la ruta del directorio: ')
        return choice

def main():

        # entrada del directorio        
        dir = '/home/willians'
        dir = '/home/wp'

        dir = directory_choice()
        
        # Seguro de proseguir?
        print(f'Ha elegido a {dir} como directorio raiz')

        if dialog.accept_choice():
            print('Creando un catálogo de archivos')

            #stats = getDirCatalog(dir)
            print(dirs.isAlive())
            stats = dirs.getList(dir, excluded)
            print(f'Total Sub-directorios: {stats[0]}')
            print(f'Total directorios excluidos: {stats[1]}')
        

        # else:
        #     print('Bye')
        
        
if __name__ == '__main__':
    main() 
