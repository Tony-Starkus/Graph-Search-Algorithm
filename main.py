"""
Python 3.7

https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

"""
from utils.node import Node
from utils.graph import Graph


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

print(f"{n1}: {n1.get_edges_to(value=False, with_coust=True)}")

print(f"{n1}: {n1.edges_to}")
print(f"{n2}: {n2.edges_to}")
print(f"{n3}: {n3.edges_to}")
print(f"{n4}: {n4.edges_to}")
print(f"{n5}: {n5.edges_to}")
print(f"{n6}: {n6.edges_to}")
