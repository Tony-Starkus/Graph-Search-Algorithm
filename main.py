"""
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

graph = Graph("A")

n1.vertices = [n2, n3]
n2.vertices = [n4, n5]
n3.vertices = [n6]
n5.vertices = [n6]

print(f"{n1}: {n1.vertices}")
print(f"{n2}: {n2.vertices}")
print(f"{n3}: {n3.vertices}")
print(f"{n4}: {n4.vertices}")
print(f"{n5}: {n5.vertices}")
print(f"{n6}: {n6.vertices}")

