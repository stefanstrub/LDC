import numpy as np
import pandas as pd
import os
from os import listdir
from os.path import isfile, join
from copy import deepcopy

# import pyyaml module
import yaml
from yaml.loader import SafeLoader

# get current directory
path = os.getcwd()
 
# parent directory
parent = os.path.dirname(path)
# grandparent directory
grandparent = os.path.dirname(parent)

DATAPATH = grandparent+"/Repositories/ldc1_evaluation_data/submission"
SAVEPATH = grandparent+"/LDC/Radler/LDC1-4_evaluation/"

##### Montana
if False:
    file_name = DATAPATH + '/MSFCMontanaU_Gal/msfc-montana-ldc1-4-gb.yaml'
    with open(file_name) as f:
        data = yaml.load(f, Loader=SafeLoader)
    i = 0
    found_signals = []
    for name in data.keys():
        i += 1
        if i < 7:
            continue
        if i == len(data.keys()):
            continue
        found_signals.append(data[name])
    np.save(SAVEPATH+'Montana.npy', found_signals)

### ETH
if False:
    file_name = DATAPATH + '/ETH_LDC1-4_4mHz/LDC1-4_evaluationETH_LDC1-4_4mHz.yaml'
    with open(file_name) as f:
        data = yaml.load(f, Loader=SafeLoader)
    data = data['estimates']
    parameters = data[0].keys()
    for i in range(len(data)):
        for parameter in parameters:
            data[i][parameter] = float(data[i][parameter])
    np.save(SAVEPATH+'ETH.npy', data)



##### APC
if True:
    file_name = DATAPATH + '/PlagnolAPC/myYamFile.yaml'
    with open(file_name) as f:
        data = yaml.load(f, Loader=SafeLoader)
        
    data = data['estimates']
    parameters = []
    for i in range(len(data)):
        for parameter in data[0].keys():
            parameters.append(parameter)
            data[i][parameter] = float(data[i][parameter].split()[0])

    for i in range(len(data)):
        for parameter in parameters:
            if parameter == 'Fdot':
                data[i]['FrequencyDerivative'] = data[i][parameter]
            elif parameter == 'Phi0':
                data[i]['InitialPhase'] = data[i][parameter]
            elif parameter == 'Psi':
                data[i]['Polarization'] = data[i][parameter]
            elif parameter == 'cos(iota)':
                data[i]['Inclination'] = np.arccos(data[i][parameter])
            elif parameter == 'lambda':
                data[i]['EclipticLongitude'] = data[i][parameter]
            elif parameter == 'sin(beta)':
                data[i]['EclipticLatitude'] = np.arcsin(data[i][parameter])
    
    for i in range(len(data)):
        for parameter in ['Fdot', 'Phi0', 'Psi', 'cos(iota)', 'lambda', 'sin(beta)']:
            del data[i][parameter]
    np.save(SAVEPATH+'APC.npy', data)


print('end')