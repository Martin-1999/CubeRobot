import kociemba


#得到还原步骤
def CubeSolve(str_condition):
    try:
        str_step = kociemba.solve(str_condition)
    except ValueError:
        return None
    else:
        operations = str_step.split(" ")
        print(operations)
        return operations
