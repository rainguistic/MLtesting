class Node:
    def __init__(self, name, type, data):
        self.name = name
        self.type = type
        self.data = data
        self.associations = []

class Edge:
    def __init__(self, node1, node2, type, weight):
        self.node1 = node1
        self.node2 = node2
        self.type = type
        self.weight = weight