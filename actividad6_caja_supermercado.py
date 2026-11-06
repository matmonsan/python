# Actividad 6: la caja del supermercado

productos = ["pan", "leche", "huevos"]
precios = [0.85, 1.20, 2.50]   # el precio de productos[0] es precios[0], etc.
carrito = []                   # aquí se guardan los precios de lo que se compra


# ---------- Parte A: funciones (sin input() ni print()) ----------

def convertir_numero(texto):
    numero = int(texto)
    if numero < 0:
        raise ValueError("Número no válido: no puede ser negativo")
    return numero


def anadir(carrito, numero):
    if numero >= len(precios):
        raise IndexError("Ese producto no existe")
    carrito.append(precios[numero])


def quitar(carrito, posicion):
    if posicion >= len(carrito):
        raise IndexError("Esa posición no existe")
    carrito.pop(posicion)


def calcular_total(carrito):
    total = 0
    for precio in carrito:
        total = total + precio
    return total


def repartir(total, personas):
    return total / personas


# ---------- Parte B: programa principal ----------

def main():
    opcion = 0

    while opcion != 4:
        print()
        print("1. Añadir")
        print("2. Quitar")
        print("3. Repartir la cuenta")
        print("4. Salir")
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            opcion = 0   # no es un número: se trata como opción no válida

        if opcion == 1:
            try:
                texto = input("Número de producto (0 = pan, 1 = leche, 2 = huevos): ")
                numero = convertir_numero(texto)
                anadir(carrito, numero)
            except IndexError:
                print("Ese producto no existe")
            except ValueError as error:
                print(error)
            else:
                print("Operación realizada")
            finally:
                print(f"Carrito: {carrito}")
                print(f"Total: {calcular_total(carrito):.2f} euros")

        elif opcion == 2:
            try:
                texto = input("Posición a quitar (la primera es la 0): ")
                posicion = convertir_numero(texto)
                quitar(carrito, posicion)
            except IndexError:
                print("Esa posición no existe")
            except ValueError as error:
                print(error)
            else:
                print("Operación realizada")
            finally:
                print(f"Carrito: {carrito}")
                print(f"Total: {calcular_total(carrito):.2f} euros")

        elif opcion == 3:
            try:
                texto = input("¿Entre cuántas personas? ")
                personas = convertir_numero(texto)
                parte = repartir(calcular_total(carrito), personas)
            except (ValueError, ZeroDivisionError):
                print("No se puede repartir: escribe un número de personas mayor que 0")
            else:
                print(f"Cada persona paga {parte:.2f} euros")
                print("Operación realizada")
            finally:
                print(f"Carrito: {carrito}")
                print(f"Total: {calcular_total(carrito):.2f} euros")

        elif opcion == 4:
            print("Gracias por su compra")

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
