from utils.node import Node


class Graph:

    def __init__(self, node_root, node_objective, nodes=[]):
        if isinstance(node_root, Node):
            self.__node_root = node_root
        else:
            raise Exception("The root node must be a Node object.")

        if isinstance(node_objective, Node):
            self.__node_objective = node_objective
        else:
            raise Exception("The node objective must be a Node object.")

        for item in nodes:
            if not isinstance(item, Node):
                raise Exception("The item in list must be a Node object.")
        self.__nodes = nodes

    def add_node(self, node):
        self.__nodes.append(node)

    def show_graph(self):
        for node in self.__nodes:
            print(f"{node}: {[item.name for item in node.get_edges_to(False, False)]}")

    def dfs(self, node, visited_nodes):
        visited_nodes.append(node.name)
        if node is self.__node_objective:
            print("found!")
            print(f"Visited nodes: {visited_nodes}")
            exit()
        elif len(node.edges_to):
            for item2 in node.get_edges_to(value=False, with_coust=False):
                self.dfs(item2, visited_nodes)

    def dfs_search(self):
        visited_nodes = []
        for item1 in self.__nodes:
            self.dfs(item1, visited_nodes)



