Escaner de puertos, por EssEnemiGz.

Programado en Python.

Uso básico. 

Argumentos.

-o, indica al programa que debe escanear los puertos abiertos. Luego de esta opción se debe pasar el host y el limite de puertos a escanear.

--only, indica al programa que solo haga un escaneo a un puerto en un host.

Ejemplo de uso.

python ports.py -o localhost 4000

python ports.py --only 1.1.1.1 53
