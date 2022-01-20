#Importamos el modulo para visualizar los procesos
import os
#Declaramos la funcion principal
def main():
    #Creamos un bucle infinito
    while True:
        #Variable para almacenar los procesos en un string
        procesos = os.popen('wmic process get description, processid').read()
        #Si el proceso de musica no se esta ejecutando entonces...
        if (procesos.find("wmplayer.exe") == -1):
            #Abrimos el archivo .mp3
            os.system("Ping.mp3")
#Declaramos un punto de acceso
if __name__ == "__main__":
    #Llamamos a la funcion principal
    main()