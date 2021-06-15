from Persona import Persona

class Cliente(Persona):
    def __init__(self,nombre:str, edad:int, idcliente:int, dui:str):
        Persona.__init__(self,nombre,edad)
        self.__idcliente = idcliente
        self.__dui = dui

    def get_idcliente(self):
        return self.__idcliente
    
    def get_dui(self):
        return self.__dui