from website import create_app
from flask import send_from_directory, request

import os, subprocess

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

    # Convertendo a string binária para um número inteiro
    valor_binario = int(parametro, 2)
    
     # Caminho completo para o shift_register.py
    path_to_shift_register = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ctrl_hardware', 'shift_register.py'))

    ## Operações com o valor binário recebido
    # Chama shift_register.py com subprocesso e passar o parâmetro
    try:
        subprocess.run(["python3", path_to_shift_register, parametro], check=True)
        return f'Parâmetro binário {parametro} enviado para shift_register.py com sucesso!'
    except subprocess.CalledProcessError as e:
        return f'Erro ao chamar shift_register.py: {e}'

if __name__ == '__main__':
    app.run(debug=True)
