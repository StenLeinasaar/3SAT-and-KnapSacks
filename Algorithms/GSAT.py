

""""
GSAT : input: a set of CL clauses, integers Maxflips, maxtires
OUTPUT: a satisfying truth assignment of CL, if any is found
begin: 
    for i := 1 to maxtries do
        T = a randomly generated truth assignment
        for j = 1 to maxflips do
            if T satisfies CL then return T
            for each variable p:
                let Make[p] = the number of clauses currently unsatisfied by T that would become satisifed if th truth value of p were reversed. 
                let Break[p] = the number of clauses currently satisifed by T that would become unsatisfied if the truth value of p were flipped
                let diff[p] = Make[p] - Break[p]
            end for
            let MaxDiffList = list of variables with the greatest diff
            p = a random member of maxDiffList
            T = T with the truth assignment of p flipped
        end for
    end for
return No satisfying assingment found.
end

"""

import copy
import random


def GSAT(formulaInitial, truthAssignment, maxFlips, maxTries):
    #print("This is the formula", formulaInitial)
    wouldBeSatisfied = []
    wouldNotBeSatisfied = []
    difference = []
    satisfied = []
    trueValuesInTheClause = []
    truthValues = copy.deepcopy(truthAssignment)
    #Length of the formula. So each clause can be included. 
    for i in range(0, len(formulaInitial)):
        satisfied.append(False)
        trueValuesInTheClause.append(0)
    #these are depending of the variables.
    for j in range(0, len(truthAssignment)):
        difference.append(0)
        wouldBeSatisfied.append(0)
        wouldNotBeSatisfied.append(0)

    #for i := 1 to maxtries do
    maxT = maxTries
    while maxT > 0:
        #Initilize beginning of each trie. 
        for i in range(0, len(formulaInitial)):
            satisfied[i] = False
            trueValuesInTheClause[i] = 0
        for j in range(0, len(truthAssignment)):
            difference[j] = 0
            wouldBeSatisfied[j] = 0
            wouldNotBeSatisfied[j] = 0
            truthValues[j] = None
        #truthAssignment = a randomly generated truth assignment
        idx = 0
        for literal in truthAssignment:
            rand = random.randint(0,15)
            if rand >=7:
                truthValues[idx] = True
            else:
                truthValues[idx] = False
            idx += 1
        #print("Current truthAssignment", truthValues)
        clauseIndex = 0
        for clause in formulaInitial: 
            for literal in clause:
                #If literal is positive
                if literal == abs(literal):
                # print("THe value of the literal", literal)
                # print("Truth assignment of that literal is", truthAssignment[abs(literal)])
                    if truthValues[literal] == True:
                        trueValuesInTheClause[clauseIndex] += 1
                    # print(trueValuesInTheClause
                #It was negated
                else:
                    if truthValues[abs(literal)] == False:
                        trueValuesInTheClause[clauseIndex] += 1
                    

            if trueValuesInTheClause[clauseIndex] > 0:
                satisfied[clauseIndex] = True
            else:
                satisfied[clauseIndex] = False
            clauseIndex += 1

        # MAX FLIP COUNTER BEGINS HERE.        
        # for j = 1 to maxflips do
        for j in range( 1, maxFlips):
            formulaToCheckAgainst = copy.deepcopy(formulaInitial)
                
            #     if T satisfies CL then return T
            #print("THe formula i am passing to verify if satisfies", formulaToCheckAgainst)
            if satisfies(formulaToCheckAgainst, truthValues):
                return True, 100, truthValues
            formulaToCount = copy.deepcopy(formulaInitial)
            numberSatisfied = howManySatsified(formulaToCount, truthValues)
            bestTruth = copy.deepcopy(truthValues)
            #     for each variable p:
            #         let wouldBeSatisfied[p] = the number of clauses currently unsatisfied by T that would become satisifed if th truth value of p were reversed. 
            #         let wouldNotBeSatisfied[p] = the number of clauses currently satisifed by T that would become unsatisfied if the truth value of p were flipped
            #         let diff[p] = Make[p] - Break[p]
            #     end for
            #print("THe formula I am handling in this file after passing", formulaInitial)
            #print("Formula I passed to the method", formulaToCheckAgainst)
            idx = -1
            for variable in truthValues:
                idx += 1
                if variable == True:
                #let wouldBeSatisfied[idx] = the number of clauses currently unsatisfied by T that would become satisifed if th truth value of p were reversed.
                    for clause in formulaInitial:
                        if clause.count(idx) > 0:
                            if trueValuesInTheClause[formulaInitial.index(clause)] == 1 and satisfied[formulaInitial.index(clause)] ==  True:
                                #That counrs how many clauses would not be satisfied if I flip it
                                wouldNotBeSatisfied[idx] += 1
                            #Else it has to be more than 1 and changing it wouldn't matter
                            else:
                                wouldBeSatisfied[idx] +=1  
                    #let wouldNotBeSatisfied[idx] = the number of clauses currently satisifed by T that would become unsatisfied if the truth value of p were flipped
                    #let difference[idx] = wouldBeSatisfied[idx] - wouldNotBeSatisfied[idx]               
                #Check for negated variables.
                #because it was False so negated ones are true. 
                else:
                    for clause in formulaInitial:
                        if clause.count(-idx) > 0:
                            if trueValuesInTheClause[formulaInitial.index(clause)] == 1 and satisfied[formulaInitial.index(clause)] ==  True:
                                wouldNotBeSatisfied[idx] += 1
                            else:
                                wouldBeSatisfied[idx] +=1
                difference[idx] = wouldBeSatisfied[idx] - wouldNotBeSatisfied[idx]
            #     let MaxDiffList = list of variables with the greatest diff
            idx = -1
            maxDiff = 0
            for x in difference:
                idx += 1
                if x >= maxDiff:
                    maxDiff = x
                    

            #     p = a random member of maxDiffList
            p = difference.index(maxDiff)
            if truthValues[p] == False:
                truthValues[p] = True
            else:
                truthValues[p] = False

            formulaToCount = copy.deepcopy(formulaInitial)
            result = howManySatsified(formulaToCount, truthValues)
            if numberSatisfied <= result:
                numberSatisfied = result
                bestTruth = copy.deepcopy(truthValues)
                
        maxT -= 1
        #T = T with the truth assignment of p flipped
        # end for
    #RETURN Satisfying truth assignment if there is any. 
    formulaToCheckAgainst = copy.deepcopy(formulaInitial)
    formulaToCount = copy.deepcopy(formulaInitial)
    #print("The formula I pass", formulaToCheckAgainst)
    if satisfies(formulaToCheckAgainst, truthValues):
        return True,100, truthValues
    else:
        resultFinal = howManySatsified(formulaToCount, truthValues)
        if numberSatisfied <= resultFinal:
            bestTruth = copy.deepcopy(truthValues)
            return False, resultFinal, bestTruth
        else:
            return False, numberSatisfied, bestTruth


def satisfies(formula, truthAssignment):
    idx = -1
    for truthValue in truthAssignment:
        idx += 1
        for clause in formula:
            if truthValue == True:
                #print("Popping every clause that has this true variable")
                for clause in formula:
                    if clause.count(idx) > 0:
                        formula.pop(formula.index(clause))
            elif truthValue == False:
                #print("Popping every clause with the negated variable")
                for clause in formula:
                    if clause.count(-idx) > 0:
                        formula.pop(formula.index(clause))
        if not formula: 
            return True
    if not formula:
        return True
    else:
        return False

def howManySatsified(satForm, truthAssignment):
    satisfied = 0
    idx = -1
    for truthValue in truthAssignment:
        idx += 1
        for clause in satForm:
            if truthValue == True:
                #print("Popping every clause that has this true variable")
                for clause in satForm:
                    if clause.count(idx) > 0:
                        satisfied += 1
                        satForm.pop(satForm.index(clause))
            elif truthValue == False:
                #print("Popping every clause with the negated variable")
                for clause in satForm:
                    if clause.count(-idx) > 0:
                        satisfied += 1
                        satForm.pop(satForm.index(clause))
        if not satForm: 
            break
    return satisfied