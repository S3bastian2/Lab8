from BSTEntry import *
from arbolBinario import *
from nodoDoble import *

class arbolBinarioBusqueda(arbolBinario):
    def __init__(self, root, size):
        super().__init__(root, size)
    
    def arbolBinarioBusqueda(self):
        self.__init__()
    
    def buscarArbol(self, clave, v):
        if v is None:
            return None
        u = v.getData()
        if clave == u.getClave():
            return v
        elif clave < u.getClave():
            return self.buscarArbol(clave, v.getLeft())
        else:
            return self.buscarArbol(clave, v.getRight())
    
    def find(self, clave): #Métodos principales
        return self.buscarArbol(clave, self.root())
    
    def agregarNodo(self, v, o):
        temp = v.getData()
        nodito = nodoDoble(o)
        if o.getClave() < temp.getClave():
            if self.hasLeft(v):
                self.agregarNodo(self.left(v), o)
            else:
                v.setLeft(nodito)
        else:
            if self.hasRight(v):
                self.agregarNodo(self.right(v), o)
            else:
                v.setRight(nodito)
    
    def insertar(self, objeto, clave): #Métodos principales
        o = BSTEntry(objeto, clave)
        if self.isEmpty():
            self.addRoot(o)
        else:
            self.agregarNodo(self.root(), o)
    
    def nodoMaximo(self, temp):
        if self.hasRight(temp):
            return self.nodoMaximo(self.right(temp))
        else:
            return temp.getData().getClave()
    
    def nodoMenor(self, v):
        if v is None:
            return None
        while self.hasLeft(v):
            v = self.left(v)
        return v.getData().getClave()
    
    def predecesor(self, v):
        temp = v.getLeft()
        return self.nodoMaximo(temp)
    
    def remover(self, clave): #Métodos principales
        v = self.find(clave)
        temp = v.getData()
        if self.hasLeft(v) and self.hasRight(v):
            w = self.predecesor(v)
            v.setData(w.getData())
            self.remove(w)
        else:
            self.remove(v)
        return temp
    
    def mostrarArbol(self, n, profundidad):
        if n is not None:
            self.mostrarArbol(n.getRight(), profundidad + 1)
            print(' ' * 5 * profundidad + '---', n.getData().getData())
            self.mostrarArbol(n.getLeft(), profundidad + 1)
        return 