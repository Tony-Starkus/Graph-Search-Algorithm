"""
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
n1 = Node("n1", {
    "l": {
        "m": 3,
        "c": 3
    },
    "r": {
        "m": 0,
        "c": 0
    }
})

n2 = Node("n2", {
    "l": {
        "m": 3,
        "c": 2
    },
    "r": {
        "m": 0,
        "c": 1
    }
})

n3 = Node("n3", {
    "l": {
        "m": 2,
        "c": 2
    },
    "r": {
        "m": 1,
        "c": 1
    }
})

n4 = Node("n4", {
    "l": {
        "m": 1,
        "c": 1
    },
    "r": {
        "m": 2,
        "c": 2
    }
})

n5 = Node("n5", {
    "l": {
        "m": 0,
        "c": 0
    },
    "r": {
        "m": 3,
        "c": 3
    }
})

n6 = Node("n6", {
    "l": {
        "m": 3,
        "c": 1
    },
    "r": {
        "m": 0,
        "c": 2
    }
})

n7 = Node("n7", {
    "l": {
        "m": 3,
        "c": 0
    },
    "r": {
        "m": 0,
        "c": 3
    }
})

n1.edges_to = [[n2], [n3], [n6]]
n2.edges_to = [[n3], [n6], [n7]]
n3.edges_to = [[n4]]
n4.edges_to = [[n5]]
n6.edges_to = [[n2], [n6]]

graph = Graph(n1, n5, [n1, n2, n3, n4, n5, n6, n7])
graph.show_graph()
graph.dfs_search()

"""
arquivo = open('graph.json')

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")
n5 = Node("E")
n6 = Node("F")

graph = Graph(n1)

n1.edges_to = [[n2, 5], [n3]]
n2.edges_to = [[n4, 10], [n5, 25]]
n3.edges_to = [[n6, 10]]
n5.edges_to = [[n6, 0]]

print(f"{n1}: {n1.get_edges_to(value=True, with_coust=False)}")

print(f"{n1}: {n1.edges_to}")
print(f"{n2}: {n2.edges_to}")
print(f"{n3}: {n3.edges_to}")
print(f"{n4}: {n4.edges_to}")
print(f"{n5}: {n5.edges_to}")
print(f"{n6}: {n6.edges_to}")
print(f"{n7}: {n7.edges_to}")
"""
