#! /usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2016 Charles Armstrap <charles@armstrap.org>
# If you like this library, consider donating to: https://bit.ly/armstrap-opensource-dev
# Anything helps.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import random

import os, sys, requests

# Caminho para o diretório ctrl_hardware
ctrl_hardware_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ctrl_hardware'))
# Adiciona o diretório ao sys.path
sys.path.append(ctrl_hardware_path)

#from shift_register import SRoutput

# This examples demonstrates how to make measurements using the Power
    
def read_Vcc_R (Vcc, Resistence):
    Vcc = int(Vcc) # É passado o parâmetro em forma de string mas é necessária a conversão para int
    Resistence = int(Resistence)

    measurement_result = Vcc*random.uniform(1, 5)
    #measurement_result = 1.2345

    print("Measurement: %f V" % (Vcc))
    print("Measurement: %f V" % (measurement_result))
    print("Measurement: %f KOhm" % (Resistence))
        # Atribui o valor à variável, garantindo o tipo correto
    #measurement_result = float(measurement_result)
    
    """
    # Construa a URL usando o caminho para o arquivo HTML
    html_path = os.path.join(ctrl_hardware_path, 'website/webserver/home.html')
    url = f'file://{html_path}?measurement_value={measurement_result}'

    # Faça a solicitação GET para a rota home
    resposta = requests.get(url)
    print(resposta.text)
    """
    return measurement_result
