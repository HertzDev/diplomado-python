from Prestamo import Prestamo
from Cliente import Cliente
from datetime import date
from Pago import Pago
import sys

def main():
    menu = """
    Selecciona una opción:
    [A] Realizar Pago
    [B] Ver Pagos Realizados
    """
    idcliente = 0
    nombre = ""
    edad = 0
    dui = ""
    monto = 0.0
    interes = 0
    plazo = 0
    try:
        try:
          idcliente = int(input("Ingresa tu código de cliente: "))
          while idcliente <= 0:
             print("El código de cliente es inválido")
             idcliente = int(input("Ingresa tu código de cliente: "))
       
          nombre = input("Ingresa tu nombre completo: ")
          while is_white_or_empty(nombre):
             print("Debes ingresar un valor")
             nombre = input("Ingresa tu nombre completo: ")
        
          edad = int(input("Ingresa tu edad: "))
          while edad < 18 or edad > 100:
             print("No cumples con la edad para poder solicitar un préstamo")
             edad = int(input("Ingresa tu edad: "))
        
          dui = input("Ingresa tu número de DUI (XXXXXXXX-X): ")
          while is_white_or_empty(dui) or len(dui)<10:
             print("Debes ingresar un DUI con formato válido")
             dui = input("Ingresa tu número de DUI (XXXXXXXX-X): ") 
        
          monto = float(input("Ingresa el monto de tu préstamo: "))
          while monto <= 0:
             print("El monto ingresado es inválido")
             monto = float(input("Ingresa el monto de tu préstamo: "))
       
          interes = float(input("Ingresa el interes aplicable a tu préstamo(1-100): "))
          while interes < 1 or interes > 100:
             print("El interes ingresado es inválido")
             interes = float(input("Ingresa el interes aplicable a tu préstamo: "))
        
          interes = interes / 100
        
          plazo = int(input("Ingresa el plazo del préstamo (meses): "))    
          while plazo <= 0:
             print("El interes ingresado es inválido")
             plazo = int(input("Ingresa el plazo del préstamo (meses): "))
        except Exception as e:
          print(f"Ha ocurrido un error durante la inserción de los datos {e}")
          sys.exit()
        
        cliente = Cliente(nombre, edad, idcliente, dui)
        prestamo = Prestamo(monto, interes, plazo, cliente)
        
        print(prestamo)
        opcion = input(menu)
        while (opcion.upper()== "A" or opcion.upper() == "B"):
          if opcion.upper() == "A":
            pago = Pago(len(prestamo.pagos)+1,prestamo.get_cuota(),str(date.today()))
            prestamo.agregar_pago(pago)
          elif opcion.upper() == "B":
            for pag in prestamo.pagos:
              print()
              print("="*60)
              print(pag.__str__())
              print("="*60)
          opcion = input(menu)
        else:
          sys.exit()
    except Exception as e:
        print(f"Ha ocurrido un error durante tu proceso de prestamo {e}")

def is_white_or_empty(cadena:str):
    return not (cadena and cadena.strip())

if __name__ == "__main__":
    main()    
