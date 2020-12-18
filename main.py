"""
Python 3.7

https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

http://www.inf.ufsc.br/grafos/temas/travessia/canibais.htm

Initial State -> All missionaries and cannibals on the same side of the river.
Objective Test -> Missionaries number on a river side can't be less than cannibals number.
Successor Function -> River: go from a side to another side.
Coust Function -> Number of times the boat cross the river.

m -> Missionary
c -> Cannibal
r -> Right side of river
l -> Left side of river
"""
from utils.node import Node
from utils.graph import Graph

# Initial State
n1 = Node({
    "l": {
        "m": 3,
        "c": 3
    },
    "r": {
        "m": 0,
        "c": 0
    }
})

n2 = Node({
    "l": {
        "m": 3,
        "c": 2
    },
    "r": {
        "m": 0,
        "c": 1
    }
})

n3 = Node({
    "l": {
        "m": 2,
        "c": 2
    },
    "r": {
        "m": 1,
        "c": 1
    }
})

n4 = Node({
    "l": {
        "m": 1,
        "c": 1
    },
    "r": {
        "m": 2,
        "c": 2
    }
})

n5 = Node({
    "l": {
        "m": 0,
        "c": 0
    },
    "r": {
        "m": 3,
        "c": 3
    }
})

n6 = Node({
    "l": {
        "m": 3,
        "c": 1
    },
    "r": {
        "m": 0,
        "c": 2
    }
})

n7 = Node({
    "l": {
        "m": 3,
        "c": 0
    },
    "r": {
        "m": 0,
        "c": 3
    }
})

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
print(f"{n6}: {n6.edges_to}")"""
