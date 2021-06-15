class Pago:
    def __init__(self, idpago:int, monto:float, fecha:str):
        self.__idpago = idpago
        self.__monto = monto
        self.__fecha = str

    def __str__(self):
        return f""" Id Pago: {self.__idpago}
                    Monto: {self.__monto}
                    Fecha: {self.__fecha}
                """
