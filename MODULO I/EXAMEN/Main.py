from Prestamo import Prestamo
from Cliente import Cliente

def main():
    menu = """
    Selecciona una opción:
    [A] Realizar Pago
    [B] Ver Pagos Realizados
    """
    try:
        idcliente = int(input("Ingresa tu código de cliente: "))
        nombre = input("Ingresa tu nombre completo: ")
        edad = int(input("Ingresa tu edad: "))
        dui = input("Ingresa tu número de DUI (XXXXXXXX-X): ")
        monto = float(input("Ingresa el monto de tu préstamo: "))
        interes = float(input("Ingresa el interes aplicable a tu préstamo: "))
        plazo = int(input("Ingresa el plazo del préstamo (1-12): "))    

        cliente = Cliente(nombre, edad, idcliente, dui)
        prestamo = Prestamo(monto, interes, plazo, cliente)
        print(prestamo.generar_id())
    except Exception as e:
        print(f"Ha ocurrido un error durante la inserción de los datos {e}")



if __name__ == "__main__":
    main()    