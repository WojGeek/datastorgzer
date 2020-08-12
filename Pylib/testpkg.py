from dummy import hello
from utils import files, dirs

hello.coder()
print(files.getChecksum('testpkg.py'))
print(dirs.isAlive())
