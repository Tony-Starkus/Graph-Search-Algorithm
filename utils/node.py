
class Node:

    def __init__(self, name, value):
        """
        :param name: Name/id for the node. Must be unique
        :param value: Anything you want.

        :var edges_to type(list):  struct sample -> [[node_object, coust_to_node], [node_object, coust_to_node]]
        The edges_to is list of list, where each list on index 0 is a node object, and index 1 is a int that represents
        the coust to go to the node in index 0.
        """
        self.__name = name
        self.__value = value
        self.__edges_to = []

    @property
    def value(self):
        return self.__value

    @property
    def coust(self):
        return self.__coust

    @property
    def name(self):
        return self.__name

    @property
    def edges_to(self):
        return self.__edges_to

    def get_edges_to(self, value=True, with_coust=True):
        """
        :param value: Return list with nodes values instead of Node Object.
        :param with_coust: Return list with coust to a Node Object.
        :return: a list of list that each list represents an edge with node and coust.
        """
        if value:
            if with_coust:
                result = []
                for node in self.__edges_to:
                    result.append([node[0].value, node[1]])
                return result
            return [node[0].value for node in self.__edges_to]
        if with_coust is False:
            return [node[0] for node in self.__edges_to]
        return self.__edges_to if with_coust and value else [node[0] for node in self.__edges_to]

    @edges_to.setter
    def edges_to(self, list_nodes):
        """
        :param list_nodes: a list of list that each list represents an edge with node and coust. If coust not informed,
        the default value is 0.
        :return: edge_to variable value.
        """
        for node in list_nodes:
            if len(node) == 1:
                self.__edges_to.append([node[0], 0])
            else:
                if not isinstance(node[0], Node):
                    raise Exception("First value must be a node object")
                if not isinstance(node[1], int):
                    raise Exception("Second value must be an int number")
                self.__edges_to.append(node)
        return self.__edges_to

    def __str__(self):
        return self.__name
