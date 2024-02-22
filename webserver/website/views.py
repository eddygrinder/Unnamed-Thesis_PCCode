from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from controlVB import read_Vcc_R

views = Blueprint('views', __name__)

# Esta rota será acessada através de AJAX para obter o valor atualizado da medição
@views.route('/obter-valor-da-medicao')
def obter_valor_da_medicao():
    # Aqui você pode definir o valor da medição que deseja passar para o HTML
    measurement_results = "valor_da_medicao"
    return jsonify({'medicao': measurement_results})

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    try:
        if request.method == 'GET':
        # Renderiza o HTML inicial
            return render_template("your_template.html")
        elif request.method == 'POST':
            Vcc = request.args.get('Vcc', 0, int)
            Resistence = request.args.get('R',0, int)
            print(f'Valores Recebidos - Vcc: {Vcc}, Resitence: {Resistence}')
            # Chamar a função que estará definida no script control_VB e passar os dois parâmetros recebids
            # Atenção Vcc string e Resistence string
            #Vcc_float = float(Vcc) # Atribui o valor à variável, garantindo o tipo correto
            # Verificar se ambos os valores são diferentes de zero
            if Vcc != 0 and Resistence != 0:
            # Chamar a função apenas se os valores não forem zero
                measurement_results = read_Vcc_R(Vcc, Resistence)
                print(f'MeAsure: {measurement_results}')
            else:
                #  Se um ou ambos os valores forem zero, defina measurement_results como zero
                measurement_results = 0

            # Renderize o template 'home.html' com os resultados da medição
            return render_template("home.html", user=current_user, measurement_result=measurement_results)
    except Exception as e:
        # Lidar com possíveis erros e mostrar uma mensagem de erro
        measurement_error = str(e)
        return render_template("home.html", user=current_user, measurement_error=measurement_error)

#########################################################
# Rota para passar parâmetros para o script controlVB.py
# Só passa os parâmetros de escolha    
#########################################################


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