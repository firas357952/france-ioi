def bfs(node, adjlist):
    n = 1
    file = [node]
    visited = {}
    for i in range(len(adjlist)):
        visited[i] = False
    visited[node] = True
    while file != []:
        for element in adjlist[file[0]]:
            if not (visited[element]):
                file.append(element)
                visited[element] = True
                n += 1
        print(file)
        file.pop(0)
    return n


if __name__ == "__main__":

    adjlist = {
        1: [8],
        8: [1, 3],
        3: [4, 8, 2],
        4: [3],
        2: [3, 6],
        6: [2, 7, 5, 0],
        7: [6],
        5: [6, 9],
        9: [5],
        0: [6],
    }

    result = bfs(1, adjlist)
    print(f"Count: {result}")
