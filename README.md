Escaner de puertos, por EssEnemiGz.

Programado en Python.

Uso básico. 

Argumentos.

-o, indica al programa que debe escanear los puertos abiertos. Luego de esta opción se debe pasar el host y el limite de puertos a escanear.

-tcp, indica que realice el escaneo usando el protocolo TCP.

-udp, indica que realice el escaneoo usando el protocolo UDP.

-all, indica que use el protocolo TCP y UDP por igual.

Ejemplo de uso.

python ports.py -o 8.8.8.8 4000 -udp
