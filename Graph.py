import json


class WeightedGraph:
    # graph = { 'v1':{'v2': cost, ... } }
    def __init__(self, d=None):
        if d:
            self.graph = d
        else:
            self.graph = {}

    def __repr__(self):
        return str(self.graph)

    def __getitem__(self, key):
        # key = (v1, v2,)
        v1, v2 = key
        if v1 in self.graph:
            if v2 in self.graph[v1]:
                return self.graph[v1][v2]
        return None

    def addVertex(self, v):
        if v not in self.graph:
            self.graph[v] = {}

    def addEdge(self, v1, v2, cost):
        if v1 not in self.graph:
            self.graph[v1] = {v2: cost}

        # If v1 and v2 not connected
        elif v2 not in self.graph[v1]:
            self.graph[v1][v2] = cost

        if v2 not in self.graph:
            self.graph[v2] = {v1: cost}

        # If v2 and v1 not connected
        elif v1 not in self.graph[v2]:
            self.graph[v2][v1] = cost

    def vertices(self):
        return list(self.graph.keys())

    def __iter__(self):
        # return edges with costs
        for v1 in self.graph.keys():
            for v2 in self.graph[v1].keys():
                yield (v1, v2, self.graph[v1][v2])

    def dump(self, buffer):
        json.dump(self.graph, buffer, indent=4)

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            graph = json.load(f)
            g = WeightedGraph(graph)
        return g