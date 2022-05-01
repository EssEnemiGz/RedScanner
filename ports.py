"""
Red scanner.
By: EssEnemiGz
"""

from socket import *
from sys import argv

class main:
    def __init__(self):
        print("\033[1;32m-> Escaner de red.\n Por: EssEnemiGz \033[0m")
    
    def openPorts(self, host, portRange):
        dispo = []
        close = []

        if portRange > 65535:
            portRange = 65535
        
        try:
            print(f"\033[1;32m-> Escaneando puertos con TCP... \033[0m")
            verification = 0
            
            for port in range(portRange):
                try:
                    s = socket(AF_INET, SOCK_STREAM)
                    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
                    s.settimeout(0.3)
                    s.connect( (host, port) )
                    s.close()
                    dispo.append(port)

                    print(f"\033[1;31m Puerto disponible -> {dispo[verification]} \033[0m")
                    verification += 1
                
                except OSError:
                    close.append(port)

            print(f"\033[1;31m-> Total de puertos disponibles -> {len(dispo)} \033[0m")
        
        except ValueError:
            print("\033[1;31m->Debe introducir un puerto, no un str. \033[0m")

red = main()

if argv[1] in ["--open", "-o"]:
    try:
        red.openPorts(argv[2], int(argv[3]))
    except IndexError:
        print(f"\033[1;31m-> Faltó información, abortando operaciones...\nDatos de entrada ->")
        for i in argv[2:]:
            print(f"-> {i}")
        "\033[0m"
elif argv[1] in ["--only"]:
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect( (argv[2], int(argv[3])) )
        print(f"\033[1;31m-> El puerto {argv[3]} está disponible en <<{argv[2]}>> \033[0m")
    except OSError:
        print(f"\033[1;31m-> El puerto {argv[3]} no está disponible en <<{argv[2]}>> \033[0m")
else:
    print("Failed")
