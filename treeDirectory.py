from pathlib import Path
import os
import glob
import shutil

dir = '/home/willians'

def tree(directory):
    print(f'* {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '  ' * depth
        print(f'{spacer}+ {path.name}')



path = Path.cwd() # current dir
home = Path.home() # root

print(path)
print(home)

tree(home)
