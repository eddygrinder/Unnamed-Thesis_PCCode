import socket

def readVoltage():
    stringValue = "11011"
            # Endereço IP e porta do Raspberry Pi
    HOST = '192.168.1.75'  # Substitua pelo endereço IP do Raspberry Pi
    PORT = 12345  # Porta de escuta no Raspberry Pi

    # Criar um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Conectar-se ao servidor (Raspberry Pi)
        s.connect((HOST, PORT))
        
        # Enviar a mensagem
        s.sendall(stringValue.encode())
        
        print("Mensagem enviada com sucesso.")