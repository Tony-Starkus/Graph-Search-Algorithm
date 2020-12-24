from utils.node import Node


class Graph:

    def __init__(self, node_root, node_objective, nodes=[]):
        self.__goal = None
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

    def dfs(self, node, visited_nodes, border, max_deep):
        """
        Function by: Thalisson
        :param node: node object
        :param visited_nodes: list of node objects
        :param border: list of node objects
        :param max_deep: Max deep of search in the graph
        :return: None
        """
        if node.deep > max_deep:
            max_deep = node.deep
        if node in visited_nodes:
            return
        visited_nodes.append(node.name)
        if node is self.__node_objective:
            print("found!")
            print("Deep:", node.deep)
            print("Max Deep:", max_deep)
            print(f"Total nodes visited: {len(visited_nodes)}")
            print(f"Visited nodes: {visited_nodes}")
            print("Generated nodes:", len(border))
            exit()
        elif len(node.edges_to):
            deep += 1
            for item2 in node.get_edges_to(value=False, with_coust=False):
                border = border + [item for item in item2.get_edges_to(value=False, with_coust=False)]
                self.dfs(item2, visited_nodes, border, max_deep)

    def dfs_search(self):
        """
        Function by: Thalisson.
        :return: None
        """
        visited_nodes = []
        border = [self.__node_root]
        border = border + [item for item in self.__node_root.get_edges_to(value=False, with_coust=False)]
        max_deep = 0
        # print("1:", [item.name for item in border])
        self.dfs(self.__node_root, visited_nodes, border, max_deep)
