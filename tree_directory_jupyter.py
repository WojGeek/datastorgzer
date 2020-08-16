#!/usr/bin/env python
# coding: utf-8

# In[219]:


sourcepath = '/home/willians/datastorgzer/model3'
#sourcepath = '/media/willians/CENTOS/home/willians'
print(f'Directorio: {sourcepath} ')

# Destination path to save the sorted files
destinationrootpath = '/media/willians/32E5585F137BEDC8'
print('Destination: ', destinationrootpath)


# In[220]:


abs_srcpath = abs_dstpath = ''


# In[221]:


from pathlib import Path
import os
from shutil import copytree
import shutil, errno
from Pylib.utils import dirs
from Pylib.utils import files
from Pylib.interface import dialog


# In[230]:

def copyFiles(source, destination):
    try:
        if os.path.isfile(destination):
            print(f'File already copied {destination}')
        else:
            shutil.copy(source, destination,follow_symlinks=True)
            print(f"Copied {source} to {destination} ")
        
    except FileNotFoundError as e: 
        print("Error with \r\n".format(source) +
        "Error number: {0}\r\n".format(e.errno) +
        "Error text: {0}".format(e.strerror))
    
    except FileExistsError:
        print(f'Already copied {destination}')

    
        
def copyFilesInSortedWay(source, destination):
    print(f"Copying {source} to {destination} ")
    try:
        #if not os.path.exists(destination):
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


# In[231]:


def createDirectoryCluster(dirpath):
    lastpath = '/'
    created = False
    try:
        for d in dirpath.split('/'):
            # handle instances of // in string
            if not d:
                continue 

            lastpath += d + '/'

            if not os.path.isdir(lastpath):
                os.mkdir(lastpath)
                created = True

        return lastpath

    except PermissionError as e:
        print("Error wth directory!\r\n" +
        "Error number: {0}\r\n".format(e.errno) +
        "Error text: {0}".format(e.strerror))
        return None


# In[232]:


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


# In[233]:


def tree(source_directory, destinationRootPath):
    print(f'Sorting the Directory  {source_directory}')

    sourcedir = source_directory.replace('/', '_')
    directory = Path(source_directory)

    counter = 0

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

            # destination path within sorted directory
            dst = fileDestinationPath(path, destinationRootPath)

            abspathfile.append(dst)
            abspathfile.append(sourcedir)
            abspathfile.append(os.fspath(path))

            abs_dstpath = abspathfile[0]+'/'+abspathfile[1]
            abs_srcpath = str(p)

            # verify destination 
            dstpath = abs_dstpath+'/'+str(path.relative_to(directory))
            #+str(path.name)
            
            print(f'1) Create DESTINATION according modified date: {dst} ')
            print(f'2) Subfolder readed at: {path}')
            print(f'3) Absolute path estimated: {dst}{path}')
            print(f'4) Absolute destination path to save the content: {abs_dstpath}')
            print(f'5) Absolute source path to be saved: {abs_srcpath}')
            print(f"6) Directory depth level  : {depth}")
            print(f"7) Path name: {path.name}")
            print(f'8) dstpath: {dstpath}')
            #dirs.createDirectoryCluster(abspathfile)
            

            

            if not dirs.uniqueDirectoryPath(dstpath):
                        # create a new destination directory
                        createDirectoryCluster(dstpath)
                        print("Destination created at {} ".format(dstpath))
            else:
                        print("Destination already created: {} ".format(dstpath))

            print('-'*10,'Directory process terminated','-'*10)

        else:

            abspathfile.append(dst)
            abspathfile.append(sourcedir)
            abspathfile.append(os.fspath(path))

            abs_dstpath = abspathfile[0]+'/'+abspathfile[1]
            abs_srcpath = str(p)
            rp = str(path.relative_to(path))
            relat_path = rp.split('/')

            dstpath = abs_dstpath+'/'+str(path.relative_to(directory))
            

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
            
            copyFiles(path, dstpath)     
            print('-'*10,'File process terminated','-'*10)
       
        
        #createDirectoryCluster(abs_dstpath)
        #copyFilesInSortedWay(abs_srcpath, abs_dstpath) 


# In[ ]:





# In[234]:


tree(sourcepath, destinationrootpath)


# In[202]:





# In[ ]:





# In[ ]:




