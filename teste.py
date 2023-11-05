import serial
import time

import sys
import cv2

import schemdraw
import schemdraw.elements as elm

import subprocess

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
    print("- 470 Ohm")
    print ("- 1.2K")
    print ("- 10K")
    
    while True:
        try:
            R1_Value = input("Escolha o valor da Resistência - ")

            # Validação da escolha
            if R1_Value in ("470", "1K2", "10K"):
                caminho_imagem = "esquemaOhm.png"
                subprocess.Popen([visualizador, caminho_imagem])
                draw_schematic(R1_Value)
                # Enviar os bits para o Shift register e activar os relés 
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