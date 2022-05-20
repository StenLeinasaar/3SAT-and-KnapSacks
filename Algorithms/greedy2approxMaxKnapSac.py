""""
def modifiedGreedyKnapsack(itemList, value, cost, B):

    Initialize G to be the empty set
    sort itemList in decreasing order of v(a)/c(a)
    intialize L to B //L is the amount of money we have left.
    for each a in itemList and while L > 0
        if cost(a) <= L:
            then begin
                add a to G
                Decrease L by cost(a)
            end
    end for
    Let amax be the object with maximum value
    if value(amax) > Value(G)
        then return {amax}
        else return G.

"""
#B is the budget. 

import copy
from KnapSackItem import KnapSackItem


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
    

