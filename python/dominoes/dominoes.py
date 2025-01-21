# https://www.geeksforgeeks.org/hamiltonian-cycle/


# pylint: disable=invalid-name
class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.V = vertices

    def isSafe(self, v, pos, path):
        if not self.graph[path[pos - 1]][v]:
            return False
        return all(vertex != v for vertex in path)

    def hamCycleUtil(self, path, pos):
        if pos == self.V:
            return self.graph[path[pos - 1]][path[0]] == 1
        for v in range(1, self.V):
            if self.isSafe(v, pos, path):
                path[pos] = v
                if self.hamCycleUtil(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def hamCycle(self):
        path = [-1] * self.V
        path[0] = 0
        if not self.hamCycleUtil(path, 1):
            return None
        return path


def can_chain(dominoes):
    if not dominoes:
        return dominoes
    if len(dominoes) == 1:
        return dominoes if dominoes[0][0] == dominoes[0][1] else None
    graph = Graph(len(dominoes))
    graph.graph = [
        [
            1 if i != j and set(domino).intersection(set(other_domino)) else 0
            for j, other_domino in enumerate(dominoes)
        ]
        for i, domino in enumerate(dominoes)
    ]
    if not (cycle := graph.hamCycle()):
        return None
    first_domino = dominoes[cycle[0]]
    second_domino = dominoes[cycle[1]]
    common_element = set(first_domino).intersection(set(second_domino)).pop()
    if first_domino[1] != common_element:
        first_domino = first_domino[::-1]
    if second_domino[0] != common_element:
        second_domino = second_domino[::-1]
    solution = [first_domino, second_domino]
    link = second_domino[1]
    for domino_index in cycle[2:]:
        domino = dominoes[domino_index]
        if domino[0] != link:
            domino = domino[::-1]
        solution.append(domino)
        link = domino[1]
    return solution
