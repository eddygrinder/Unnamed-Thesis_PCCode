from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from controlVB import read_Vcc_R


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    try:
        # Tente obter o valor da medição a partir dos parâmetros da solicitação
        measurement_value = request.args.get('measurement_value', None)
        measurement_value = float(measurement_value) if measurement_value is not None else None

        # Renderize o template 'home.html' com o valor da medição
        return render_template('home.html', user=current_user, measurement_result=measurement_value)
    except Exception as e:
        measurement_error = str(e)

        # Lidar com possíveis erros e mostrar uma mensagem de erro
        #, measurement_error=str(e)
        return render_template("home.html", user=current_user, measurement_error=measurement_error)

# Rota para passar parâmetros para o script controlVB.py
@views.route('/control_virtual_bench', methods=['GET'])
def control_virtual_bench():
    try:
        Vcc = request.args.get('Vcc','')
        Resistence = request.args.get('R','')
        print(f'Valores recebidos - Vcc: {Vcc}, Resitence: {Resistence}')
        # Chamar a função que estará definida no script control_VB e passar os dois parâmetros recebids
        measurement_results = read_Vcc_R (Vcc, Resistence)
        # Renderize o template 'home.html' com os resultados da medição
        return render_template("home.html", user=current_user, measurement_result=measurement_results)
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
