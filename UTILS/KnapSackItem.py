#This class defined a knapSack item. 
#KnapSack item has a value and a cost. 
# """"
# KnapSackItems.py is a class with a goal to define the item object used in knapSack problems. 

# There are two attributes for the knapSack item:

#     knapsack item has a value
#     knapSack item has a cost
#     knapSack item will also have a ratio that is value/cost
    
# """
class KnapSackItem:

    def __init__(self, value, cost):
        self.value = value
        self.cost = cost
        self.ratio = round(value/cost,3)

    def getValue(self):
        return self.value

    def changeValue(self, newValue):
        self.value = newValue

    def getCost(self):
        return self.cost

    def getRatio(self):
        return self.ratio
    def setValue(self, value):
        self.ratio = round(value/self.cost, 3)







