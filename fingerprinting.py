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