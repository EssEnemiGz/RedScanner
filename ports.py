"""
Red scanner.
By: EssEnemiGz
"""

from socket import *
from sys import argv

class main:
    def __init__(self):
        print("\033[1;32m-> Escaner de red.\n Por: EssEnemiGz \033[0m")
    
    def openPorts(self, host, portRange, sock):
        dispo = []
        close = []

        if portRange > 65535:
            portRange = 65535

        try:
            print(f"\033[1;32m-> Escaneando {sock}... \033[0m")
            for port in range(portRange+1):
                try:
                    if port > 0:
                        if sock == "UDP":
                            s = socket(AF_INET, SOCK_DGRAM)
                        else:
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
                print(f"\033[1;31m-> Puerto disponible -> {i}")

            print(f"\033[1;31m-> Total de puertos disponibles ({sock}) -> {len(dispo)} \033[0m")
        
        except ValueError:
            print("\033[1;31m->Debe introducir un puerto, no un str. \033[0m")

red = main()

if argv[1] in ["--open", "-o"]:
    try:
        if len(argv) == 5:
            if argv[4] == "-tcp":
                red.openPorts(argv[2], int(argv[3]), "TCP")
            elif argv[4] == "-udp":
                red.openPorts(argv[2], int(argv[3]), "UDP")
            else:
                red.openPorts(argv[2], int(argv[3]), "UDP")
                red.openPorts(argv[2], int(argv[3]), "TCP")
                exit()
        else:
            print("-> No se ha especificado un protocolo, estableciendo a TCP.")
            red.openPorts(argv[2], int(argv[3]), "TCP")

    except IndexError:
        print(f"\033[1;31m-> Faltó información, abortando operaciones...\nDatos de entrada ->")
        for i in argv[2:]:
            print(i)
        "\033[0m"

else:
    print("Failed")
