#!/usr/bin/env python3
import os
import lab
import json
import unittest
import copy

import sys
sys.setrecursionlimit(10000)

TEST_DIRECTORY = os.path.join(os.path.dirname(__file__), 'test_inputs')

class Test_1_TestSat(unittest.TestCase):
    def opencase(self, casename):
        with open(os.path.join(TEST_DIRECTORY, casename + ".json")) as f:
            cnf = json.load(f)
            return [[[variable, polarity]
                     for variable, polarity in clause]
                    for clause in cnf]

    def convert_to_tuple(self, formula):
        return [[tuple(literal) for literal in formula[i]] for i in range(len(formula))]

    def satisfiable(self, casename, use_tuple=False):
        cnf = self.opencase(casename)
        if use_tuple:
            cnf = self.convert_to_tuple(cnf)
        asgn = lab.satisfying_assignment(copy.deepcopy(cnf))
        self.assertIsNotNone(asgn)

        # Check that every clause has some literal appearing in the assignment.
        self.assertTrue(all(any(variable in asgn and asgn[variable] == polarity
                                for variable, polarity in clause)
                            for clause in cnf))

    def unsatisfiable(self, casename, use_tuple=True):
        cnf = self.opencase(casename)
        if use_tuple:
            cnf = self.convert_to_tuple(cnf)
        asgn = lab.satisfying_assignment(copy.deepcopy(cnf))
        self.assertIsNone(asgn)

    def test_A_2_2_2(self):
        self.satisfiable('2_2_2')

    def test_B_5_3_3(self):
        self.satisfiable('5_3_3')

    def test_C_10_4_3(self):
        self.unsatisfiable('10_4_3')

    def test_D_10_3_100(self):
        self.unsatisfiable('10_3_100')

    def test_E_20_3_1000(self):
        self.unsatisfiable('20_3_1000')

    def test_F_100_10_100(self):
        self.satisfiable('100_10_100')

    def test_G_1000_5_10000(self):
        self.unsatisfiable('1000_5_10000')

    def test_H_1000_10_1000(self):
        self.satisfiable('1000_10_1000')

    def test_I_1000_11_1000(self):
        self.satisfiable('1000_11_1000')

    def test_J_10_3_100_tuple(self):
        self.unsatisfiable('10_3_100', True)

    def test_K_1000_5_10000_tuple(self):
        self.unsatisfiable('1000_5_10000', True)

class Test_2_TestPuzzleSudoku(unittest.TestCase):
    """
    These three tests use your satisfying_assignment code to solve sudoku
    puzzles (formulated as Boolean formulas).

    See http://www.cs.qub.ac.uk/~I.Spence/SuDoku/SuDoku.html for one
    explanation of how to formulate a CNF formula for a sudoku puzzle.
    """

    def get_sudoku(self, n):
        with open(os.path.join(TEST_DIRECTORY, 'sudoku%s.json' % n)) as f:
            return json.loads(f.read())

    def run_sudoku_test(self, n, original):
        result = lab.satisfying_assignment(self.get_sudoku(n))
        self.assertNotEqual(None, result, "There is a valid sudoku solution, but you returned None.")
        self.check_sudoku(original, self.assignment_to_grid(result))

    def assignment_to_grid(self, a):
        a = {k for k,v in a.items() if v}
        out = []
        for r in range(9):
            row = []
            for c in range(9):
                row.append([v+1 for v in range(9) if '%s_%s_%s' % (r, c, v) in a][0])
            out.append(row)
        return out

    def get_superblock(self, sr, sc):
        return {(r, c) for r in range(sr*3, (sr+1)*3) for c in range(sc*3, (sc+1)*3)}

    def check_sudoku(self, original, result):
        all_nums = set(range(1, 10))

        # all values from original must be preserved
        self.assertTrue(all((iv==jv or iv == 0) for i,j in zip(original, result) for iv, jv in zip(i, j)))

        # all rows must contain the right values
        self.assertTrue(all(set(i) == all_nums for i in result))

        # all columns must contain the right values
        for c in range(9):
            self.assertTrue(set(i[c] for i in result) == all_nums)

        # all superblocks must contain the right values
        for sr in range(3):
            for sc in range(3):
                self.assertTrue(set(result[r][c] for r, c in self.get_superblock(sr, sc)) == all_nums)

    def test_sudoku_1(self):
        """
        sudoku corresponding to the following board (0 denotes empty)
        """
        original = [[5,1,7,6,0,0,0,3,4],
                    [2,8,9,0,0,4,0,0,0],
                    [3,4,6,2,0,5,0,9,0],
                    [6,0,2,0,0,0,0,1,0],
                    [0,3,8,0,0,6,0,4,7],
                    [0,0,0,0,0,0,0,0,0],
                    [0,9,0,0,0,0,0,7,8],
                    [7,0,3,4,0,0,5,6,0],
                    [0,0,0,0,0,0,0,0,0]]
        self.run_sudoku_test(1, original)

    def test_sudoku_2(self):
        """
        sudoku corresponding to the following board (0 denotes empty)
        """
        original = [[5,1,7,6,0,0,0,3,4],
                    [0,8,9,0,0,4,0,0,0],
                    [3,0,6,2,0,5,0,9,0],
                    [6,0,0,0,0,0,0,1,0],
                    [0,3,0,0,0,6,0,4,7],
                    [0,0,0,0,0,0,0,0,0],
                    [0,9,0,0,0,0,0,7,8],
                    [7,0,3,4,0,0,5,6,0],
                    [0,0,0,0,0,0,0,0,0]]
        self.run_sudoku_test(2, original)

    def test_sudoku_3(self):
        """
        sudoku corresponding to the following board (0 denotes empty)
        (from http://www.extremesudoku.info/sudoku.html)
        """
        original = [[0,0,1,0,0,9,0,0,3],
                    [0,8,0,0,2,0,0,9,0],
                    [9,0,0,1,0,0,8,0,0],
                    [1,0,0,5,0,0,4,0,0],
                    [0,7,0,0,3,0,0,5,0],
                    [0,0,6,0,0,4,0,0,7],
                    [0,0,8,0,0,5,0,0,6],
                    [0,3,0,0,7,0,0,4,0],
                    [2,0,0,3,0,0,9,0,0]]
        self.run_sudoku_test(3, original)

class Test_3_TestScheduling(unittest.TestCase):
    def opencase(self, casename):
        with open(os.path.join(TEST_DIRECTORY, casename + ".json")) as f:
            v = json.load(f)
            return ({p[0] : set(p[1])
                     for p in v[0].items()}, v[1])

    def satisfiable(self, casename):
        students, sessions = self.opencase(casename)
        formula = lab.boolify_scheduling_problem(copy.deepcopy(students),
                                                      copy.deepcopy(sessions))
        sched = lab.satisfying_assignment(formula)
        self.assertIsNotNone(sched)

        unplaced_students = set(students)

        for var, val in sched.items():
            if val:
                student, session = var.split('_')

                self.assertIn(student, unplaced_students, "Students should be assigned at most one session.")
                unplaced_students.remove(student)

                self.assertIn(student, students, "This is not a valid student.")
                self.assertIn(session, students[student], "Student should be assigned a desired session.")

                self.assertIn(session, sessions, "This is not a valid session.")
                self.assertTrue(sessions[session] >= 1, "This session is over-capacity.")
                sessions[session] -= 1

        self.assertEqual(len(unplaced_students), 0)

    def unsatisfiable(self, casename):
        students, sessions = self.opencase(casename)
        sched = lab.satisfying_assignment(
            lab.boolify_scheduling_problem(copy.deepcopy(students),
                                                copy.deepcopy(sessions)))
        self.assertIsNone(sched)

    def test_A_3_3(self):
        self.satisfiable('3_3')

    def test_B_10_10(self):
        self.satisfiable('10_10')

    def test_C_10_10_unsat(self):
        self.unsatisfiable('10_10_unsat')

    def test_D_15_5(self):
        self.satisfiable('15_5')

    def test_E_17_5_unsat(self):
        self.unsatisfiable('17_5_unsat')


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
