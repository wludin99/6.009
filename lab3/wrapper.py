import os
import importlib, importlib.util
import pickle
import json
import sys

sys.setrecursionlimit(5000)

try:
    import lab
    importlib.reload(lab)
except ImportError:
    import solution
    lab = solution

data = {}
for i in os.listdir('./resources/testing_data'):
    if not i.endswith('.pickle') or not i.startswith('SolveCircuit'):
        continue

    i = i[:-7]
    
    with open('./resources/testing_data/%s.pickle' % i, 'rb') as f:
        num = 0
        while True:
            num += 1
            try:
                data[i + '_' + str(num)] = pickle.load(f)
            except EOFError:
                break

def jsonify(circuit):
    jcircuit = {'junctions': [], 'wires': []}
    for junction in circuit['junctions']:
        jcircuit['junctions'].append({'label': repr(junction), 'pos': list(circuit['junctionpos'][junction])})
    for wire in circuit['wires']:
        jcircuit['wires'].append({'id': repr(wire), 'resistance': circuit['resistances'][wire], 'voltage': circuit['voltages'][wire], 'pos': [circuit['junctionpos'][circuit['wires'][wire][0]]] + [list(i) for i in circuit['intermediate'][wire]] + [circuit['junctionpos'][circuit['wires'][wire][1]]], 'soln': circuit['soln'][wire], 'startJunction': repr(circuit['wires'][wire][0]), 'endJunction': repr(circuit['wires'][wire][1])})
        if 'currents' in circuit:
            jcircuit['wires'][-1]['current'] = circuit['currents'][wire]
    return jcircuit

import traceback

def runTest(case):
    try:
        case = data[case]
        case['currents'] = lab.solveCircuit(case['junctions'], case['wires'], case['resistances'], case['voltages'])
        if set(case['currents'].keys()) != set(case['wires'].keys()) or not all([isinstance(case['currents'][current], int) or isinstance(case['currents'][current], float) for current in case['currents']]):
            raise ValueError("Returned dictionary has invalid format.")
        print("lab.solveCircuit returned:\n" + repr(case['currents']), flush=True)
        return jsonify(case)
    except:
        trace = traceback.format_exc()
        print(trace, flush=True)
        return {"error": trace}

def load(case):
    print("Loading test case:", case, flush=True)
    return jsonify(data[case])
