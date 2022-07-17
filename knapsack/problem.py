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
        v, w = map(int, lines[i].split())
        values.append(v)
        weights.append(w)
        
    
    return (n, k, values, weights)

def test_solver(n, solver):
    print("Input:")
    show_input(n)
    n, k, values, weights = get_input(n)
    print("Output:")
    items = solver(n, k, values, weights)
    value = 0
    for i in range(n):
        if items[i] == 1:
            value += values[i]
    
    print(value)
    [print(item, end = " ") for item in items]
    return

def sort_by_values(n, V) -> list:
    items = [[V[i], i] for i in range(n)]
    items = sorted(items, key = lambda x: x[0], reverse = True)
    I = [item[1] for item in items]
    return I

def sort_by_density(n, V, W) -> list:
    items = [[V[i]/W[i], i] for i in range(n)]
    items = sorted(items, key = lambda x: x[0], reverse = True)
    I = [item[1] for item in items]
    return I
