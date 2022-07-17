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
        weights.append(w)
        values.append(v)
    
    return (n, k, weights, values)

def test_solver(solver, n):
    print("Input:")
    show_input(n)
    n, k, weights, values = get_input(n)
    print("Output:")
    value, items = solver(n, k, weights, values)
    print(value)
    [print(item, end = " ") for item in items]
    return
