from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

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
        # Lidar com possíveis erros e mostrar uma mensagem de erro
        return render_template("home.html", user=current_user, measurement_error=str(e))


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
