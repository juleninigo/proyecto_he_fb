import pyfiglet
from termcolor import colored
import os

def mostrar_intro():
    # Crear objeto Figlet con la fuente "slant"
    custom_fig = pyfiglet.Figlet(font='slant')

    # Crear mensaje "exploitmenu" en ASCII art utilizando la fuente "slant"
    intro = custom_fig.renderText('exploitmenu')

    # Imprimir mensaje ASCII art en la consola
    print(intro)
    print(colored("Made by: Julen, Mikel & Imanol", 'red'))
    print()
    print(colored("Ahora se lanzará el menu", 'yellow'))
def mostrar_menu():
    # Imprimir opciones del menú
    print()
    print(colored("\t 1. FootPrinting",'green'))
    print(colored("\t 2. Escaneo de puertos con Nmap",'red'))
    print(colored("\t 3. Busqueda de exploits para metasploit",'blue'))
    print(colored("\t 3. Busqueda de payloads para exploits de metasploit", 'blue'))
    print()
    print("Escribe 'salir' para salir del menú")


def barrer_pantalla():
        print()
        barrer = input(colored("Quieres limpiar la pantalla (S/N)",'yellow'))

        if barrer.upper() == "S":
            os.system('clear')
            mostrar_intro()
        else:
            pass