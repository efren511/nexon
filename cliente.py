#importamos el modulo para trabajar con sockets
import socket
#declaramos la ip del servidor
server_ip = "192.168.0.72"
#declaramos el puerto a usar
port = 5025
#creamos un socket
socket_client = socket.socket()
#nos conectamos a un socket
socket_client.connect((server_ip, port))
#enviamos datos
socket_client.send(b"Soy un mensaje del cliente :3")
#almacenamos la respuesta del servidor con la longitud de datos
answer = socket_client.recv(1024)
#mostramos los datos recibidos
print("Datos: {}".format(answer.decode()))