import pyfiglet
from termcolor import colored
import funcionesbasicas as funciones
import os


# Mostrar introduccion

funciones.mostrar_intro()

while  True:
    funciones.mostrar_menu()

    seleccion = input(colored("Selecciona una opción:",'yellow'))

    if seleccion.lower() == "salir":
        print("Cerrando el menú ....")
        break

    print(colored("Seleccionaste la opcion ",'red'), seleccion)

    funciones.barrer_pantalla()