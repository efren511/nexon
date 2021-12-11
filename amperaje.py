#script desarrollado por Ing. Efren Garcia
#El script es usado para consultar valores del multimetro Keithley 6500

#importamos el modulo para trabajar con sockets
import socket
#importamos el modulo para trabajar con tiempos
import time

#ip del multimetro
instrument_ip = "192.168.0.101"
#puerto del multimetro
instrument_port = 5025

#creamos una funcion para conectarnos
def instrument_connect(my_socket, my_address, my_port):
    #nos conectamos al dispositivo
    my_socket.connect((my_address, my_port))
    #regresamos el objeto de tipo socket
    return my_socket

#creamos una funcion para desconectarnos
def instrument_disconnect(my_socket):
    #cerramos el socket
    my_socket.close()
    #no retornamos ningun valor
    return

#creamos una funcion para enviar comandos
def instrument_command(my_socket, my_command):
    #establecemos el formato del comando
    cmd = "{}\n".format(my_command)
    #enviamos el comando mediante el socket
    my_socket.send(cmd.encode())
    #no retornamos ningun valor
    return

#creamos una funcion para leer los datos recividos
def instrument_read(my_socket, receive_size):
    #retornamos el valor leido
    return my_socket.recv(receive_size).decode()

#creamos una funcion para hacer una peticion al instrumento
def instrument_query(my_socket, my_command, receive_size):
    #enviamos un comando
    instrument_command(my_socket, my_command)
    #ponemos una pausa
    time.sleep(0.1)
    #regresamos el valor entregado
    return instrument_read(my_socket, receive_size)
    

#generamos un punto de acceso
if __name__ == "__main__":
    #establecemos el socket con TCP
    instrument_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #creamos la conexion
    instrument_connect(instrument_socket, instrument_ip, instrument_port)
    #enviamos el comando de reset
    instrument_command(instrument_socket, "reset()")
    #ajustamos el multimetro para medir corriente
    instrument_command(instrument_socket, "dmm.measure.func = dmm.FUNC_DC_CURRENT")
    #ajustamos el rango a 10 amperios
    instrument_command(instrument_socket, "dmm.measure.range = 10")
    # set the nplc to 0.1
    instrument_command(instrument_socket, "dmm.measure.nplc = 1.0")
    #limpiamos la pantalla
    instrument_command(instrument_socket, "display.clear()")
    #ajustamos la pantalla
    instrument_command(instrument_socket, "display.changescreen(display.SCREEN_HOME_LARGE_READING)")
    #hacemos una lectura
    reading = float(instrument_query(instrument_socket, "print(dmm.measure.read())", 32).strip('\n'))
    #mostramos el valor medido
    print("\nMedicion: {} A".format(reading))
    #nos desconectamos del dispositivo
    instrument_disconnect(instrument_socket)
    #salimos del script
    exit()