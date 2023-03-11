import pyfiglet
from termcolor import colored
import funcionesbasicas as funciones
import footprinting
import nmap
import metasploit
import chatgpt
import os
from shutil import get_terminal_size


# Mostrar introduccion

funciones.mostrar_intro()

# Crear un diccionario con las opciones para ejecutar las funciones

opciones = {'1': footprinting.footprinting,
            '2': nmap.nmap,
            '3': metasploit.buscarexploits,
            '4': metasploit.buscarpayloads,
            '5': chatgpt.hablar
            }

while  True:
    funciones.mostrar_menu()

    seleccion = input(colored("Selecciona una opción: ",'yellow'))

    if seleccion.lower() == "salir":
        print(colored("Cerrando el menú ....",'blue'))
        break

    print(colored("Seleccionaste la opcion: ",'red'), seleccion)


    # Comprobacion de la seleccion correcta
    if seleccion in opciones:
        opciones[seleccion]()
        funciones.barrer_pantalla()
    else:
        os.system('clear')
        print(colored("Seleccionaste la opcion: ", 'red'), seleccion)
        print(colored("Selecciona una de las opciones del menu",'red'))
        funciones.mostrar_menu()





