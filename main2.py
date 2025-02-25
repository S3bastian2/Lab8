from arbolBinarioBusqueda import *
from BSTEntry import *
from nodoDoble import *

abb = arbolBinarioBusqueda(None, 0)

n1 = abb.insertar("Objeto A", 50)
n2 = abb.insertar("Objeto B", 30)
n3 = abb.insertar("Objeto C", 70)
n4 = abb.insertar("Objeto D", 20)
n5 = abb.insertar("Objeto E", 40)
n6 = abb.insertar("Objeto F", 60)
n7 = abb.insertar("Objeto G", 80)
"""nodoBuscado = abb.find(50)
if nodoBuscado:
    print(f"Encontrado: Clave {nodoBuscado.getData().getClave()}, Objeto {nodoBuscado.getData().getData()}")
else:
    print("No encontrado")
#print(abb.size())
abb.remover(80)
abb.remover(30)
abb.remover(50)
buscandoNodoEliminado = abb.find(50)
if buscandoNodoEliminado:
    print(f"Encontrado: Clave {buscandoNodoEliminado.getData().getClave()}, Objeto {buscandoNodoEliminado.getData().getData()}")
else:
    print("No encontrado")"""
raiz = abb.root()
#print(abb.nodoMaximo(raiz))
#print(abb.nodoMenor(raiz))
abb.mostrarArbol(raiz, 0)


