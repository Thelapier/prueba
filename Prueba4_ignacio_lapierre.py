#  almacenar las reservas
# comentario de prueba
nombre  = ""
frase_secreta  = ""
decision = ""
disponibles = 0
reservadas = 0
opcion = 0
# Programa para gestionar reservas de zapatillas

reservas = {}
stock_maximo = 20

def reservar_zapatillas():
    global reservas
    if len(reservas) >= stock_maximo:
        print("No hay stock disponible para nuevas reservas.")
        return

    nombre = input("Ingrese su nombre: ").strip()

    if nombre in reservas:
        print("Este nombre ya ha sido registrado. Solo se permite una reserva por comprador.")
        return

    frase_secreta = input("Ingrese la frase secreta para continuar: ")

    if frase_secreta != "EstoyEnListaDeReserva":
        print("Frase secreta incorrecta. No se puede realizar la reserva.")
        return

    reservas[nombre] = 1  # 1 reserva por defecto
    print("Reserva registrada exitosamente para " +nombre)

def buscar_reserva():
    nombre = input("Ingrese el nombre para buscar la reserva: ").strip()

    if nombre in reservas:
        print("Reserva encontrada para " +nombre )
        if reservas[nombre] == 1:
            decision = input("¿Desea pagar un adicional para reserva VIP (si/no)? ").lower()
            if  decision == "si":
                reservas[nombre] = 2
                print("Reserva VIP activada. Ahora tiene 2 pares reservados.")
            else:
                print("No se realizó la mejora a VIP.")
        else:
            print("Ya cuenta con una reserva VIP.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")

def ver_stock():
    reservadas = sum(reservas.values())
    disponibles = stock_maximo - len(reservas)
    print(f"Reservas realizadas: {len(reservas)} compradores.")
    print(f"Total de pares de zapatillas reservados: {reservadas}")
    print(f"Stock disponible para nuevas reservas: {disponibles}")

def menu():
    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Ver stock de reservas")
        print("4.- Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar una opción válida!")
            continue

        if opcion == 1:
            reservar_zapatillas()
        elif opcion == 2:
            buscar_reserva()
        elif opcion == 3:
            ver_stock()
        elif opcion == 4:
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!")

menu()