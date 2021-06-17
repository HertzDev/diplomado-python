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
        self.__idprestamo = ""
        try:
            palabras = self.__cliente.nombre.split(' ')
            for palabra in palabras:
                self.__idprestamo += palabra[0:1]
        except Exception as e:
            print(f"Ocurrio un error: {e}")
        return self.__idprestamo
    
    def get_cuota(self):
        self.__calcular_cuota()
        return self.__cuota
    
    def __calcular_cuota(self):
        try:
            self.__cuota = self.__monto * ((self.__interes * ((1 + self.__interes) ** self.__plazo)) / (((1 + self.__interes) ** self.__plazo) - 1))
        except ZeroDivisionError as e:
            print("Se intento realizar una división entre cero")
        except Exception as e:
            print(f"Ocurrió un error al calcular la cuota del prestamo: {e}") 
        return self.__cuota

    def __calcular_monto_pagar(self):
        monto = 0.0
        try:
            monto = self.__cuota * self.__plazo
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        return monto



    def get_monto_pagar(self):
        return self.__calcular_monto_pagar()

    def agregar_pago(self, pago: Pago):
        self.pagos.append(pago)
        print("Se agrego el pago correctamente")
    
    def __str__(self):
        cuota = self.get_cuota()
        total_pagar = self.get_monto_pagar()
        print()
        print("="*10,"Información del cliente","="*10)
        print(self.__cliente)
        print("="*60)
        print()
        print("="*10,"Información del préstamo", "="*10)
        print("ID Préstamo : {:<10}  \nMonto : ${:<10.2f}  \nInteres : {:<6.2f}%  \nPlazo : {:<10} meses  \nTotal a Pagar : ${:<10.2f}  \nCuota Mensual : ${:10.2f}  ".format(self.__idprestamo, self.__monto, (self.__interes * 100) ,self.__plazo, total_pagar, cuota))
        print("="*60)
        print()
        print("="*10,"Calendario de Pagos", "="*10)
        print()    
        mensaje = "|{:<10}  |{:<10}   |{:<10}  |\n".format("No.","Cuota","Saldo")
        for mes in range(self.__plazo+1):
          if mes == 0:
            mensaje += "|{:<10}  |${:<10.2f}  |${:<10.2f}  |\n".format(str(mes),0,total_pagar)
          else:
            mensaje += "|{:<10}  |${:<10.2f}  |${:<10.2f}  |\n".format(str(mes),cuota,(total_pagar-cuota))
            total_pagar -= cuota
        mensaje += "|{:<10}  |${:<10.2f}    {:<10}  |\n".format("Monto",self.get_monto_pagar()," ")
        return mensaje
               
