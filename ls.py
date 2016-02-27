import os
from sys import argv

path = "."
if len(argv) >= 2:
    path = argv[1]

for i in os.listdir(path):
    print i,
