# Archivo para la funcion de busqueda de exploits
import requests
from bs4 import BeautifulSoup
from termcolor import colored

def buscarexploits():
    exploits = input(colored("¿Sobre que servicio quieres que busque los exploits? "))
    url = "https://www.infosecmatter.com/metasploit-module-library/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for td in soup.find_all('td', {'class': 'column-1'}):
        for a in td.find_all('a'):
            link = a.get("text")
            if link and exploits in link:
                links.append(link)

    print(colored("Exploits encontrados: ","red"))
    for enlace in links:
        print(enlace)


def buscarpayloads():
    payloads = input(colored("¿Sobre que servicio quieres que busque los exploits? "))
    url = "https://www.infosecmatter.com/metasploit-module-library/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for td in soup.find_all('td', {'class': 'column-1'}):
        for a in td.find_all('a'):
            link = a.get('href')
            if link and payloads in link:
                links.append(link)
