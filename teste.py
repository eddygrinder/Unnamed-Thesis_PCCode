import shift_register as SR

import RPi.GPIO as GPIO

import serial
import time

import sys
#import cv2

import schemdraw
import schemdraw.elements as elm

import subprocess

current_measure760  = 0b0010
current_measure1K = 0b0100
# bit a ZERO activa o relé
# 0111
# Rele 1 | Rele2 | Rele 3 | Rele 4
# Q0 -> Relé 1
# Q1 -> Relé 2
# (...)

# Resistências:
# R1 = 470
# R2 = 1.2K
# R3 = 10K

# Caminho para o visualizador de imagens (pode variar dependendo do seu sistema operacional)
visualizador = "xdg-open"  # Linux
# visualizador = "open"  # macOS
# vi

import warnings
warnings.filterwarnings("ignore")

#arduino = serial.Serial (port='/dev/ttyACM1', baudrate='9600')
#time.sleep(2)

# Caminho para o visualizador de imagens (pode variar dependendo do seu sistema operacional)
visualizador = "xdg-open"  # Linux
# visualizador = "open"  # macOS
# visualizador = "start"  # Windows

def main():
    # Escolha do valor da resistência
    # Não sai do ciclo enquanto não for feita uma escolha válida
    print("Para o estudo da Lei de Ohm escolha uma das três resistências:")
    print("- 760 Ohm - [760]")
    print ("- 1.2K - [1K2]")
    print ("- 10K")
    
    while True:
        try:
            R_Value = input("Escolha o valor da Resistência - ")

            # Validação da escolha
            if R_Value in ("760", "1K2", "10K"):
                caminho_imagem = "esquemaOhm.png"
                subprocess.Popen([visualizador, caminho_imagem])
                draw_schematic(R_Value)
                # Enviar os bits para o Shift register e activar os relés 
                if R_Value == "760":
                    SR.register_clear()
                    time.sleep(1)
                    SR.SRoutput(current_measure760)
                elif R_Value == "1K2":
                    SR.register_clear()
                    time.sleep(1)
                    SR.SRoutput(current_measure1K)
                break
            else:
                raise ValueError("Escolha não é válida")
        except ValueError as e:
            print(e)    

#if (escolha == 'R1'):
#print("escolheu R1")
#cv2.destroyAllWindows() # destroy all windows
#byte_R1 = "004002000000\n"
#arduino.write(byte_R1.encode())
#time.sleep(0.5)
#arduino.close

def draw_schematic(R1_Value):
    with schemdraw.Drawing(show=False) as d:
        d.config(unit=5) #tamanho do componente
        # Adicionando os elementos
        d += (V1 := elm.SourceV().label('Vin'))
        d += (I1 := elm.MeterA().right().label('Amp'))
        d += elm.Dot()
        d.push()
        d += (R1 := elm.Resistor().down().label(R1_Value, loc='bot'))
        d += elm.Dot()
        d.pop()
        d += (L1 := elm.Line())
        d += (Vol := elm.MeterV().down().label('Volt', loc='bot', rotate=True))
        d += (L2 := elm.Line().tox(V1.start))            
        #d.draw()
        d.save('esquemaOhm.png')

if __name__ == "__main__":
    main()
    #GPIO.cleanup()
