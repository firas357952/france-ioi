graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F", "G"],
    "C": [],
    "D": ["H"],
    "E": ["A"],
    "F": [],
    "G": [],
    "H": [],
}

pile = ["A"]
memo = {"A": None}
while pile != []:
    print(pile)
    node = pile[-1]
    if graph[node] != []:
        element = graph[node].pop(0)
        if element not in memo:
            memo[element] = None
            pile.append(element)
    else:
        pile.pop(-1)
