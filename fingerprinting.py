# Archivo para la funcion de nmap
from termcolor import colored
import funcionesbasicas as funciones
import footprinting
import fingerprinting
import metasploit
import os
import requests
from bs4 import BeautifulSoup
import subprocess

import nmap
def fingerprinting():

    ip = input(colored("Dime la ip o el dominio a escanear: ",'yellow'))
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments='-p 1-65535 -sT')

    for host in scanner.all_hosts():
        print(colored('Puertos abiertos para el host: ' + host,"green"))
        for puerto, estado in scanner[host]['tcp'].items():
            if estado['state'] == 'open':
                print('  Puerto:', puerto, '- Estado:', estado['state'])
                #Comprobar existencia de la carpeta
                if not os.path.exists("resultados/nmapscans"):
                    os.makedirs("resultados/nmapscans")

                ruta_archivo = os.path.join("resultados/nmapscans", ip)
                with open(ruta_archivo,'w') as fichero:
                    contenido = f"El puerto {puerto} esta abierto\n"
                    fichero.write(contenido)
                print(colored("El contenido del escaneo se ha guardado en: "+ ruta_archivo,"green"))



## En caso de error con las librerias hacer lo siguiente
'''
try:
    output = subprocess.check_output(['pip', 'show', 'python-nmap'])
    output_lines = output.decode().split('\n')
    for line in output_lines:
        if line.startswith('Location:'):
            nmap_path = line.split(': ')[1]
            break
except:
    print('Error: No se pudo obtener la ruta de instalación de python-nmap')
    exit()

# Agregar la ruta a la variable PYTHONPATH
try:
    python_path = os.environ.get('PYTHONPATH', '')
    nmap_path = os.path.join(nmap_path, 'nmap')
    if python_path:
        python_path += ';'
    python_path += nmap_path
    os.environ['PYTHONPATH'] = python_path
    print('La ruta de python-nmap se agregó correctamente a la variable de entorno PYTHONPATH')
except:
    print('Error: No se pudo agregar la ruta de python-nmap a la variable de entorno PYTHONPATH')
'''