"""
Red scanner.
By: EssEnemiGz
"""

from socket import *
from sys import argv

class main:
    def __init__(self):
        print("Escaner de red.\nPor: EssEnemiGz")
    
    def openPorts(self, host, portRange):
        dispo = []
        close = []
        
        try:
            for port in range(int(portRange)):
                try:
                    if port > 0:
                        s = socket(AF_INET, SOCK_STREAM)
                        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
                        s.connect( (host, port) )
                        s.close()
                        dispo.append(port)
                    else:
                        pass
                except OSError:
                    close.append(port)

            for i in dispo:
                print(f"Puerto disponible -> {i}")

            print(f"Total de puertos disponibles -> {len(dispo)}")
        
        except ValueError:
            print("Debe introducir un puerto, no un str.")
red = main()

if argv[1] in ["--open", "-o"]:
    try:
        red.openPorts(argv[2], argv[3])
    except IndexError:
        print(f"Faltó información, abortando operaciones...\nDatos de entrada ->")
        for i in argv[2:]:
            print(i)

else:
    print("Failed")
