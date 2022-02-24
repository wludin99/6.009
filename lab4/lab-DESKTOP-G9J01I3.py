"""6.009 Lab 4 -- Boolean satisfiability solving"""

import sys
sys.setrecursionlimit(10000)
# NO ADDITIONAL IMPORTS
class SAT:
    def __init__(self, formula):
        form = dict()
        for i in range(len(formula)):
            for literal in formula[i]:
                form[(i,literal[0])] = literal[1]
        self.formula = form

        lits = set()
        for key in self.formula:
            clause, lit = key
            lits.add(lit)
        self.literals = sorted(list(lits))

        self.length = len(formula)

    def empty_clause(self):
        for i in range(self.length):
            empty = True
            for j in self.literals:
                if (i,j) in self.formula:
                    empty = False
                    break
            if empty:
                return True
        return False

    def consistency(self):
        asst = dict()
        for l in self.literals:
            val = set()
            for i in range(self.length):
                try:
                    val.add(self.formula[(i,l)])
                except:
                    pass
                if val == {True, False}:
                    raise ValueError
            if val == {True}:
                asst[l] = True
            elif val == {False}:
                asst[l] = False
        return asst

    def unit(self, i):
        vals = []
        for l in self.literals:
            try:
                vals.append((i,l,self.formula[(i,l)]))
                if len(vals) == 2:
                    raise unitError
            except:
                pass
        return vals[-1]

    def unit_propagate(self, unit):
        '''
        returns: (singletons, vars)
        singletons: boolean assignments that must be
        vars: list of variables sorted by # of clauses they appear in, minus
        singletons
        no changes to formula
        '''
        clause, lit, val = unit
        for i in range(self.length):
            if i != clause:
                try:
                    if self.formula[(i,lit)] == val:
                        for l in self.literals:
                            try:
                                del self.formula[(i, l)]
                            except:
                                pass
                    if self.formula[(i,lit)] != val:
                        del self.formula[(i,lit)]
                except:
                    pass

    def pure(self, l):
        vals = set()
        for i in range(self.length):
            try:
                vals.add(self.formula[(i,l)])
                if vals == {True, False}:
                    break
            except:
                pass
        if len(vals) == 1:
            return vals

    def pure_literal_assign(self, lit, val):
        if val == set():
            return None
        for i in range(self.length):
            try:
                if self.formula[(i,lit)] in val:
                    for l in self.literals:
                        if l != lit:
                            try:
                                del self.formula[(i, l)]
                            except:
                                pass
                if self.formula[(i, lit)] not in val:
                    del self.formula[(i,lit)]
            except:
                pass

    def choose_literal(self):
        lit = None
        max = 0
        for l in self.literals:
            number = 0
            for i in range(self.length):
                if (i, l) in self.formula:
                    number += 1
            if number >= max:
                lit = l
                max = number
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

    Pseudocode:
        function DPLL(Φ):
        if Φ contains an empty clause then
            return False;
        if Φ is a consistent set of literals then
            return True;
        for every unit clause {l} in Φ do
           Φ ← unit-propagate(l, Φ);
        for every literal l that occurs pure in Φ do
           Φ ← pure-literal-assign(l, Φ);
        l ← choose-literal(Φ);
        return DPLL(Φ ∧ {l}) or DPLL(Φ ∧ {not(l)});
    """
    formula = SAT(formula)

    def DPLL(formula):
        # print(formula.formula)
        try:
             return formula.consistency()
        except:
            pass

        if formula.empty_clause():
            # print('empty clause')
            return None

        for i in range(formula.length):

            try:
                formula.unit_propagate(formula.unit(i))
                # print("unit-propagated clause " + str(i+1))
                # print(formula.formula)
            except:
                pass

        for l in formula.literals:
            try:
                formula.pure_literal_assign(l, formula.pure(l))
                # print("pure-literal-propagated literal " + str(l))
                # print(formula.formula)
            except:
                pass

        l = formula.choose_literal()
        # print("chose literal " +str(l))
        formula.length += 1
        formula.formula[(formula.length-1, l)] = True
        t = DPLL(formula)
        if t != None:
            return t
        else:
            formula.formula[(formula.length-1, l)] = False
            return DPLL(formula)

    return DPLL(formula)

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
    test = [[["c", False], ["b", False]], [["c", False], ["c", False], ["c", False]], [["b", False], ["b", True], ["a", False]], [["a", False], ["a", True]], [["a", True], ["a", False], ["c", True]], [["b", False]], [["c", True], ["a", False]], [["b", False], ["c", False], ["b", False]], [["a", True]], [["b", True], ["c", True]]]
    formula = SAT(test)
    # print(formula.empty_clause())
    print(satisfying_assignment(test))

    # import doctest
    # _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    # doctest.testmod(optionflags=_doctest_flags)
