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

import os, sys
from pyvirtualbench import PyVirtualBench, PyVirtualBenchException
ctrl_hardware_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ctrl_hardware'))
sys.path.append(ctrl_hardware_path)

from shift_register import SRoutput

# This examples demonstrates how to make measurements using the Power
# Supply (PS) on a VirtualBench.
    
def read_Vcc_R (Vcc, Resitence):
    # Power Supply Configuration
    channel = "ps/+25V"
    voltage_level = Vcc
    current_limit = 0.5
    
    try:  
        # You will probably need to replace "myVirtualBench" with the name of your device.
        # By default, the device name is the model number and serial number separated by a hyphen; e.g., "VB8012-309738A".
        # You can see the device's name in the VirtualBench Application under File->About
        virtualbench = PyVirtualBench('VB8012-30A210F')
        ps = virtualbench.acquire_power_supply()

        ps.configure_voltage_output(channel, voltage_level, current_limit)
        ps.enable_all_outputs(True)
    
        """
        EXEMPLO: Realiza 10 leituras - pretende-se só uma leitura
        for i in range(10):
            voltage_measurement, current_measurement, ps_state = ps.read_output(channel)
            print("Measurement [%d]: %f V\t%f A\t(%s)" % (i, voltage_measurement, current_measurement, str(ps_state)))
        """
        
        # Realiza UMA medição
        voltage_measurement, current_measurement, ps_state = ps.read_output(channel)
        print("Measurement: %f V\t%f A\t(%s)" % (voltage_measurement, current_measurement, str(ps_state)))
        
        ps.release()    
    except PyVirtualBenchException as e:
        print("Error/Warning %d occurred\n%s" % (e.status, e))
    finally:
        virtualbench.release()
