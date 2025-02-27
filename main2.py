from arbolBinarioBusqueda import *
from BSTEntry import *
from nodoDoble import *

abb = arbolBinarioBusqueda(None, 0)

abb.insertar("Objeto A", 50)
abb.insertar("Objeto B", 30)
abb.insertar("Objeto C", 70)
abb.insertar("Objeto D", 20)
abb.insertar("Objeto E", 40)
abb.insertar("Objeto F", 60)
abb.insertar("Objeto G", 80)
nodoBuscado = abb.find(50)
#if nodoBuscado:
#    print(f"Encontrado: Clave {nodoBuscado.getData().getClave()}, Objeto {nodoBuscado.getData().getData()}")
#else:
#    print("No encontrado")
print(nodoBuscado.getData())
print(abb.size())
abb.remover(50)
buscandoNodoEliminado = abb.find(50)
if buscandoNodoEliminado:
    print(f"Encontrado: Clave {buscandoNodoEliminado.getData().getClave()}, Objeto {buscandoNodoEliminado.getData().getData()}")
else:
    print("No encontrado")
#raiz = abb.root()
#print(abb.nodoMaximo(raiz))
#print(abb.nodoMenor(raiz))
#abb.mostrarArbol(raiz, 0)


