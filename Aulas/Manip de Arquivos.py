from os import chdir, getcwd, listdir
from os.path import isfile

# Caminho do arquivo
cam = input('Digite o caminho: ')

chdir(cam)
print(getcwd())

for c in listdir():
    if isfile(c):
        print(c)