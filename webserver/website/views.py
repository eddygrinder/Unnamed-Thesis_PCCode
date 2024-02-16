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
@views.route('/control_virtual_bench', methods=['GET'])
@login_required
def control_virtual_bench():
    try:
        Vcc = request.args.get('Vcc','')
        Resistence = request.args.get('R','')
        print(f'Valores Recebidos - Vcc: {Vcc}, Resitence: {Resistence}')
        # Chamar a função que estará definida no script control_VB e passar os dois parâmetros recebids
        
        measurement_result = 1.2
        print(f'Measure: {measurement_result}')

        # Renderize o template 'home.html' com os resultados da medição
        return render_template("home.html", user=current_user, measurement_result = measurement_result)
    except Exception as e:
        # Lidar com possíveis erros e mostrar uma mensagem de erro
        measurement_error = str(e)
        return render_template("home.html", user=current_user, measurement_error=measurement_error)


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

"""
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