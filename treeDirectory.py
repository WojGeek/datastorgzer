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

def fileDestinationPath(dir_path, destroot_path):
    
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

    sourcedir = source_directory.replace('/', '_')
    directory = Path(source_directory)

    #for path in sorted(directory.rglob('*')):
    for path in directory.rglob('*'):
        depth = len(path.relative_to(directory).parts)
        
    
        # destination path within sorted directory
        dst = fileDestinationPath(path, destinationRootPath)

        #source_root = source_directory.split()
        #print(source_root)
        
        p = path.name
        print(p)
        
        abspathfile = []
        
        abspathfile.append(dst)
        abspathfile.append(sourcedir)
        abspathfile.append(p)
     
        #print(abspathfile)
        abs_dstpath = abspathfile[0]+'/'+abspathfile[1]+'/'+abspathfile[-1]
        #print('*'*25)
        #print(abs_dstpath)
        print('*'*25)
        #abspathfile = os.path.join(dst,sourcedir, path)
        #print("--> ", abspathfile)
        parent = os.path.dirname(path)
        print(f'PARENT: ',parent)
        

        spc = ' +' * depth
        if path.is_dir():
            print(f'1) Create DESTINATION Root: {dst} ')
            print(f'2) Create DIR as: {path}')
            print(f'3) SEND THIS ABSOLUTE PATH: {dst}{path}')
            #print(f'3) SEND THIS ABSOLUTE PATH: {os.path.join(dst,os.path.dirname(path),path)}')
            print(f'3.1) Send this ABSOLUTE Path: {abs_dstpath}')
            print(f"DIRECTORY DEPTH IS : {depth}")
            print(f"PATH.NAME: {path.name}")
            #dirs.createDirectoryCluster(abspathfile)
                      
        else:
            print(f'1) Create DESTINATION Root: {dst} ')
            print(f'2) Save File into: {path}')
            print(f'3) SEND THIS ABSOLUTE PATH: {dst}{path}')
            print(f'3.1) Send this abolute Path: {abs_dstpath}')
            #print(f"DIRECTORY DEPTH IS : {depth}")
            #print(f"PATH.NAME: {path.name}")
            
            # print(f"SAVE FILE into: {path} \n DEPTH:" + 
            # f"{depth} \n PATH: {dst} \n PATHNAME: {path.name} ")
            
        # print(f" ABS PATHFILE: {abspathfile} \n ")
        
   
        #if path.is_dir():
        # print(f"{spc} Copying {abspathfile} into {dst} ")
        #copyFilesInSortedWay(abspathfile, dst) 

        
 
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
#path = os.path.join(os.getcwd(),'model')

sourcepath = '/home/willians/datastorgzer/model3'
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
    


