from website import create_app
from flask import send_from_directory, request

<<<<<<< HEAD
import os, sys, subprocess
=======
from gpiozero import OutputDevice

import os, sys
>>>>>>> 95b4c87f04bd85c23dd5ca10b277dbfe61a2c851

ctrl_hardware_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ctrl_hardware'))
sys.path.append(ctrl_hardware_path)
from shift_register import SRoutput
<<<<<<< HEAD
=======

>>>>>>> 95b4c87f04bd85c23dd5ca10b277dbfe61a2c851

app = create_app()

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory("images", filename)

# Definição dos bits a serem transmitidos

#Rota para receber o parâmetro binário e usar no shift_register.py
@app.route('/atualizar_shift_register', methods=['GET'])
def atualizar_shift_register():
    parametro = request.args.get('parametro')

    # Remove o prefixo '0b' se presente
    if parametro.startswith('0b'):
        parametro = parametro[2:]

<<<<<<< HEAD
=======
    OutputDevice.close
>>>>>>> 95b4c87f04bd85c23dd5ca10b277dbfe61a2c851
    # Chama a função SRoutput do shift_register.py passando o parâmetro binário
    SRoutput(int(parametro,2)) #Converte o parâmetro binário para inteiro

    return f'Parâmetro binário {parametro} passado com sucesso!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) #Defenido para executar em todos os ip's disponíveis pela rede
