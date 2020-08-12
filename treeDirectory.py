from pathlib import Path
import os
import glob
import shutil
from Pylib.utils import dirs
from Pylib.utils import files
from Pylib.dummy import hello



files_at_root = 0
files_at_subdir = 0
files_at_othersub = 0
files_at_deeper = 0

def createDestinationFiles(dir_path, dest_dir):
    # see modification date 
    #lstdest = os.path.join(root_path,dest_dir)
    lastmodified = files.getLastModified(dir_path)
    print(lastmodified)
    ''' determines destination directory in
    order to organize the folder as a 
    chronological order '''
    dest_dir = files.whichDestination(lastmodified)
    print(dest_dir)
    # determines new destination on storage
    dstpath = os.path.join(dest_dir,dir_path)
    print('last destination ', dstpath)

    # verify destination 
    if not dirs.uniqueDirectoryPath(dstpath):
        print("Destination not found: {} ".format(dstpath))
        # create a new destination directory
        dirs.createDirectoryCluster(dstpath)
    else:
        print("Destination found: {} ".format(dstpath))


def tree(directory):
    print(f'* {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '  ' * depth
        #print(f'{spacer}+ {path.name}')
        #print("path: {}".format(path.relative_to(directory)))
   

        #print('Parent: ',path.parent)
        #print('Depth: ',depth)
        spc = '>>>' * depth
        if path.is_dir():
            #print(f"{spc} DIR: {path} at level {depth}")
            print(f"{spc}{depth}) Folder: {path}")
        else:
            #print("\t\__ {} \n\t \_ at {}".format(path.name,path.parent))
            print("\t\_ {} \t ".format(path.name))

        #createDestinationFiles(path, rp)
       

        #lastmodified = files.getLastModified(path.name)
        #print(lastmodified)
        



#path = Path.cwd() # current dir
#home = Path.home() # root

#print(path)
#print(home)

# source
rootpath = os.path.join(os.getcwd(),'model')
#dirpath = os.getcwd()'modelo'
rp = Path(rootpath)

# destination

tree(rp)

#print(dirs.isAlive())
#hello.coder()
print()
print(f'Root: {files_at_root}')
print(f'Subdir: {files_at_subdir}')
print(f'Under subdir: {files_at_othersub}')
print(f'Deeper: {files_at_deeper}')