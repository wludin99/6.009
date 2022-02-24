"""6.009 Lab 4 -- Boolean satisfiability solving"""

import sys
sys.setrecursionlimit(10000)
# NO ADDITIONAL IMPORTS
def consistent(formula):
    '''
    if all literals in formula have only one value, formula can be satisfied trivially
    returns true if so, false otherwise
    '''
    d = {}
    for clause in formula:
        for lit, val in clause:
            if lit not in d:
                d[lit] = val
            elif d[lit] != val:
                return False
    return True

def assignment(formula):
    d = {}
    for clause in formula:
        for lit, val in clause:
            d[lit] = val
    return d

def unit_propagate(formula, unit):
    '''
    unit: [(lit, val)]
    return: simplified formula
    '''
    literal, val = unit[0]
    new = []
    for clause in formula:
        if not any(lit[0] == literal for lit in clause):
            new.append(clause)
        elif any(lit == (literal, not val) for lit in clause):
            clause.remove((literal, not val))
            new.append(clause)
    new.append(unit)
    return new

def pure_literals(formula):
    d = {}
    for clause in formula:
        for literal in clause:
            lit, val = literal
            if lit not in d:
                d[lit] = val
            elif d[lit] != val:
                d[lit] = None
    return d

def pure_literal_assign(formula, unit):
    '''
    unit: [(lit, val)]
    return: simplified formula
    '''
    literal, val = unit[0]
    new = []
    for clause in formula:
        if not any(lit[0] == literal for lit in clause):
            new.append(clause)
        elif any(lit == (literal, not val) for lit in clause):
            clause.remove((literal, not val))
            new.append(clause)
    new.append(unit)
    return new

def choose_literal(literals):
    '''
    literals: dictionary with lit: bool/none values
    '''
    for lit in literals:
        if literals[lit] == None:
            return lit


def satisfying_assignment(formula):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise.

    >>> satisfying_assignment([])
    {}
    >>> x = satisfying_assignment([[('a', True), ('b', False), ('c', True)]])
    >>> x.get('a', None) is True or x.get('b', None) is False or x.get('c', None) is True
    True
    >>> satisfying_assignment([[('a', True)], [('a', False)]])

    function DPLL(Φ)
    if Φ is a consistent set of literals then
        return true;
    if Φ contains an empty clause then
        return false;
    for every unit clause {l} in Φ do
       Φ ← unit-propagate(l, Φ);
    for every literal l that occurs pure in Φ do
       Φ ← pure-literal-assign(l, Φ);
    l ← choose-literal(Φ);
    return DPLL(Φ ∧ {l}) or DPLL(Φ ∧ {not(l)})
    """
    for clause in formula:
        if clause == []:
            return None
    if consistent(formula):
        return assignment(formula)
    literals = pure_literals(formula)
    for clause in formula:
        if len(clause) == 1 and literals[clause[0][0]] == None:
            formula = unit_propagate(formula, clause)
    for literal in literals:
        if literals[literal] != None:
            formula = pure_literal_assign(formula, [(literal, literals[literal])])
    l = choose_literal(literals)
    return satisfying_assignment(formula + [[(l,True)]]) or satisfying_assignment(formula + [[(l,False)]])


def get_combos(list,n):
    if n > len(list):
        return []
    if n == 1:
        return [{el} for el in list]
    if n == len(list):
        return [set(list)]
    last = list.pop()
    leave = get_combos(list.copy(), n)
    take = get_combos(list.copy(),n-1)
    for combo in take:
        combo.add(last)
    return leave + take

def boolify_scheduling_problem(student_preferences, session_capacities):
    """
    Convert a quiz-room-scheduling problem into a Boolean formula.

    student_preferences: a dictionary mapping a student name (string) to a set
                         of session names (strings) that work for that student
    session_capacities: a dictionary mapping each session name to a positive
                        integer for how many students can fit in that session

    Returns: a CNF formula encoding the scheduling problem, as per the
             lab write-up
    We assume no student or session names contain underscores.
    """
    formula = []
    ##each student in at least one room
    for student in student_preferences:
        formula.append([(str(student) + '_' + str(session),True) for session in student_preferences[student]])
    ##for each student in one of their possible locations, each pair must have have an absent
    ##so each student is only scheduled to one room
    for student in student_preferences:
        for i in student_preferences[student]:
            for j in student_preferences[student]:
                if i != j:
                    formula.append([(str(student) + '_' + str(i),False),(str(student) + '_' + str(j),False)])
    ## for each room, for all possible groups of n+1 students, one must be absent from room
    students = list(student_preferences.keys())
    for session in session_capacities:
        combos = get_combos(students, session_capacities[session] + 1)
        for combo in combos:
            formula.append([(str(student) + '_' + str(session),False) for student in combo])
    return formula



if __name__ == '__main__':
    # phi = [[('a', True)], [('a', False)]]
    # print(satisfying_assignment(phi))

    # print(get_combos([1,2,3,4,5],1))

    # students = {'jim':{'1'}, 'alice':{'1'}}
    # sessions = {'1':1}
    # print(boolify_scheduling_problem(students, sessions))

    import doctest
    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=_doctest_flags)
