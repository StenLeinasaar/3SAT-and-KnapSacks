# with Triangle Inquality.

#I might need Prim's algorithm to be implemented. 

#The least distant path to reach a vertex j from i is always to reach j directly from i, rather than through some other vertex k
# i, e dis(i,j) is always less than or equal to dis(i,k) + dist(k,j). The triangle-inequlity


# Prim's Algorithm in Python


INF = 9999999
#Hard coded number of vertices in the graph. 
N = 5
#Hard coding a graph
G = [[0, 7, 5, 0, 0],[19, 0, 5, 4, 2],[5, 1, 0, 1, 6],[0, 2, 1, 0, 1],[0, 2, 3, 7, 0]]



def prims(Graph):
    global INF, N
    nodes = []
    for i in range(len(Graph)):
        nodes.append(0)

    no_edge = 0

    nodes[0] = True

    # printing for edge and weight
    #print("Edge : Weight\n")
    while (noEdge < N - 1):
        
        minimum = INF
        a = 0
        b = 0
        for m in range(N):
            if nodes[m]:
                for n in range(N):
                    if ((not nodes[n]) and Graph[m][n]):  
                        # not in selected and there is an edge
                        if minimum > Graph[m][n]:
                            minimum = Graph[m][n]
                            a = m
                            b = n
        nodes[b] = True
        noEdge += 1
    return minimum


print(prims(G))

#Start from 1
#Generate MST
#List vertices visited in preorder walk of the constructer MST, and add 1 at the end. 
