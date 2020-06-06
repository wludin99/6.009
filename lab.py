"""6.009 Lab 4 -- Boolean satisfiability solving"""

import sys
sys.setrecursionlimit(10000)
# NO ADDITIONAL IMPORTS
global backtrack
backtrack = {}
def update(formula, asst):
    '''
    asst: (var, bool)
    return: simplified formula
    '''
    var, bool = asst
    new = []
    for clause in formula:
        if not any(lit[0] == var for lit in clause):
            new.append(clause)
        else:
            if any(lit == (var, not bool) for lit in clause):
                if len(clause) == 1:
                    return False
                simplified = clause.copy()
                simplified.pop((var, not bool))
                new.append(simplified)
    backtrack[new] = (formula, asst)
    return new

def init(formula):
    '''
    returns: (singletons, vars)
    singletons: boolean assignments that must be
    vars: list of variables sorted by # of clauses they appear in, minus
    singletons
    no changes to formula
    '''
    vars = set()
    for clause in formula:
        for lit in clause:
            vars.add(lit[0])
    singletons = set()
    for clause in formula:
        if len(clause) == 1:
            singletons.add(clause[0])
    return (singletons, vars)

def get_next_var(formula, vars):
    d = {}
    for clause in formula:
        for var in vars:
            if any(lit[0]==var for lit in clause):
                if var in d:
                    d[var] += 1
                else:
                    d[var] = 1
    return max(d, key=lambda x: d[x])

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
    """
    asst, vars = init(formula)
    for var in asst:
        formula = update(formula, var)
    first_var = get_next_var(formula, vars)
    def search(formula, asst):
        if len(formula) == 1 or formula == []:
            clause = formula[0]
            asst[0] = clause[0][1]
            return asst
        next_var = vars.pop()
        tass = update(formula, (var, True))
        if search(tass, queue) != None:
            return search(tass, queue)
        fass = update(formula, (var, False))
        if search(fass, queue) != None:
            return search(formula, queue)
    return search(formula, asst)



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
    raise NotImplementedError


if __name__ == '__main__':
    import doctest
    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=_doctest_flags)
