import RPi.GPIO as GPIO

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

import serial
import time

SER = 5         # GPIO 5 - SER/DS (serial data input, SPI data)
RCLK = 6        # GPIO 6 - RCLK/STCP
SRCLK = 13      # GPIO 13 - SRCLK/SHCP (storage register clock pin, SPI clock)
SRCLR = 26      # GPIO 26 - O registo de deslocamento é limpo (ACTIVO BAIXO)

# Setup dos pinos
GPIO.setup(SER, GPIO.OUT)               
GPIO.setup(RCLK, GPIO.OUT)                     
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(SRCLR, GPIO.OUT)

# Inicializar a variavel correspondente a R1
# Reles 1 e 2
#checkshift = 0b0011

# Valor por defeito de espera nas operações do registo de deslocamento
WaitTimeSR = 0.1

# Inicaializa o pino de clear dos registos a 1 - o clear é controlado e feito numa função
GPIO.output(SRCLR,1)

import warnings
warnings.filterwarnings("ignore")

# Funcao que limpa o registo
def register_clear ():
    GPIO.output(SRCLR, 0) # É feito o clear
    time.sleep(WaitTimeSR) # espera 100ms
    GPIO.output(SRCLR, 1)

# Função que verifica e desloca os bits para armazenar no registo de deslocamento
def SRoutput(checkshift):
    for i in range(4):
        shift = checkshift & 1
        if shift == 1:
            print ("UM")
            WriteReg (shift, WaitTimeSR)
        else:
            print ("ZERO")
            WriteReg(shift, WaitTimeSR)
        checkshift = checkshift >> 1
    OutputReg()

# Definição da função que envia os dados para o registo de deslocamento,
# segundo o algoritmo descrito em baixo

### ALGORITMO ###
# Enviar um bit para o pino SER/DS
### Depois de enviado, é dado um impulso de clock (SRCLK/SHCP) e o bit armazenado nos registos
###### ... um segundo bit é enviado, repetindo os dois passos em cima - É repetido até estarem armazenados 8 bits
######### Por ultimo é dado um impulso aos registos (RCLK/STCP) para obter os 8 bits na saida

def WriteReg (WriteBit, WaitTimeSR):
    GPIO.output (SRCLK, 0)  # Clock - flanco POSITIVO
    GPIO.output(RCLK,0) # Garantir que o LATCH está a zero antes de enviar o bit
    GPIO.output (SER,WriteBit) # Envia o bit para o registo
    time.sleep (WaitTimeSR) # Espera 100ms
    GPIO.output(SRCLK,1)
    GPIO.output(SRCLK,0)
    
# Armazenar o valor no registo
def OutputReg():
    GPIO.output(RCLK, 1)
    #GPIO.cleanup()
    while True:
        pass
