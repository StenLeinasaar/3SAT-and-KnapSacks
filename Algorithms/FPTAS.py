#FULLY Polynomial Time Appoximation
import copy
from math import floor
import math


"""

O(n3 * 1/epsilon) -- > poly time in n and 1/epsilon
PseudoCode: 

def knapSackApproxScheme(objectList, value, cost, F):
    //compute the scaled values
    for each a in objectList
        set scaled[a] = floor(v(a)/F)
    end for
    //solve using the scaled values
result = SolveMaximumKnapsack(objectList, scaled, c)


# """
# import SolveMaximumKnapsack
from Algorithms.MaxKnapSackMinVers import solveMaximumKnapsack
scaleFactor = 1/5

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



