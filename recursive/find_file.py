"""
Implement a recursive function with signature find(path, filename) that
reports all entries of the file system rooted at the given path having the
given file name.
"""

import os

def find(path, filename):
    #print path,
    if os.path.basename(path) == filename:
        return path
    elif os.path.isdir(path):
        for npath in os.listdir(path):
            res = find(os.path.join(path,npath),filename)
            if res :
                return res

    else:
         return False
print find('/tmp/','ak')
