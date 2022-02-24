"""6.009 Lab 3 -- Circuit Solver."""

# NO IMPORTS ALLOWED!

# Uncomment below and comment/rename the solveLinear defined in this file to
# use the sample solveLinear function.
# Remember to comment it out before submitting!

#from solve_linear_sample import solveLinear
# global asst
# asst = {}

def substituteEquation(equation, substitutedVariable, substitutionEquation):
    """
        Note that implementing this function is optional. You might want to
        consider implementing it to break up your code into more managable
        chunks.

        Given:
            equation: An equation represented by a dictionary that maps the
                      variables or 1 to its coefficient in the equation.
                      E.g. {1: 2, 'x': 2, 'y': 3} represents 2 + 2x + 3y = 0.
            substitutedVariable: The variable to be substituted out of the
                                 equation.
            substitutionEquation: The substitution equation represented as a
                                  dictionary.
        Return:
            finalEquation: A dictionary representing the resulting equation
                           after the substitution is performed.
    """
    coeff = equation[substitutedVariable]
    d = {}
    for var in {**substitutionEquation, **equation}:
        if var in equation:
            if var in substitutionEquation:
                x = equation[var] - coeff*substitutionEquation[var]/substitutionEquation[substitutedVariable]
            else:
                x = equation[var]
        else:
            x = -coeff*substitutionEquation[var]/substitutionEquation[substitutedVariable]
        if var == 1:
            d[var] = x
        if abs(x) > 10**-7:
            d[var] = x
    return d

def down_gauss(equations, upper=[]):
    '''
    find equation with most variables and pop from equations
    find variable with largest coefficient
    for all equations in eq_d[max_var], substitute longest equation and add
    resulting eq to new equations set.
    recurse on new equations and updated equation dict
    return equation dict when there are no more equations, order that variables
    were popped in list
    '''
    if equations == {}:
        return upper
    sub_eq = min(equations, key=len)
    vars = set(sub_eq)
    try:
        vars.remove(1)
    except:
        pass
    maxVar = max(vars, key=lambda x: abs(sub_eq[x]))
    for eq in varDict[maxVar]:
        if maxVar in eq:
            new_eqs.append(substituteEquation(eq, maxVar, sub_eq))
        else:
            new_eqs.append(eq)
    upper.append((maxVar,sub_eq))
    return down_gauss(new_eqs, upper)

def up_gauss(upper, asst={1:1}):
    '''
    for all equations in eq_d[var_order.pop()], substitute shortest equations
    and add assignment
    '''
    if upper == []:
        del asst[1]
        return asst
    var, eq = upper.pop()
    asst[var] = -sum([asst[key]*eq[key] for key in eq if key != var])/eq[var]
    return up_gauss(upper, asst)

def get_vardict(equations):
    for variable in variables:
        for eq in equations:
            if var in eq:
                try:
                    varDict[var].add[eq]
                except:
                    varDict[var] = {eq}
    return varDict

def solveLinear(variables, equations):
    """
        Given:
            variables: A set of strings or tuples representing the independent
                       variables. E.g. {'x', 'y', 'z'}
            equations: A list of linear equations where each equation is
                       represented as a dictionary. Each dictionary maps the
                       variables or 1 to its coefficient in the equation.
                       E.g. {1: 2, 'x': 2, 'y': 3} represents 2 + 2x + 3y = 0.
                       Note that all variables may not appear in all of the
                       equations. Moreover, you may assume that the equations
                       are independent.
        Return:
            result: A dictionary mapping each variable to the numerical value
            that solves the system of equations. Assume that there is exactly
            one solution. Some inaccuracy as typical from floating point
            computations will be acceptable.
    """
    varDict = get_vardict(equations)
    upper = down_gauss(set([frozenset(eq) for eq in equations]), varDict)
    return up_gauss(upper)

def solveCircuit(junctions, wires, resistances, voltages):
    """
        Given:
            junctions:  A set of junctions. Each junction is labeled by a string
                        or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire, respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        directions, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the
                        starting junction otherwise. This dictionary also has
                        the same set of keys as the wires dictionary.
        Return:
            result: A dictionary mapping the label of each wire to the current
                    it carries. The labels must be the keys in the wires
                    dictionary and the current should be considered positive if
                    it is flowing from the starting junction to the ending
                    junction as specified in the wires dictionary.
    """
    ### make I Equations
    equations = {}
    for wire in wires:
        start, stop = wires[wire]
        if start in equations:
            equations[start][wire] = 1
        else:
            equations[start] = {wire: 1, 1:0}
        if stop in equations:
            equations[stop][wire] = -1
        else:
            equations[stop] = {wire: -1, 1:0}
        r = resistances[wire]
        v = voltages[wire]
        equations[wire] = {start:1, stop:-1, wire:r, 1:-v}
    equations[0] = {start:1, 1:0}
    del equations[start]
    solved = solveLinear(set(equations.keys()).add(start), list(equations.values()))
    d = {}
    for wire in wires:
        d[wire] = solved[wire]
    return d

def findMaximumDeviationJunction(junctions, wires, resistances, voltages, currents):
    """
        Note that this part is completely optional and would not contribute to your grade.

        Given:
            junctions:  A set of junctions. Each junction is labeled by a
                        string or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        direction, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the
                        starting junction otherwise. This dictionary also has
                        the same set of keys as the wires dictionary.
            currents:   A dictionary mapping each unique wire ID to a numeric
                        value representing the indicated current flowing along
                        the wire. The format is identical to that of the output
                        of the previous function. Note that the values will not
                        necessarily be correct.
        Return:
            result: A junction with the maximum deviation from current
                    conservation. Note that any junction with maximal deviation
                    will be accepted.
    """
    raise NotImplementedError

def findMaximumDeviationLoop(junctions, wires, resistances, voltages, currents):
    """
        Note that this part is completely optional and would not contribute to your grade.

        Given:
            junctions:  A set of junctions. Each junction is labeled by a string
                        or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        directions, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the
                        starting junction otherwise. This dictionary also has
                        the same set of keys as the wires dictionary.
            currents:   A dictionary mapping each unique wire ID to a numeric
                        value representing the indicated current flowing along
                        the wire. The format is identical to that of the output
                        of the previous function. Note that the values will not
                        necessarily be correct.
        Return:
            result: A list of wires IDs representing the edges along a loop with
                    maximal (additive) deviation from Kirchoff's loop law.
                    The wires should be in order along the cycle but the
                    starting node and the direction may be arbitrary.
    """
    raise NotImplementedError

if __name__ == '__main__':
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used for testing.
    variables = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    equations = [{'a': 1, 'b': 2, 'e': 3, 1: -2},
                 {'b': 2, 'e': 4, 'd': 6, 'h': 4, 1: -8},
                 {'a': -1, 'c': 5, 'd': -4, 1: 2},
                 {'b': 2, 'd': -2, 'f': 3, 1: 10},
                 {'e': -1, 'g': 3, 1: 8},
                 {'a': 2, 'd': 3, 'h': -1, 1: -18},
                 {'b': -3, 'c': 2, 'f': 1, 1: 2},
                 {'c': 1, 'd': 2, 'e': -1, 1: -12}]
    print(solveLinear(variables, equations))
