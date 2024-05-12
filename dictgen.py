# dictgen - Desarrollado por rodrigo47363

import random
import string
import signal

def generar_contraseñas(longitud=12, cantidad=5, incluir_mayusculas=True, incluir_numeros=True, incluir_especiales=True):
    """
    Genera contraseñas aleatorias.

    Args:
    - longitud: Longitud de las contraseñas.
    - cantidad: Cantidad de contraseñas a generar.
    - incluir_mayusculas: Indica si se deben incluir letras mayúsculas.
    - incluir_numeros: Indica si se deben incluir números.
    - incluir_especiales: Indica si se deben incluir caracteres especiales.

    Returns:
    - Lista de contraseñas generadas.
    """
    contraseñas = []
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    for _ in range(cantidad):
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        contraseñas.append(contraseña)
    return contraseñas

def manejar_interrupcion(signum, frame):
    """
    Maneja la interrupción de Ctrl+C para salir del programa.
    """
    print("\n¡Interrupción detectada! Saliendo del programa.")
    exit()

def mostrar_banner():
    """
    Muestra un banner ASCII al inicio del programa.
    """
    print("""      _ _      _                   
  __| (_) ___| |_ __ _  ___ _ __  
 / _` | |/ __| __/ _` |/ _ \ '_ \ 
| (_| | | (__| || (_| |  __/ | | |
 \__,_|_|\___|\__\__, |\___|_| |_|
                 |___/              """)

def generar_contraseñas_interactivo():
    """
    Interfaz interactiva para generar contraseñas personalizadas.
    """
    longitud = int(input("\nIngrese la longitud de la contraseña (por defecto 12): ") or 12)
    cantidad = int(input("Ingrese la cantidad de contraseñas a generar (por defecto 5): ") or 5)
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    contraseñas_generadas = generar_contraseñas(longitud, cantidad, incluir_mayusculas, incluir_numeros, incluir_especiales)

    print("\nContraseñas generadas:")
    for contraseña in contraseñas_generadas:
        print(contraseña)

    exportar = input("\n¿Desea exportar las contraseñas a un archivo? (s/n): ")
    if exportar.lower() == 's':
        exportar_diccionario({'contraseñas_generadas': contraseñas_generadas}, 'contraseñas.txt')

def mostrar_menu_principal():
    """
    Muestra el menú principal de opciones.
    """
    print("\nBienvenido al dictgen - Generador de Contraseñas Aleatorias!")
    print("1. Generar contraseñas")
    print("2. Mostrar banner")
    print("3. Salir")

def ejecutar_programa():
    """
    Ejecuta el programa principal.
    """
    signal.signal(signal.SIGINT, manejar_interrupcion)
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción (1/2/3): ")
        if opcion == '1':
            generar_contraseñas_interactivo()
        elif opcion == '2':
            mostrar_banner()
        elif opcion == '3':
            print("¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    ejecutar_programa()
