import sys
from fraccion import Fraccion


class MatFrac():
    pass


# esto es para MAC o Linux, en dado que sea Windows debe ser directamente
# el nombre del archivo
dir = sys.path[0]+"/"+"matriz1"
dir2 = sys.path[0]+"/"+"matriz2"
dir = sys.path[0]+"/"+"matriz1.txt"
dir2 = sys.path[0]+"/"+"matriz2.txt"


mf = MatFrac(dir)
mf.lectura()
mf2 = MatFrac(dir2)
mf2.lectura()
print(mf.mat)
print(mf2.mat)
mf3 = mf.suma(mf2)
print(mf3.mat)
