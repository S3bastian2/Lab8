class nodoDoble:
    def __init__(self, data, left, right):
        self.__data = data
        self.__left = left
        self.__right = right
        
    def nodoDoble(self):
        self.__init__(None, None, None)
    
    def nodoDoble(self, d):
        self.__init__(d, None, None)
        
    def setData(self, d):
        self.__data = d
    
    def setLeft(self, n):
        self.__left = n 
    
    def setRight(self, p):
        self.__right = p
        
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__left
    
    def getPrev(self):
        return self.__right