from numpy.linalg import solve

def solveLinear(variables, equations):
    if len(variables) != len(equations):
        print("Incorrect number of equations!")
        return None
    variables = list(variables)
    solution = solve([[0 if variable not in equation else equation[variable] for variable in variables] for equation in equations], [0 if 1 not in equation else -equation[1] for equation in equations])
    return {variables[variable]: solution[variable] for variable in range(len(variables))}
                
    
    
    
