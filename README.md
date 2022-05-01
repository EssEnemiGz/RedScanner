Escaner de puertos, por EssEnemiGz.

Programado en Python.

Uso básico. 

Argumentos.

-o, indica al programa que debe escanear los puertos abiertos. Luego de esta opción se debe pasar el host y el limite de puertos a escanear.

--only, indica al programa que solo haga un escaneo a un puerto en un host.

Ejemplo de uso.

```python
python ports.py -o localhost 4000
# Manda al programa a escanear hasta el puerto 4000, es decir, escanea los puertos del 0 al 4000 en localhost.

python ports.py --only 1.1.1.1 53
# Manda al programa a escanear solo el puerto 53 del host "1.1.1.1".
# Los sockets ya tienen un TimeOut, por lo que se puede usar el argumento -o para los host remotos.
