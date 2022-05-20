#This is for the MinKnapSack

    
# A is the item list, each item has value associated with them. 
    # cost of a item is also included.
# V is the value, target???
# c is the cost
def solveMaximumKnapsack(A, t):
    target = t
    itemList = A
    maximumA = 0
    #Settign the maximumA to equal an item with the max value. 
    for item in itemList:
        if item.getValue() >= maximumA:
            maximumA = item.getValue()
    takenItem = [[] for _ in range(len(itemList) * maximumA + 1)]
    
    nextTarget = 0
    
    minCost = [[] for _ in range(len(itemList)+ 1)]
    index = 0
    #print("The length of the itemList is:",len(listItems))
    #print("Valuelist before looping.", valueList)
    while index < len(itemList)+1:
        for t in range(0, (len(itemList)*maximumA + 1)):
            minCost[index].append(0)
            takenItem[index].append(0)
                #print("Debugging the inner loop. Iteration: ", t)
        index += 1

    

    # By this point the maximumA is the item with the highest value. 

#     """"
#     for i =1 to n 
#         set MinCost[i,0] = 0
#     end for
# """
    
    for i in range(1, len(itemList)):
        minCost[i][0] = 0


# """"
#     when t<= v(1), target t can be achieved by taking object 1. 
#     for t = 1 to v(1)
#         set MinCost[1,t] = c(1)
#         set Take[1,t] = Yes
#     end for
# """"
    value = int(itemList[0].getValue())
    if target <= value:
        for target in range(1, itemList[0].getValue()+1):
            minCost[1][target] = itemList[0].getCost()
            takenItem[1][target] = True


# """
#     when t > v(1) target cannot be reached with only object 1 available
#     for t = v(1) + 1 to n * v(amax)
#         set MinCost[1,t] = Infinity
#         set Take[1,t] = No
#     end for
# """"
    if target > value:
        for target in range(itemList[0].getValue() + 1, len(itemList) * maximumA):
            minCost[1][target] = 99999999999999
            takenItem[1][target] = False


# """
#     for i = 2 to n
#         for t = 1 to n*v(amax)
#             set NextT = MAX{ 0,t - v(i)} //dont let index go below 0
#             if MinCost[ i - 1, t] <= c(i) + MinCost[i - 1], NextT] 
#                 then begin //dont include object i
#                     Set minCOst[i,t] = MinCost[i -1, t]
#                     set Take[i, t] = No
#                     end
#             else begin //include i
#                 set MinCost[i,t] = c(i) + MinCost[i -1 , NExtT]
#                 set take[i,t] = Yes
#             end
#         end for
#     end for
# return Mincost and Take
# """
    for i in range(2, len(itemList)):
        for target in range(1, len(itemList) * maximumA ):

            nextTarget = max(0, target - itemList[i].getValue())
            # print("Next target is :", nextTarget)
            # print("The value compared against is", minCost[i -1][target])
            if minCost[i -1][target] <= itemList[i].getCost() + minCost[i -1][nextTarget]:
                minCost[i][target] = minCost[i -1][target]
                takenItem[i][target] = False
            else:
                minCost[i][target] = itemList[i].getCost() + minCost[i-1][nextTarget]
                takenItem[i][target] = True

    for i in range(maximumA * len(itemList)-1, -1, -1):
        if minCost[len(itemList)-1][i] <= target:
            return i