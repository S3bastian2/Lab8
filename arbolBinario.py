from nodoDoble import *

class arbolBinario():
    def __init__(self, root, size):
        self.__root = root
        self.__size = size
    
    def arbolBinario(self):
        self.__root = None
        self.__size = 0
    
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def isRoot(self, v):
        return v == self.__root
    
    def hasLeft(self, v):
        return v.getLeft() != None

    def hasRight(self, v):
        return v.getRight() != None
    
    def isInternal(self, v): 
        return self.hasLeft(v) or self.hasRight(v)
    
    def root(self):
        return self.__root

    def left(self, v):
        return v.getLeft()
    
    def right(self, v):
        return v.getRight()
    
    def parent(self, v):
        if v is None or self.isRoot(v):
            return None
        else:
            return v.getParent()
    
    def addRoot(self, e):
        if isinstance(e, nodoDoble):
            self.__root = e
        else:
            self.__root = nodoDoble(e)
        self.__size += 1
        return self.__root
    
    def insertLeft(self, v, e):
        if v.getLeft() is None:
            nuevoNodo = nodoDoble(e)
            v.setLeft(nuevoNodo)
            nuevoNodo.setParent(v)
            self.__size += 1
            return nuevoNodo
        else:
            raise Exception("El nodo ya tiene un hijo izquierdo.")
    
    def insertRight(self, v, e):
        if v.getRight() is None:
            nuevoNodo = nodoDoble(e)
            v.setRight(nuevoNodo)
            nuevoNodo.setParent(v)
            self.__size += 1
            return nuevoNodo
        else:
            raise Exception("Este ya tenia un nodo derecho.")
    
    def remove(self, v):
        p = self.parent(v)
        if self.hasLeft(v) or self.hasRight(v):
            if self.hasLeft(v):
                child = self.left(v)
            else:
                child = self.right(v)
            
            if self.left(p) == v:
                p.setLeft(child)
            else:
                p.setRight(child)
            child.setParent(p)
            v.setLeft(None)
            v.setRight(None)
        else:
            if self.left(p) == v:
                p.setLeft(None)
            else:
                p.setRight(None)
        self.__size -= 1
