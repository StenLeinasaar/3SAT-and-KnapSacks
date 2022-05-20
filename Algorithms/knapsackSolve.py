# from UTILS import KnapSackItem
# from KnapSackItem import KnapSackItem

def knapSackSolv(weight, items):
    valueList = None
    listItems = items
    maxWeight = weight

    ##CREATES THE MATRIX 
    valueList = [[] for _ in range(len(listItems)+ 1)]

    index = 0
    #Adding all the column values as 0
    while index < len(listItems) +1:
        for t in range(0, maxWeight+1):
            valueList[index].append(0)
        index += 1

    #the number of lists in the valueList is number of rows,
    #The number of elements in each list inside of valuelist is a number of columns. 
    # FIll in the base of the table: 

    # for w <- 0 to W
    #     #I have to craete n+1 lists in the F LIST. 
    #     F[n+1], w] = 0
    for w in range(0, maxWeight+1):
        valueList[len(listItems)][w] = 0
    #Fill in the first column. 
    # for i <- 1 to n+1
    #     F[i,0] = 0
    for i in range(0, len(listItems)+1):
        valueList[i][0] = 0

    #Not inclusive of the second parameter
    # for i <- n down to 1
    #     for w  <- 0 to W
    #         if wi <= W
    #             F[i, w] = MAX(F[i+1],w-wi] + vi, F[i+1, w])
    #         else F[i,w] = F[i+1, w]
    idx = len(listItems) -1
    #Fill in the valueList
    while(idx >= 0):
        for w in range(0, maxWeight +1):
            if listItems[idx].getCost() <= maxWeight:
                valueList[idx][w] = max((valueList[idx + 1][w - listItems[idx].getCost()] + listItems[idx].getValue()), valueList[idx +1][w])
            else:
                valueList[idx][w] = valueList[idx+1][w]
        idx -= 1
    return valueList[0][maxWeight]









    






