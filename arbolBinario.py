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
        if self.isEmpty(v):
            return v == None
        elif self.isRoot(v):
            return v == None
        else:
            return v.getParent()
    
    def addRoot(self, e):
        self.__root = nodoDoble(e)
        self.__size = 1
    
    def insertLeft(self, v, e):
        left = nodoDoble(e)
        v.setLeft(left)
        self.__size += 1
    
    def insertRight(self, v, e):
        right = nodoDoble(e)
        v.setRight(right)
        self.__size += 1
    
    def remove(self, v):
        p = self.parent(v)
        if self.hasLeft(v) or self.hasRight(v):
            if self.hasLeft(v):
                child = self.left(v)
            else:
                child = self.right(v)
            if self.left(p) == v:
                p.setLeft(v)
            else:
                p.setRight(v)
            v.setLeft(None)
            v.setRight(None)
        else:
            if self.left(p) == v:
                p.setLeft(None)
            else:
                p.setRight(None)
        self.__size -= 1





        