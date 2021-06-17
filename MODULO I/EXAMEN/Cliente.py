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
   
    def __str__(self):
        return "ID Cliente : {:<25}  \n{:<100}  \nDocumento Único de Identidad : {:<10}".format(self.get_idcliente(),Persona.__str__(self),self.get_dui())
