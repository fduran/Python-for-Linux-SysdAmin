import os
import fnmatch

def findall(topdir, pattern):
    ''' simple implementation of the find Bash utility '''
    for path, dirs, files in os.walk(topdir):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                yield os.path.join(path, filename)


for f in findall(".", "*.py"):
    print f
