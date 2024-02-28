from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from controlVB import read_Vcc_R

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

#########################################################
# Rota para passar parâmetros para o script controlVB.py
# Só passa os parâmetros de escolha    
#########################################################

# Rota para controlar e obter o resultado da medição
@views.route('/config_VirtualBench', methods=['GET', 'POST'])
@login_required
def config_VirtualBench():
    Vcc = request.args.get('Vcc', 0, int)
    Resistence = request.args.get('R',0, int)
    print(f'Valores Recebidos - Vcc: {Vcc}, Resitence: {Resistence}')
    # Chamar a função que estará definida no script control_VB e passar os dois parâmetros recebids
    # Atenção Vcc string e Resistence string
    #Vcc_float = float(Vcc) # Atribui o valor à variável, garantindo o tipo correto
    
    measurement_results = read_Vcc_R(Vcc, Resistence)
    print(f'MeAsure: {measurement_results}')

    return jsonify({'measurement_result': measurement_results})

"""
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


 try:
        Vcc = request.args.get('Vcc','')
        Resistence = request.args.get('R','')
        print(f'Valores recebidos - Vcc: {Vcc}, Resitence: {Resistence}')
        measurement_result = read_Vcc_R()
        # Renderize o template 'home.html' com o valor da medição
        return render_template('home.html', user=current_user, measurement_result=measurement_result)
    except Exception as e:
        measurement_error = str(e)

        # Lidar com possíveis erros e mostrar uma mensagem de erro
        #, measurement_error=str(e)
"""