#importamos el modulo para trabajar con sockets
import socket
#declaramos la ip del servidor
us_ip = "192.168.0.72"
#declaramos el puerto a usar
port = 5025
#creamos un objeto socket
socket_server = socket.socket()
#asociamos ip y puerto al socket
socket_server.bind((us_ip, port))
#nos ponemos a la escucha con un numero maximo de conexiones
socket_server.listen(5)
#ejecutamos un bucle infinito
while True:
    #aceptamos conexiones y guardamos sus datos
    conection, address = socket_server.accept()
    #almacenamos los datos recibidos agregando la longitud
    message = conection.recv(1024)
    #mostramos mensaje de la conexion
    print("Conexion establecida con {}".format(address))
    #mostramos  los datos recibidos
    print((message.decode()))
    #enviamos datos
    conection.send(b"Soy un mensaje del servidor :3")
    #cerramos la conexion
    conection.close()
