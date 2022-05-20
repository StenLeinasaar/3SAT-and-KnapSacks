class CreateGraph(object):

    def __init__(self, vertices):
        self.vertex = vertices
        #Store in default dictionary
        self.graph = []
    
    def addEdge(self, startVertex, endVertex, weight):
        self.graph.append([startVertex, endVertex, weight])


    def find(self, parent, elementToFind):
        if parent[elementToFind] == elementToFind:
            return elementToFind
        return self.find(parent, parent[elementToFind])  


    def union(self, parent, rank, first, second):
        firstRoot = self.find(parent, first)
        secondRoot = self.find(parent, second)

        if rank[firstRoot] < rank[secondRoot]:
            parent[firstRoot] = secondRoot
        elif rank[firstRoot] > rank[secondRoot]:
            parent[secondRoot] = firstRoot
        else:
            parent[secondRoot] = firstRoot
            rank[firstRoot] += 1
