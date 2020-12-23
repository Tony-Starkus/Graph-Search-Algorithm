"""
Auth: Thalisson

Python 3.7

https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

http://www.inf.ufsc.br/grafos/temas/travessia/canibais.htm

Initial State -> All missionaries and cannibals on the same side of the river.
Objective Test -> Cross all Missionaries and cannibals to the other side of the river.
Test function -> Missionaries number on a river side can't be less than cannibals number.
Successor Function -> River: go from a side to another side.
Coust Function -> Cross the river (It's a constant value).

Heuristc -> The best Heuristc for this problem is transport one missionary and one cannibal per node.
A heurística a ser usada aqui pode ser a heurística admissível, onde o valor H de um node pode ser igual ao total de
nodes que vai ser necessário visitar para chegar no node objetivo. OU então o valor de H pode ser definido de acordo com
a quantidade de M e C que atravessam o rio node.

m -> Missionary
c -> Cannibal
r -> Right side of river
l -> Left side of river
"""
from utils.node import Node
from utils.graph import Graph

# Initial State
n0 = Node("n0", {
    "l": {
        "m": 3,
        "c": 3
    },
    "r": {
        "m": 0,
        "c": 0
    }
})

n1 = Node("n1", {
    "l": {
        "m": 3,
        "c": 2
    },
    "r": {
        "m": 0,
        "c": 1
    }
})

n2 = Node("n2", {
    "l": {
        "m": 2,
        "c": 2
    },
    "r": {
        "m": 1,
        "c": 1
    }
})

n3 = Node("n3", {
    "l": {
        "m": 3,
        "c": 1
    },
    "r": {
        "m": 0,
        "c": 2
    }
})

n4 = Node("n4", {
    "l": {
        "m": 3,
        "c": 0
    },
    "r": {
        "m": 0,
        "c": 3
    }
})

n5 = Node("n5", {
    "l": {
        "m": 1,
        "c": 1
    },
    "r": {
        "m": 2,
        "c": 2
    }
})

n6 = Node("n6", {
    "l": {
        "m": 0,
        "c": 0
    },
    "r": {
        "m": 3,
        "c": 3
    }
})

n0.edges_to = [[n1], [n2], [n3]]
n1.edges_to = [[n2], [n3], [n4]]
n2.edges_to = [[n5]]
n3.edges_to = [[n1], [n2], [n4], [n5]]
n5.edges_to = [[n6]]

graph1 = Graph(n0, n6, [n0, n1, n2, n3, n4, n5, n6])
graph1.show_graph()
graph1.dfs_search()

graph2 = Graph()

graph2.addEdge(n0, n1)
graph2.addEdge(n0, n2)
graph2.addEdge(n0, n3)
graph2.addEdge(n1, n2)
graph2.addEdge(n1, n3)
graph2.addEdge(n1, n6)
graph2.addEdge(n2, n4)
graph2.addEdge(n3, n1)
graph2.addEdge(n3, n2)
graph2.addEdge(n3, n4)
graph2.addEdge(n3, n6)
graph2.addEdge(n4, n5)
graph2.addEdge(n5, n5)

"""
arquivo = open('graph1.json')

n0 = Node("A")
n1 = Node("B")
n2 = Node("C")
n3 = Node("D")
n4 = Node("E")
n5 = Node("F")

graph1 = Graph(n0)

n0.edges_to = [[n1, 5], [n2]]
n1.edges_to = [[n3, 10], [n4, 25]]
n2.edges_to = [[n5, 10]]
n4.edges_to = [[n5, 0]]

print(f"{n0}: {n0.get_edges_to(value=True, with_coust=False)}")

print(f"{n0}: {n0.edges_to}")
print(f"{n1}: {n1.edges_to}")
print(f"{n2}: {n2.edges_to}")
print(f"{n3}: {n3.edges_to}")
print(f"{n4}: {n4.edges_to}")
print(f"{n5}: {n5.edges_to}")
print(f"{n6}: {n6.edges_to}")
"""
