#If random number is bigger than 5, then negated, 
#else it is not negated. 

from contextlib import nullcontext
import random

#There will be 10 literals.
""""
this method produces a instance og 3SAT.It returns it and prints it to the file. 
""" 
def generateTestSAT():
    instance = []
    for x in range(10):
        literal = random.randint(0,15)
        if(random.randint(0,11) <= 5):
            #Positive
            literal = literal
        else:
            literal = -literal

        literalSecond = random.randint(0,15)
        while True:
            if literalSecond == abs(literal):
                literalSecond = random.randint(0,15)
            else:
                break
        
        if(random.randint(0,11) <= 5):
            #Positive
            literalSecond = literalSecond
        else:
            literalSecond = -literalSecond

        literalThird = random.randint(0,15)
        while True:
            if literalThird == abs(literal) or literalThird == abs(literalSecond):
                literalThird = random.randint(0,15)
            else:
                break

        if(random.randint(0,11) <= 5):
            #Positive
            literalThird = literalThird
        else:
            literalThird = -literalThird
        
        toAdd = [literal, literalSecond, literalThird]
        instance.append(toAdd)
    # print(instance)
    printSATToFile(instance)
    return instance

""""
    will return a list of tuples. Each tuple will store a value and a cost. 
    Then prints it to the file to store. 
"""  
def generateKnapSack():
    
    instance = []
    for x in range(501):
    #Items value will be between 1 and 100
        value = random.randint(1, 100)
        #Item's cost will be between 1 and 75.
        cost = random.randint(1, 75)
        item = (value, cost)
        instance.append(item)
    printKnapsackToFIle(instance)

    return instance



def printSATToFile(instance):     
    f = open("SATtestInstances.txt", "a")
    f.write(str(instance) + ";")
    f.close()
    
def printKnapsackToFIle(instance):
    f = open("knapSackInstances.txt", "a")
    f.write(str(instance) + ";")
    f.close()




# if __name__ == "__main__":
#     for x in range(101):
#         generateTestSAT()
    