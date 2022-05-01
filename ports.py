"""
Red scanner.
By: EssEnemiGz
"""

from socket import *
from sys import argv
import threading
import concurrent.futures

class main:
    def __init__(self):
        print("\033[1;32m-> Escaner de red.\n Por: EssEnemiGz \033[0m")
    
    def openPorts(self, host, port):
        try: 
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
                s.settimeout(1)
                s.connect( (host, port) )
                s.close()

                print(f"\033[1;31m Puerto disponible -> {port} \033[0m")
                total.append(port)
                
            except OSError:
                pass

        except ValueError:
            print("\033[1;31m->Debe introducir un puerto, no un str. \033[0m")

red = main()

if argv[1] in ["--open", "-o"]:
    try:
        print(f"\033[1;32m-> Escaneando puertos con TCP... \033[0m")
        print_lock = threading.Lock()
        total = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for _port in range(int(argv[3])):
                executor.submit(red.openPorts, argv[2], _port)

        print(f"\033[1;33m El total de puertos disponibles es -> {len(total)} \033[0m")

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
