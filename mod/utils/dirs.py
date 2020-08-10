from pathlib import Path
import os

def isAlive():
    return 'it works!'
    
def getList(dirpath,excluded='None'):

    excluded_directories = 0
    results = []
    directory_quantity = 0
    count = 0

    entries = Path(dirpath)
    for entry in entries.iterdir():
        #print(entry.name)
        if entry.is_dir():
            count += 1
            print('{}) {}'.format(count,entry))
            directory_quantity += 1

            # count the excluded directories
            if entry.name in excluded:
                print(f'EXCLUDE: {entry.name}')
                excluded_directories += 1

    results.append(directory_quantity)
    results.append(excluded_directories)
    return results

def getDirCatalog(dirpath,excluded='None'):

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