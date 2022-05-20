

import copy
import math
from UTILS import GenerateProblems
from math import floor
from UTILS import KnapSackItem
from UTILS import ReportGenerator
import time


# GenerateKnapSack call the testing method too. 
# THe instance created by GEneratePRoblems is appended to the testing file to store what I test. 
def generateKnapSack():
    forTesting = []
    knapSack = []
    for x in range(101):
        #print("test generation:", x)
        instance = GenerateProblems.generateKnapSack()
        #print("Instance generated is: " , instance)
        
    #value is the 0 index, cost is 1
        #print("For testing variable before I start appending.", forTesting)
        for tuple in instance:
            # print("Value in tuple", tuple[0], tuple[1])
            item = KnapSackItem.KnapSackItem(tuple[0], tuple[1])
            knapSack.append(item)
            # print("Item appended is with value of:" , item.getValue())
            # print("item is with the cost of: ", item.getCost())
        #print("For testing before appending knapsacl", forTesting)
        forTesting.append(knapSack)
        knapSack = []
    #print(forTesting)

    # Here will call the tests for knapSack 
    # Call for each knapSack Instance separately. 
    
    knapSackSolveTimes = []
    knapSackSolveTotalTime = 0
    knapSackSolveMaxTime = 0
    knapSackSolveMinTime = 99999999999999
    optimalSolutions = []
    testCount = 0
    weightValues = []
    weight = 120
    for knap in forTesting:
        weightValues.append(weight)
        weight += 20
        

    
    idx = -1
    for knap in forTesting:
        print("Testing knapSackSolve")
        idx +=1
        testCount += 1
        #Call testing and take notes. 
        #Weight we can carry is passed as
        #print("Callign knapSackSolve with the weight", weightValues[idx])
        start = time.time()
        value = knapSackSolv(weightValues[idx], knap)
        end = time.time()
        runTime = end - start
        # file.write(f"Test result: Max value from KnapsackSolve returned for test {testCount-1} was: ")
        # file.write(str(value[0]))
        # file.write("\n")
        
        optimalSolutions.append(value)
        knapSackSolveTimes.append(runTime)
        knapSackSolveTotalTime += runTime
        if runTime >= knapSackSolveMaxTime:
            knapSackSolveMaxTime = runTime
        if runTime <= knapSackSolveMinTime:
            knapSackSolveMinTime = runTime  
    
    knapSackSolveAverage = knapSackSolveTotalTime/testCount
    ReportGenerator.generateReportKnapSackSolve(knapSackSolveTimes, knapSackSolveMinTime, knapSackSolveMaxTime
    ,knapSackSolveAverage, optimalSolutions, weightValues)
    print(f"Average time {knapSackSolveAverage}, with the results{optimalSolutions}")


    modifiedKnapSackSolveTimes = []
    modifiedKnapSackSolveTotalTime = 0
    modifiedKnapSackSolveMaxTime = 0
    modifiedKnapSackSolveMinTime = 99999999999999
    modifiedSolutions = []
    idx = -1
    for knap in forTesting:
        print("Testing modifiedGreedy")
        idx += 1
        #weightValue here refers to the budget
        #print("Calling modified Greedy knapsack with the budget of", 120)
        start = time.time()
        value = modifiedGreedyKnapsack(knap, weightValues[idx])
        end = time.time()
        runTime = end - start
        #file.write("Test result. Max value from ModifiedGreedy returned: ")
        # file.write(str(value[0]))
        # file.write("\n")
        # print("Finished modifiedGreedyKnapsack with the return value of:", value[0])
        modifiedSolutions.append(value)
        modifiedKnapSackSolveTimes.append(runTime)
        modifiedKnapSackSolveTotalTime += runTime
        if runTime >= modifiedKnapSackSolveMaxTime:
            modifiedKnapSackSolveMaxTime = runTime
        if runTime <= modifiedKnapSackSolveMinTime:
            modifiedKnapSackSolveMinTime = runTime  
    modifiedKnapSackSolveAverage = modifiedKnapSackSolveTotalTime/testCount
    ReportGenerator.generateReportModifedKnapSack(modifiedKnapSackSolveTimes, modifiedKnapSackSolveMinTime, modifiedKnapSackSolveMaxTime
    ,modifiedKnapSackSolveAverage, optimalSolutions, weightValues, modifiedSolutions)
    print(f"Average time {modifiedKnapSackSolveAverage}, with the results{modifiedSolutions}")

    maxKnapSackSolveTimes = []
    maxKnapSackSolveTotalTime = 0
    maxKnapSackSolveMaxTime = 0
    maxKnapSackSolveMinTime = 99999999999999
    maxKnapSackSolutions = []
    idx = -1
    for knap in forTesting:
        print("Testing maxKnapSack")
        idx += 1
        #Target is weigthValues
        #print("Callign solve maximumKnapsack with the target of", 120)
        start = time.time()
        value = solveMaximumKnapsack(knap,weightValues[idx])
        end = time.time()
        runTime = end - start
        maxKnapSackSolutions.append(value)
        # file.write("Test result. Max value from solveMaximumKnapsack returned: ")
        # file.write(str(value[0]))
        # file.write("\n")
        # print("Finished solveMaximumKnapsack with the return value of", value[0])
        maxKnapSackSolveTimes.append(runTime)
        maxKnapSackSolveTotalTime += runTime
        if runTime >= maxKnapSackSolveMaxTime:
            maxKnapSackSolveMaxTime = runTime
        if runTime <= maxKnapSackSolveMinTime:
            maxKnapSackSolveMinTime = runTime  
    maxKnapSackAverage = maxKnapSackSolveTotalTime/testCount
    ReportGenerator.generateReportMaxKnapSack(maxKnapSackSolveTimes, maxKnapSackSolveMinTime, maxKnapSackSolveMaxTime
    ,maxKnapSackAverage, optimalSolutions, weightValues, maxKnapSackSolutions)
    print(f"Average time {maxKnapSackAverage}, with the results{maxKnapSackSolutions}")

    approxKnapSackSolveTimes = []
    approxKnapSackSolveTotalTime = 0
    approxKnapSackSolveMaxTime = 0
    approxKnapSackSolveMinTime = 99999999999999
    approxKnapSackSolutions = []
    scaleFactors = []
    scaleFactor = 1/60
    for knap in forTesting:
        scaleFactor += 1/18
        scaleFactors.append(scaleFactor)
    idx = -1
    for knap in forTesting:
        print("Testing approximation")
        idx +=1
        start = time.time()
        value = knapSackApproxSchemce(knap, scaleFactors[idx], weightValues[idx])
        end = time.time()
        runTime = end -start
        approxKnapSackSolutions.append(value)
        approxKnapSackSolveTimes.append(runTime)
        approxKnapSackSolveTotalTime += runTime
        if runTime >= approxKnapSackSolveMaxTime:
            approxKnapSackSolveMaxTime = runTime
        if runTime <= approxKnapSackSolveMinTime:
            approxKnapSackSolveMinTime = runTime  
    approxKnapSackAverage = approxKnapSackSolveTotalTime/testCount
    ReportGenerator.generateReportKnapSackApproximation(approxKnapSackSolveTimes, approxKnapSackSolveMinTime, approxKnapSackSolveMaxTime
    ,approxKnapSackAverage, optimalSolutions, scaleFactor, approxKnapSackSolutions, weightValues)
    print(f"Average time {approxKnapSackAverage}, with the results{approxKnapSackSolutions}")

    ReportGenerator.generateRunGraph(knapSackSolveTimes, modifiedKnapSackSolveTimes, maxKnapSackSolveTimes, approxKnapSackSolveTimes)

###########  KNAPSACK ALGORITHMS   ####################

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


#######  Greedy 2 Approx MAX KNAPSACK  ###################

# """"
# def modifiedGreedyKnapsack(itemList, value, cost, B):

#     Initialize G to be the empty set
#     sort itemList in decreasing order of v(a)/c(a)
#     intialize L to B //L is the amount of money we have left.
#     for each a in itemList and while L > 0
#         if cost(a) <= L:
#             then begin
#                 add a to G
#                 Decrease L by cost(a)
#             end
#     end for
#     Let amax be the object with maximum value
#     if value(amax) > Value(G)
#         then return {amax}
#         else return G.

# """

def getRatio(item):
    return item.getRatio()
def getValue(item):
    return item.getValue()



def modifiedGreedyKnapsack(itemList, B):
    #Initialize variable to be the empty set.
    itemsTaken = []
    itemsValue = copy.deepcopy(itemList)
    itemsBasedOnRatio = copy.deepcopy(itemList)
    moneyLeft = B
    #Sort based on ratio. Calls function getRatio from this class with the item. 
    print("First item is currently", itemsBasedOnRatio[0].getRatio())
    itemsBasedOnRatio.sort(key = getRatio, reverse = True)
    print("FIrst item now is:", itemsBasedOnRatio[0].getRatio())
    #Sort based on value. Calls function getValue from this class with the item. 
    itemsValue.sort(key = getValue, reverse = True)
    # for each a in itemList and while L > 0
    #     if cost(a) <= L:
    #         then begin
    #             add a to G
    #             Decrease L by cost(a)
    #         end
    # end for
    while moneyLeft > 0:
        moneyLeftNow = moneyLeft
        for item in itemsBasedOnRatio:
            if item.getCost()  <= moneyLeft:
                itemsTaken.append(item)
                moneyLeft = moneyLeft - item.getCost()
        if moneyLeftNow == moneyLeft:
            break
        
    # Making maxA to be the max value item. 

    # Let amax be the object with maximum value
    # if value(amax) > Value(G)
    #     then return {amax}
    #     else return G.
    maximumValueObject = itemsValue[0]
    choseItemValue = 0
    for item in itemsTaken:
        choseItemValue = choseItemValue + item.getValue()
    
    if maximumValueObject.getValue() > choseItemValue:
        return maximumValueObject.getValue()
    else: 
        return choseItemValue
    
    


##########   Min version of KnapSack Solv  #########################

#This is for the MinKnapSack
# A is the item list, each item has value associated with them. 
    # cost of a item is also included.

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



#######   Fully Polynomial TIme Approximation scheme    #################


def knapSackApproxSchemce(objectList, scaleFactor, target):
    scaled = []
    maximumA = 0
    items = copy.deepcopy(objectList)
    for item in items:
        if item.getValue() >= maximumA:
            maximumA = item.getValue()
    #TODO what if I change the value in the ObjectList. then I don't have to pass a separate valueList. 
    for item in items:
        F =  (maximumA/ (len(items)-1)) * scaleFactor
        #scaled.append(math.floor((item.getValue())/F))
        item.setValue(math.floor((item.getValue())/F))
    
    
    # target = 0
    # for elm in scaled:
    #     target += target + elm
    result = solveMaximumKnapsack(items, target)
    return result



generateKnapSack()