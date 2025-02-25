class BSTEntry():
    def __init__(self, objeto, clave):
        self.__objeto = objeto
        self.__clave = clave
    
    def getData(self):
        return self.__objeto
    
    def getClave(self):
        return self.__clave

    def setData(self, objeto):
        self.__objeto = objeto
    
    def setClave(self, clave):
        self.__clave = clave