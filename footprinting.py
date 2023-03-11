# Archivo para la funcion de footprinting


from termcolor import colored
import funcionesbasicas as funciones
import footprinting
import nmap
import metasploit
import os
import requests
from bs4 import BeautifulSoup

def descargar_fichero(url, nombre_archivo):
    # Comprobar si existe la carpeta footprinting
    if not os.path.exists("resultados/footprinting"):
        os.makedirs("resultados/footprinting")

    ruta_archivo = os.path.join("resultados/footprinting",nombre_archivo)

    # Consulta para descargar el archivo
    respuesta = requests.get(url)

    # Guardar el contenido en un archivo
    with open(ruta_archivo,'wb') as fichero:
        fichero.write(respuesta.content)

    # Visualizar el contenido del fichero

    with open(ruta_archivo,'r') as fichero:
        contenido = fichero.read()
        print(contenido)
        print(colored("El contenido del archivo se ha guardado en: "+ ruta_archivo ,"green"))

def footprinting():
    # Preguntar por la url
    url = input(colored("Escribeme una url para listar los archivos dispoibles en un servidor web: ","yellow"))


    # Realizar una solicitud HTTP GET al sitio web
    response = requests.get(url)

    # Analizar el HTML de la página web con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos los enlaces en la página web
    enlaces = soup.find_all('a')

    # Crear una lista de archivos accesibles en el sitio web
    archivos = []
    for enlace in enlaces:
        href = enlace.get('href')
        if href and not href.startswith('#'):
            archivos.append(href)

    # Imprimir la lista de archivos
    print(f"Archivos accesibles en {url}:")
    for archivo in archivos:
        print(f" - {archivo}")


    pregunta = input(colored("¿Quieres ver el contenido de alguno de los archivos:? (S/N)","green"))

    if pregunta.upper() == "S":
        nombre_archivo = input(colored("Escribe el nombre del archivo que quieres descargar: ","blue"))
        urlconfichero = url + "/" + nombre_archivo
        descargar_fichero(urlconfichero,nombre_archivo)
    else:
        pass

