from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addConnections(self, node_val, connections):
        self.graph[node_val] = connections

    def getGraph(self):
        print self.graph

class Solution(object):
    def __init__(self, graph):
        self.graph = graph

    def getNeighborhood(self, node, depth):
        neighbors = set()
        self.getNeighborhoodRecursive(neighbors, node, int(depth))
        print list(neighbors)

    def getNeighborhoodRecursive(self, neighbors, node, depth):
        if node not in self.graph:
            return
        elif node in self.graph:
            for v in self.graph[node]:
                if depth == 0:
                    return []
                elif depth != 0:
                    self.getNeighborhoodRecursive(neighbors, v, depth - 1)
                    neighbors.add(v)

graph = {'1' : ['2', '4'],
         '2' : ['1', '3', '4'],
         '3' : ['2', '5'],
         '4' : ['1', '2', '5'],
         '5' : ['3', '4', '6'],
         '6' : ['5']}


G = Graph()
G.addConnections(1, [2, 4])
G.getGraph()
S = Solution(graph)

S.getNeighborhood('1','0')
S.getNeighborhood('1','1')
S.getNeighborhood('1','2')
S.getNeighborhood('1','3')