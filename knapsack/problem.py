def show_inputs(n : int) -> None:
    f = open("knapsack/cases/" + str(n), 'r')
    print(f.read())
    f.close()
    return