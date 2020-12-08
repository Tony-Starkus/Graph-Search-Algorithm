from .node import Node


class Graph:

    def __init__(self, node_root, nodes=[]):
        self.__nodes = nodes
        if isinstance(node_root, Node):
            self.__node_root = node_root
        else:
            raise Exception("The root node must be a Node object.")

    def add_node(self, node):
        self.__nodes.append(node)
