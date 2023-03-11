import shutil

import pyfiglet
from termcolor import colored
import funcionesbasicas as funciones
import footprinting
import fingerprinting
import metasploit
import chatgpt
import os
from shutil import get_terminal_size


# Mostrar introduccion

funciones.mostrar_intro()

# Crear un diccionario con las opciones para ejecutar las funciones

opciones = {'1': footprinting.footprinting,
            '2': fingerprinting.fingerprinting,
            '3': metasploit.buscarexploits,
            '4': chatgpt.hablar
            }

while True:
    funciones.mostrar_menu()

    seleccion = input(colored("Selecciona una opción: ",'yellow'))

    if seleccion.lower() == "salir":
        print(colored("Cerrando el menú ....",'blue'))
        break

    #print(colored("Seleccionaste la opcion: ",'red'), seleccion)


    # Comprobacion de la seleccion correcta
    if seleccion in opciones:
        opciones[seleccion]()
        funciones.barrer_pantalla()
    else:
        os.system('clear')
        #print(colored("Seleccionaste la opcion: ", 'red'), seleccion)
        # Recopilar el tamaño de la shell para adecuar el texto
        texto_error = "La opcion que has seleccionado no esta contemplada en el menu"
        ancho_shell, _ = shutil.get_terminal_size()
        # Adecuar el texto a la shell
        longitud_total = ancho_shell - len(texto_error)
        caracter_relleno = "-"

        # Crear la cadena compuesta
        mensaje_error = texto_error.center(longitud_total,caracter_relleno)
        print(colored(mensaje_error,'red'))

        funciones.mostrar_menu()





