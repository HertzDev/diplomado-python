class Pago:
    def __init__(self, idpago:int, monto:float, fecha:str):
        self.__idpago = idpago
        self.__monto = monto
        self.__fecha = fecha

    def __str__(self):
        return "ID Pago : {:<10}  \nMonto : ${:<10.2f}  \nFecha : {:<12}".format(self.__idpago,self.__monto,self.__fecha)
