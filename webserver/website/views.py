from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from configVB import read_Vcc_R
from configString import readVoltage

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
      
    measurement_results = read_Vcc_R(Vcc, Resistence)
    print(f'MeAsure: {measurement_results}')

    return jsonify({'measurement_result': measurement_results})

@views.route('/read_Voltage', methods=['GET', 'POST'])
@login_required
def read_Voltage():
    Vcc = request.args.get('Vcc', 0, int)
    Resistence = request.args.get('R',0, int)
    print(Vcc)
    print(Resistence)

    #if Vcc == None and Resistence == None:
     #   print('MeAsure: {measurement_results}AA')
    #else:
     #   readVoltage()
    return jsonify({'measurement_result': 12})