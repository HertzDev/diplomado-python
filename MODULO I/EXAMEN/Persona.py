class Persona:
    def __init__(self,nombre:str,edad:int):
        self.nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre:str):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad:int):
        self.edad = edad

    def __str__(self):
        return f"""Nombre: {self.nombre}
                Edad: {self.edad}"""
    
