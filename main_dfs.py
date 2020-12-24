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
n0 = Node("n0", "3c 3m L", 0)
n1 = Node("n1", "1c 1m R", 1)
n2 = Node("n2", "2c 0m R", 1)
n3 = Node("n3", "1c 0m R", 1)
n4 = Node("n4", "2c 3m L", 2)
n5 = Node("n5", "3c 0m R", 3)
n6 = Node("n6", "1c 3m L", 4)
n7 = Node("n7", "2c 2m R", 5)
n8 = Node("n8", "2c 2m L", 6)
n9 = Node("n9", "1c 3m R", 7)
n10 = Node("n10", "3c 0m L", 8)
n11 = Node("n11", "2c 3m R", 9)
n12 = Node("n12", "2c 0m L", 10)
n13 = Node("n13", "1c 1m L", 10)
n14 = Node("n14", "3c 3m R", 11)

n0.edges_to = [[n1], [n2], [n3]]
n1.edges_to = [[n4]]
n2.edges_to = [[n4]]
n4.edges_to = [[n5]]
n5.edges_to = [[n6]]
n6.edges_to = [[n7]]
n7.edges_to = [[n8]]
n8.edges_to = [[n9]]
n9.edges_to = [[n10]]
n10.edges_to = [[n11]]
n11.edges_to = [[n12], [n13]]
n12.edges_to = [[n14]]
n13.edges_to = [[n14]]

graph1 = Graph(n0, n14, [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14])
graph1.show_graph()
graph1.dfs_search()
