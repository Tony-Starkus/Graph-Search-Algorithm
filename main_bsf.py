"""
Auth: Italo
"""
from collections import defaultdict


class Graph:
 
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    def add_goal(self, v):
        self.goal = v

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u['state']].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []
 
        # Mark the source node as 
        # visited and enqueue it
        queue.append(s)
        visited[s['state']] = True
        visited_nodes = []

        while queue:
 
            # Dequeue a vertex from 
            # queue and print it
            s = queue.pop(0)
            # print(s)

            print(f"n{s['state']}")
            visited_nodes.append(f"n{s['state']}")
            if s == self.goal:
                print('Visited nodes:', visited_nodes)
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s['state']]:
                if visited[i['state']] == False:
                    queue.append(i)
                    visited[i['state']] = True
 

# States
n0 = {
    "state": 0,
    "l": {
        "m": 3,
        "c": 3
    },
    "r": {
        "m": 0,
        "c": 0
    }
}

n1 = {
    "state": 1,
    "l": {
        "m": 3,
        "c": 2
    },
    "r": {
        "m": 0,
        "c": 1
    }
}

n2 = {
    "state": 2,
    "l": {
        "m": 2,
        "c": 2
    },
    "r": {
        "m": 1,
        "c": 1
    }
}

n3 = {
    "state": 3,
    "l": {
        "m": 1,
        "c": 1
    },
    "r": {
        "m": 2,
        "c": 2
    }
}

n4 = {
    "state": 4,
    "l": {
        "m": 0,
        "c": 0
    },
    "r": {
        "m": 3,
        "c": 3
    }
}

n5 = {
    "state": 5,
    "l": {
        "m": 3,
        "c": 1
    },
    "r": {
        "m": 0,
        "c": 2
    }
}

n6 = {
    "state": 6,
    "l": {
        "m": 3,
        "c": 0
    },
    "r": {
        "m": 0,
        "c": 3
    }
}


g = Graph()

# Adicionando as conexões entre os vertices
g.addEdge(n0, n1)
g.addEdge(n0, n2)
g.addEdge(n0, n3)
g.addEdge(n1, n2)
g.addEdge(n1, n3)
g.addEdge(n1, n4)
g.addEdge(n2, n5)
g.addEdge(n3, n2)
g.addEdge(n3, n1)
g.addEdge(n3, n4)
g.addEdge(n3, n5)
g.addEdge(n5, n6)
g.addEdge(n6, n6)

# Adicionando o nó objetivo
g.add_goal(n6)

# Iniciando a BFS
g.BFS(n0)
