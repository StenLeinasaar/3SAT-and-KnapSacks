#your own Disjoint-Set implementation using
#union by rank with path compression.

import CreateGraph

#Takes in graph as a paramtere to find MST
def KruskalMST(graph):

    result = []  # This will store  MST
    # An index variable, used for sorted edges
    i = 0  
    # An index variable, used for result[]
    e = 0
    #Sort all the edges in
    # non-decreasing order of their
    # weight.  If we are not allowed to change the
    # given graph, we can create a copy of graph
    #TODO sort the same way like you did with knapsack item. 
    graph = sorted(graph, key=lambda item:item[2])
    
    parent = []
    rank = []

    # Create V subsets with single elements
    #TODO aaah, rank is confusing. Look it up and do it agai. 
    for node in range(graph.Vertex):
        parent.append(node)
        rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < graph.Vertex - 1:

        # Pick the smallest edge and increment
            u, v, w = graph.graph[i]
            i = i + 1
            x = graph.find(parent, u)
            y = graph.find(parent, v)

            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                graph.union(parent, rank, x, y)
            # Else discard the edge, lmao sten...

        minimumCost = 0
        print ("Edges in the constructed MST")
        
        #TODO Come back here. 
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)



graph = CreateGraph(4)
KruskalMST(graph)