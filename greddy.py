from collections import defaultdict
from queue import PriorityQueue
from states import states

'''
    Author: Ítalo Oliveira

    References: https://docs.python.org/3/library/queue.html#queue.PriorityQueue
                https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
                http://www.inf.ufsc.br/grafos/temas/travessia/canibais.htm
'''

class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)
        self.max_deep = 0
        self.solution_deep = 0
        self.order_visited = []
 
    def add_goal(self, node):
        self.goal = node

    def add_edge(self,u,v):
        self.graph[u].append(v)
 
    def print_info(self):
        print('### Ordem da travessia:')
        for node in self.order_visited:
            state = states[node]
            print(f"*Nó: {node} - Estado: {state['state']}")
        
        print(f'### Nós gerados: {self.nodes_generates}')
        print(f'### Nós visitados: {len(self.order_visited)}')
        print(f'### Profudindade máxima atingida: {self.max_deep}')
        print(f'### Profudindade da solução: {self.solution_deep}')

    
    def greddy(self, node):
        visited = set()
        self.order_visited = []

        # Create priority queue and add root node
        queue = PriorityQueue()
        queue.put((states[node]['heuristic'], node))

        self.nodes_generates = 1

        visited.add(node)
 
        while not queue.empty():
 
            item = queue.get()
            node = item[1]

            self.order_visited.append(node)

            if node == self.goal:
                self.solution_deep = states[node]['deep']
                self.print_info()
                break

            for v in self.graph[node]:
                if v not in visited:
                    queue.put((states[v]['heuristic'], v))
                    visited.add(v)
                    
                    self.nodes_generates += 1
        
                    if states[v]['deep'] > self.max_deep:
                        self.max_deep = states[v]['deep']


# Main
g = Graph()

# Adicionando as conexões entre os vertices
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 3)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(7, 8)
g.add_edge(8, 9)
g.add_edge(9, 10)
g.add_edge(10, 11)
g.add_edge(11, 12)
g.add_edge(11, 13)
g.add_edge(12, 14)
g.add_edge(13, 14)
g.add_edge(14, 14)

# Adicionando o nó objetivo
g.add_goal(14)

print('### GERANDO GREDDY COM HEURISTICA ###')
g.greddy(0)