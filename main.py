from nodoDoble import *
from arbolBinario import *

# Creación del árbol
ab = arbolBinario(None, 0)

# Añadir la raíz
raiz = ab.addRoot(8)

# Insertar hijos
n1 = ab.insertLeft(raiz, 5)
n2 = ab.insertRight(raiz, 12)
n3 = ab.insertLeft(n1, 9)
n4 = ab.insertRight(n1, 11)
n5 = ab.insertLeft(n2, 6)
n6 = ab.insertRight(n2, 21)

print(f"Raíz: {ab.root().getData()}")
print(f"Hijo Izq de Raíz: {ab.left(raiz).getData()}")
print(f"Hijo Der de Raíz: {ab.right(raiz).getData()}")
#print(f"Padre de {n3.getData()} es: {ab.parent(n3).getData()}")
#print(f"Padre de {n4.getData()} es: {ab.parent(n4).getData()}")
#print(f"Padre de {n5.getData()} es: {ab.parent(n5).getData()}")
#print(f"Padre de {n6.getData()} es: {ab.parent(n6).getData()}")
print(f"EL tamaño del arbol es: {ab.size()}")
ab.remove(n1)
print(f"EL tamaño del arbol es: {ab.size()}")
print(f"Padre de {n3.getData()} es: {ab.parent(n3).getData()}")
