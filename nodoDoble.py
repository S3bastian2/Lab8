class nodoDoble:
    def __init__(self, data, left = None , right = None, parent = None):
        self.__data = data
        self.__left = left
        self.__right = right
        self.__parent = parent
        
    def setData(self, d):
        self.__data = d
    
    def setParent(self, p):
        self.__parent = p
    
    def setLeft(self, l):
        self.__left = l
        if l != None:
            l.setParent(self)
    
    def setRight(self, r):
        self.__right = r
        if r != None:
            r.setParent(self)
    
    def getParent(self):
        return self.__parent
        
    def getData(self):
        return self.__data
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right