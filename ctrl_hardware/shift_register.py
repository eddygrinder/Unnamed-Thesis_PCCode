from gpiozero import OutputDevice

import time

import warnings
#warnings.filterwarnings("ignore")

SER = OutputDevice(5)        # GPIO 5 - SER/DS (serial data input, SPI data)
RCLK = OutputDevice(6)        # GPIO 6 - RCLK/STCP
SRCLK = OutputDevice(13)      # GPIO 13 - SRCLK/SHCP (storage register clock pin, SPI clock)
OE = OutputDevice(19)         # GPIO 19 - Enable/Disable do SR
SRCLR = OutputDevice(26)      # GPIO 26 - O registo de deslocamento � limpo (ACTIVO BAIXO)

# Setup dos pinos
#GPIO.setup(SER, GPIO.OUT)               
#GPIO.setup(RCLK, GPIO.OUT)                     
#GPIO.setup(SRCLK, GPIO.OUT)
#GPIO.setup(SRCLR, GPIO.OUT)
#GPIO.setup(OE, GPIO.OUT)

# Inicializar a variavel correspondente a R1
# Reles 1 e 2
# checkshift = 0b0011

# Valor por defeito de espera nas operacoes do registo de deslocamento
WaitTimeSR = 0.1

#####################################################
# Tabela de verdade do Registo de Deslocamento
# SER | SRCLK | 'SRCLR | RCLK |  'OE | Sa�das/Fun��es
#  X      X       X       X       H    Q's inactivas
#  X      X       X       X       L    Q'S activos
#  X      X       L       X       X    SR limpo
#  L    + et      H       X       X    0 no SR
#  H    + et      H       X       X    1 no SR
#  X      X       X     +et       X   dados out
######################################################

# Limpa o registo de deslocamento
SRCLR.on()
time.sleep(WaitTimeSR)
SRCLR.off()

# Enable do SR - sa�das sempre activas
OE.off()

# Fun��o que verifica e desloca os bits para armazenar no registo de deslocamento
def SRoutput(checkshift):
    print(checkshift)
    for i in range(2):
        shift = checkshift & 1
        print(shift)

        if shift == 1:
            print ("UM")
            WriteReg (shift, WaitTimeSR)
        else:
            print ("ZERO")
            WriteReg(shift, WaitTimeSR)
        checkshift = checkshift >> 1
    OutputReg()

# Defini��o da fun��o que envia os dados para o registo de deslocamento,
# segundo o algoritmo descrito em baixo

### ALGORITMO ###
# Enviar um bit para o pino SER/DS
### Depois de enviado, � dado um impulso de clock (SRCLK/SHCP) e o bit armazenado nos registos
###### ... um segundo bit � enviado, repetindo os dois passos em cima - � repetido at� estarem armazenados 8 bits
######### Por ultimo � dado um impulso aos registos (RCLK/STCP) para obter os 8 bits na saida

def WriteReg (WriteBit, WaitTimeSR):
    SER.value = WriteBit #GPIO.output (SER,WriteBit) # Envia o bit para o registo
    time.sleep (WaitTimeSR) # Espera 100ms
    SRCLK.on() #GPIO.output(SRCLK,1)
    time.sleep(WaitTimeSR)
    SRCLR.off() #GPIO.output (SRCLK, 0)  # Clock - flanco POSITIVO

# Funcao que limpa o registo
def register_clear ():
    SRCLK.off() #GPIO.output(SRCLK, 0)
    time.sleep(WaitTimeSR) # espera 100ms
    SRCLK.on() #GPIO.output(SRCLK, 1)

# Armazenar o valor no registo
def OutputReg ():
    RCLK.off() #GPIO.output(RCLK, 0)
    time.sleep(WaitTimeSR)
    RCLK.on() #GPIO.output(RCLK, 1)
