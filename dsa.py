import os
from pathlib import Path
'''
Proyecto: dsa

    Organize files on any data storage
 
'''
excluded = ['.themes','.config',
            '.thunderbird','.cache','.local','.sane','.mozilla']

def directory_choice():
        choice = input('Indique la ruta del directorio: ')
        return choice

def accept_choice():
     
    choice = 'wrong'
    
    while choice not in ['S','N']:
        
        choice = input("Inicia la organización de los archivos (S or N): ")
        
        if choice not in ['S','N']:
            print("Lo siento, elija de nuevo S o N ")

    if choice == 'S':
        return True
    else:
        return False

def listDir(dirpath):

    excluded_directories = 0
    results = []
    directory_quantity = 0

    entries = Path(dirpath)
    for entry in entries.iterdir():
        #print(entry.name)
        if entry.is_dir():
            print('{})'.format(entry))
            directory_quantity += 1

            # count the excluded directories
            if entry.name in excluded:
                print(f'EXCLUDE: {entry.name}')
                excluded_directories += 1

    results.append(directory_quantity)
    results.append(excluded_directories)
    return results

def getDirCatalog(dirpath):

    excluded_directories = 0
    directory_quantity = 0
    files_quantity = 0
    results = []
    last_dir = ''
    subdirectories = []
    excludeddirs = []

    absWorkingDir = os.path.abspath(dirpath)
    
    for folderName, subfolders, filenames in os.walk(dirpath):
        # Mostrar si se quiere
        #print(f'\n< Current folder: {folderName} >') 
   
        for subfolder in subfolders:
            # Mostrar si se quiere
            #print(f'\n* Subfolders de:  {folderName}: {subfolder}')
            
            # I avoid counting the same directory
            if not subfolder  in subdirectories:
                directory_quantity += 1
            
            # memorize the directory already counted
            subdirectories.append(subfolder)
              
            base_folder =  os.path.basename(subfolder)
            #splitted_path = subfolder.split(os.path.sep)
            excludedDirectoryPath = os.path.join(absWorkingDir, subfolder)
            

            # count the excluded directories
            if base_folder in excluded:

                # I avoid counting the same directory
                if not subfolder  in excludeddirs:
                   excluded_directories += 1
                
                # imprime si se quiere 
                #print(f' {subfolder} is EXCLUDED\n')
                #print(f'Path will be excluded: {os.path.abspath(subfolder)}')
                #print(f'Path will be excluded: {base_folder}')

                print("Excluded: " +
                "Directory: {} ".format(base_folder) +
                "at Path: {}".format(subfolder))
                #"at Path: {}".format(excludedDirectoryPath))
 
            #print(f'{os.path.abspath(folders)}')    
            for filename in filenames:
                # Mostrar los archivos. Si se desea
                #print(f'\n_ File inside {folderName} \n \_ {filename}')
                files_quantity += 1
            
    results.append(directory_quantity)
    results.append(excluded_directories)
    results.append(files_quantity)
    return results

def main():

        # entrada del directorio        
        #dir = directory_choice()
        dir = '/home/willians'
        dir = '/media/willians/_sda5_'

        # Seguro de proseguir?
        #print(f'Ha elegido a {dir} como directorio raiz')

        #if accept_choice():
        print('Creando un catálogo de archivos')

        

        #stats = getDirCatalog(dir)
        stats = listDir(dir)
        print('Se imprime Catálogo y Estadísticas')
        print(f'Total Sub-directorios: {stats[0]}')
        print(f'Total directorios excluidos: {stats[1]}')

            
            

        # else:
        #     print('Bye')
        
        

  

if __name__ == '__main__':
    main() 
