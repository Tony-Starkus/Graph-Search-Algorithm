
class Node:

    def __init__(self, value, coust=0, vertices=[]):
        self.__value = value
        self.__coust = coust
        self.__vertices = vertices

    @property
    def value(self):
        return self.__value

    @property
    def coust(self):
        return self.__coust

    @property
    def vertices(self):
        return [node.value for node in self.__vertices]

    @vertices.setter
    def vertices(self, list_nodes):
        self.__vertices = list_nodes

    def __str__(self):
        return self.__value
