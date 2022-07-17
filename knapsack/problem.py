import os

def get_cases():
    cases = []
    for i in os.listdir("knapsack/cases"):
        cases.append(int(i))
    
    cases.sort()

    return cases   

def show_input(n : int) -> None:
    f = open("knapsack/cases/" + str(n), 'r')
    print(f.read())
    f.close()
    return

def get_input(n : int) -> tuple:
    f = open("knapsack/cases/" + str(n), 'r')
    lines = f.readlines()
    f.close()
    n, k = map(int, lines[0].split())
    weights = []
    values = []
    for i in range(1, n+1):
        w, v = map(int, lines[i].split())
        values.append(v)
        weights.append(w)
        
    
    return (n, k, values, weights)

def test_solver(solver, n):
    print("Input:")
    show_input(n)
    n, k, values, weights = get_input(n)
    print("Output:")
    value, items = solver(n, k, values, weights)
    print(value)
    [print(item, end = " ") for item in items]
    return


