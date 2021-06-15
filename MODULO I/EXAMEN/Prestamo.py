from Cliente import Cliente
from Pago import Pago

class Prestamo:
    def __init__(self, monto:float, interes:float, plazo:float, cliente:Cliente):
        self.__monto = monto
        self.__idprestamo = ""
        self.__interes = interes
        self.__plazo = plazo
        self.__cuota = 0
        self.__cliente = cliente
        self.pagos = []

    def generar_id(self):
        idprestamo = ""
        try:
            palabras = self.__cliente.nombre.split(' ')
            for palabra in palabras:
                idprestamo += palabra[0:1]
        except Exception as e:
            print(f"Ocurrio un error: {e}")
        return idprestamo
    
    def get_cuota(self):
        return self.__cuota
    
    def __calcular_cuota(self):
        try:
            self.__cuota = self.__monto * ((self.__interes * ((1 + self.__interes) ** self.__plazo)) / (((1 + self.__interes) ** self.__plazo)-1))
        except ZeroDivisionError as e:
            print("Se intento realizar una división entre cero")
        except Exception as e:
            print(f"Ocurrió un error al calcular la cuota del prestamo: {e}") 
        return self.__cuota

    def __calcular_monto_pagar(self):
        monto = 0.0
        try:
            monto = self.get_cuota() * self.__plazo
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        return monto



    def get_monto_pagar(self):
        return self.__calcular_cuota()

    def agregar_pago(self, pago: Pago):
        self.pagos.append(pago)
    
    def __str__(self):
        return f"""hoij
                """