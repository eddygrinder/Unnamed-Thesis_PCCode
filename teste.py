import serial
import time

import sys
import cv2
import threading

import warnings
warnings.filterwarnings("ignore")

arduino = serial.Serial (port='/dev/ttyACM1', baudrate='9600')
time.sleep(2)

def main():
    path_image = "/home/grinder/Dropbox/VSC/Imagens/tese_resistencias.png"
    # Cria uma nova thread para abrir a imagem
    thread_imagem = threading.Thread(target=open_image, args=(path_image,))
    thread_imagem.start()

    # Continua a execução do programa
    escolha = input("Escolha uma resistência da imagem:")

    if (escolha == 'R1'):
        print("escolheu R1")
        cv2.destroyAllWindows() # destroy all windows
        byte_R1 = "004002000000\n"
        arduino.write(byte_R1.encode())
        time.sleep(0.5)
        arduino.close


def open_image(path_image):
    img = cv2.imread("/home/grinder/Dropbox/VSC/Imagens/tese_resistencias.png", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("Reistencias", img)
    cv2.waitKey(0)

    
main()

