from pathlib import Path
import os
from Pylib.utils import files
from Pylib.utils import dirs


def directoryTree(source_directory, excluded, destinationRootPath):
    print(f'Directory sorting started at  {source_directory}')

    sourcedir = source_directory.replace('/', '_')
    directory = Path(source_directory)

    counter = 0
    excluded_directories = 0
    results = []
    directory_quantity = 0

    #for path in sorted(directory.rglob('*')):
    for path in directory.rglob('*'):
        depth = len(path.relative_to(directory).parts)
    
        counter += 1
        #print('*'*25,'Start of directory or file','*'*25)
        p = path.resolve()
        #print(type(p))
        
        #print('RESOLVE ',p)
        
        abspathfile = []
        
       
        
        #print(abspathfile)
        #abs_dstpath = abspathfile[0]+'/'+abspathfile[1]+str(p)
        #abs_dstpath = abspathfile[0]+str(p)
        
             
        #print(abs_dstpath)
        #print('*'*25)
        
        print('='*3, str(counter), '='*3 )  

        parent = os.path.dirname(path)
        print(f'PARENT: ',parent)
        print('RELATIVE TO DIRECTORY: ', path.relative_to(directory))
        
        

        if path.is_dir():

            directory_quantity += 1

            if path.name in excluded:
                print('Excluded directory '+str(path.name))
                excluded_directories += 1
            else:
                # destination path within sorted directory
                dst = files.fileDestinationPath(path, destinationRootPath)

                abspathfile.append(dst)
                abspathfile.append(sourcedir)
                abspathfile.append(os.fspath(path))

                abs_dstpath = abspathfile[0]+'/'+abspathfile[1]
                abs_srcpath = str(p)

                # verify destination 
                dstpath = abs_dstpath+'/'+str(path.relative_to(directory))
                #+str(path.name)
                if not dirs.uniqueDirectoryPath(dstpath):
                    print(f'1) Create DESTINATION according modified date: {dst} ')
                    print(f'2) Subfolder readed at: {path}')
                    print(f'3) Absolute path estimated: {dst}{path}')
                    print(f'4) Absolute destination path to save the content: {abs_dstpath}')
                    print(f'5) Absolute source path to be saved: {abs_srcpath}')
                    print(f"6) Directory depth level  : {depth}")
                    print(f"7) Path name: {path.name}")
                    print(f'8) dstpath: {dstpath}')
                    #dirs.createDirectoryCluster(abspathfile)

                #if not dirs.uniqueDirectoryPath(dstpath):
                    # create a new destination directory
                    dirs.createDirectoryTreeDatebased(dstpath)
                    print("Destination created at {} ".format(dstpath))
                else:
                    print("Destination already created: {} ".format(dstpath))
                    print('-'*10,'Directory processing finished','-'*10)

        else:

            # destination path within sorted directory
            dst = files.fileDestinationPath(path, destinationRootPath)

            abspathfile.append(dst)
            abspathfile.append(sourcedir)
            abspathfile.append(os.fspath(path))

            abs_dstpath = abspathfile[0]+'/'+abspathfile[1]
            abs_srcpath = str(p)
            #rp = str(path.relative_to(path))
            #relat_path = rp.split('/')

            dstpath = abs_dstpath+'/'+str(path.relative_to(directory))
            
            if not os.path.isfile(dstpath):
                print(f'1) Create DESTINATION according modified date: {dst} ')
                print(f'2) File readed at: {path}')
                print(f'3) Absolute path (path): {dst}{path}')
                print(f'4) Definitive path to save the content: {abs_dstpath}')
                print(f'5) Absolute source path to be saved: {abs_srcpath}')
                print(f"6) Directory depth level  : {depth}")
                print(f"7) Path name: {path.name}")
                print(f'8) (dstpath) {dstpath}')
                

            # # verify destination 
            # rp = str(path.relative_to(directory))
            # relat_path = rp.split('/')
            # #print('+'*20, relat_path)
            # dstpath = dst+'/'+relat_path[0]+'/'+path.name
            # # if not dirs.uniqueDirectoryPath(dstpath):
            # #     # create a new destination directory
            # #     createDirectoryCluster(dstpath)
            # #     print("Destination created at {} ".format(dstpath))
            # # else:
            # #     print("Destination already created: {} ".format(dstpath))

            # dstpath = dst+'/'+relat_path[0]+'/'+path.name
            #print(f'COPIAR ARCHIVO DESDE: {path}  EN: {dstpath} ')
            
                files.copyFiles(path, dstpath)     
                #print('-'*10,'File process terminated','-'*10)
            else:
                print("File already copied: {} ".format(dstpath))
                print('-'*10,'File processing finished','-'*10)


       
    results.append(directory_quantity)
    results.append(excluded_directories)
    return results
        #createDirectoryCluster(abs_dstpath)
        #copyFilesInSortedWay(abs_srcpath, abs_dstpath) 
