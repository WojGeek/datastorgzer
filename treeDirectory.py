from pathlib import Path
import os
import glob
import shutil, errno
from Pylib.utils import dirs
from Pylib.utils import files
from Pylib.interface import dialog
from shutil import copytree



files_at_root = 0
files_at_subdir = 0
files_at_othersub = 0
files_at_deeper = 0

def createDestinationFiles(dir_path, destroot_path):
    
    # get modification date from the dir or files
    lastmodified = files.getLastModified(dir_path)
    
    #print(lastmodified)
    
    ''' determines destination directory in
    order to organize the folder as a 
    chronological order '''
    datesorted = files.whichDestination(lastmodified)
    
    # determines new destination on storage
    destinationsortedbydate = os.path.join(destroot_path, datesorted)
    #print('Destination sorted by date: ', destinationsortedbydate)

    # verify destination root
    # if not dirs.uniqueDirectoryPath(destinationsortedbydate):
    #     #print("Destination not found: {} ".format(destinationsortedbydate))
    #     # create a new destination directory
    #     dirs.createDirectoryCluster(destinationsortedbydate)
    # else:
    #     #print("Destination found: {} ".format(destinationsortedbydate))
    #     pass
    #copyFiles(path, dst)
    return destinationsortedbydate

def tree(source_directory, destinationRootPath):
    print(f'Sorting the Directory  {source_directory}')

    for path in sorted(source_directory.rglob('*')):
        depth = len(path.relative_to(source_directory).parts)
           
        spc = ' +' * depth
        if path.is_dir():
            #print(f"{spc} DIR: {path} at level {depth}")
            print(f"{spc} Folder: {path}  ")
        else:
           #print("\t\_ {} \t ".format(path.name))
           pass

        dst = createDestinationFiles(path, destinationRootPath)

        #if path.is_dir():
        #print(f"{spc} Copying {path} to {dst} ")
        copyFilesInSortedWay(path, dst) 

        
       
def copyFiles(source, destination):
    try:
        shutil.copytree(source, destination) 
    except FileExistsError:
        print(f'Already copied {source}')
    except PermissionError:
        print(f'Permission denied on {source}')
 
def copyFilesInSortedWay(source, destination):
    
    try:
        if not os.path.exists(destination):
            print(f"Copying {source} to {destination} ")
            if source.is_dir():
                shutil.copytree(source, destination)
            else:
                shutil.copy(source, destination)
                print('DESTINATION: ', destination)
    except FileExistsError:
        print(f'Already copied {filepath}')
    except PermissionError:
        print(f'Permission denied on {source}')
    except FileNotFoundError:
        print(f' {source} not found ')
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(source, destination)
        else: raise
    



# Source directory where files will be sorted
path = os.path.join(os.getcwd(),'model')
sourcepath = Path(path)
print(f'Directorio: {sourcepath} ')

# Destination path to save the sorted files
destinationrootpath = '/tmp'


#while True:

sort_files = input('Start? Yes or No ')

if sort_files.lower()[0] == 'y':
    sorting_on = True
else:
    sorting_on = False

while sorting_on:

    tree(sourcepath, destinationrootpath)
    sorting_on = False

        # if not dialog.accept():
        #     break
    


