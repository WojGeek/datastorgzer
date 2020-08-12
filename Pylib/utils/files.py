import time
from pathlib import Path

fileNotFound = 'file not found'
checkFileName = 'check file name'
#  PENDIENTE EVALUAR EL USO DE DICCIONARIO PARA ESTOS MENSAJES

def isFoundDestination(dirpath):
    destination_root = Path(dirpath)

    return dirpath

def ojo():
    if destination_root.exists():
        return True
    else:
        return False
#    except:
#        return 'Error isFoundDestination'

def whichDestination(lastdate):
    ''' receive last modified date to create a cronological tree'''
    spacer = r'/'
    destinationDir  = (str(lastdate[4]) +spacer+ 
            str(lastdate[1]) +spacer+ str(lastdate[2]))
    return destinationDir

def getLastModified(file):

    try:
        last_modified = time.ctime(os.path.getmtime(file))
        return last_modified.split()
    except:
        return 'Date not found'

def getCreated(file):

    try:
        created = time.ctime(os.path.getctime(file))
        return created.split()
    except:
        return 'Date not found'    
        
import hashlib
'''
Calculate the hash file.  Options: sha1,sha256,md5,sha512
'''

def getChecksum(filepath, mode='sha1'):
    try:
        h = hashlib.new(mode)
        with open(filepath, 'rb') as file:
            data = file.read()
    
        h.update(data)
        digest = h.hexdigest()
        file.close()
        return digest
    except FileNotFoundError:
        return 'Cannot determines Hash, {}.format(fileNotFound '
    except IsADirectoryError:
        return 'Is a directory, must indicate a file name'
    except:
        return 'Error: {checkFileName}'

import filetype
import os

def getFileType(f):
    
    if os.path.isdir(f):
        return 'Is a directory, must indicate a file name'
 
    ft = []
    try:
        guess = filetype.guess(f)
        ft.append(guess.extension)
        ft.append(guess.mime)
        
        return ft

    except AttributeError:
        return 'Type not supported'
    except FileNotFoundError:
        return f'Cannot identify file type, {fileNotFound} '
    except TypeError:
        return f'Unsupported type as file input, {checkFileName}'
    except IsADirectoryError:
        return 'Is a directory, must indicate a file name'
    except:
        return 'Error: {checkFileName}'


import imghdr
'''
   determines type image contained in a file
'''
def getTypeImage(filepath):
    try:
        filetype = imghdr.what(filepath)
    except FileNotFoundError:
        return f'Cannot identify image type, {fileNotFound} '
    except AttributeError: 
        return f'No attribute found, {checkFileName}'
    except IsADirectoryError: 
        return 'Is a directory, must indicate a file name'


    return filetype

