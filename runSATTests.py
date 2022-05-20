#  @Author :  Sten Leinasaar
#  Computer Science 306 Computability and Complexity final project



from collections import Counter
import copy

import random
import time


from UTILS import GenerateProblems
from UTILS import ReportGenerator

def generate3SAT():
    forTesting = []
    for x in range(2):
        satInstance = GenerateProblems.generateTestSAT()
        #print("got a satInstance of: ", satInstance)
        #satInstance is a list of lists now. 
        #each list inside is a clause. 
        #Call tests for each. 
        forTesting.append(satInstance)
    #print(forTesting)
    testCount = 0
    clausesSatisfiedDPLL = []
    truthAssignmentDPLL = []
    maxRunTimeDPLL = 0
    minRunTimeDPLL = 10000
    runTimesDPLL = []
    totalRunTimeDPLL = 0
    for sat in forTesting:
        testCount +=1
        #DPLL returns either True or False  && TruthAssignment
        #I only allow 16 literals in total
        truthAssignment = [None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None]
        #print("The problem called with",sat)
        #print("Calling DPLL with truth assignment of", truthAssignment)
        start = time.time()
        result = DPLL(sat, truthAssignment)
        end = time.time()
        runTime = end - start
        
        totalRunTimeDPLL += runTime
        runTimesDPLL.append(runTime)
        if runTime >= maxRunTimeDPLL:
            maxRunTimeDPLL = runTime
        elif runTime <= minRunTimeDPLL:
            minRunTimeDPLL = runTime
        satis = result[0]
        print("DPLL result is", satis[0])
        print("TruthAssignment is:", result[1])
        if satis[0] == False:
            formula = copy.deepcopy(sat)
            numberOfSatisfiedClauses = howManySatsified(formula, result[1])
            #print("Satisifed clauses was: ", numberOfSatisfiedClauses)
            clausesSatisfiedDPLL.append(numberOfSatisfiedClauses)
        else:
            numberOfSatisfiedClauses = len(sat)
            clausesSatisfiedDPLL.append(numberOfSatisfiedClauses)
        truthAssignmentDPLL.append(copy.deepcopy(result[1]))
    averageRunTimeDPLL = totalRunTimeDPLL/testCount
    ReportGenerator.generateSatReport(runTimesDPLL, maxRunTimeDPLL, minRunTimeDPLL, averageRunTimeDPLL,clausesSatisfiedDPLL, truthAssignmentDPLL, True, False)

    clausesSatisfiedGSAT = []
    truthAssignmentGSAT = []
    maxRunTimeGSAT = 0
    minRunTimeGSAT = 10000
    runTimesGSAT = []
    totalRunTimeGSAT = 0
    for sat in forTesting:
        # GSAT returns either True and the truthassignment
        # Or False and how Many literals was satisfied. 
        #I only allow 16 literals in total.
        truthAssignment = [None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None]
        #print("Calling GSAT with the problem", sat)

        start = time.time()
        result = GSAT(sat, truthAssignment, 6, 10)
        end = time.time()
        runTime = end - start
        print("Result of GSAT is, ", result[0])
        #print("Clauses satisfied is,:", result[1])
        print("The truth assignment is:", result[2])
        totalRunTimeGSAT += runTime
        runTimesGSAT.append(runTime)
        if runTime >= maxRunTimeGSAT:
            maxRunTimeGSAT = runTime
        elif runTime <= minRunTimeGSAT:
            minRunTimeGSAT = runTime
        if result[0] == True:
            clausesSatisfiedGSAT.append(len(sat))
        else:
            clausesSatisfiedGSAT.append(result[1])
        truthAssignmentGSAT.append(copy.deepcopy(result[2]))
    averageRunTimeGSAT = totalRunTimeGSAT/testCount  
    ReportGenerator.generateSatReport(runTimesGSAT, maxRunTimeGSAT, minRunTimeGSAT, averageRunTimeGSAT,clausesSatisfiedGSAT, truthAssignmentGSAT, False, True)
    
    clausesSatisfiedSevenBeforeFlip = []
    clausesSatisfiedSevenAfterFlip = []
    truthAssignmentSevenBefore = []
    truthAssignmentSevenAfter = []
    maxRunTimeSeven = 0
    minRunTimeSeven = 10000
    runTimesSeven = []
    totalRunTimeSeven = 0
    for sat in forTesting: 
        #I only allow 16 literals.
        truthAssignment = [None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None]
        #print("Calling seven eight approximation")
        start = time.time()
        result = sevenEight(sat, truthAssignment)
        end = time.time()
        runTime = end - start
        print("Clauses satisfied before:", result[0])
        #print("Truth assignment before: ", result[2])
        print("Clauses satisfied after:", result[1])
        #print("Truth assignment after", result[2])
        totalRunTimeSeven += runTime
        runTimesSeven.append(runTime)
        if runTime >= maxRunTimeSeven:
            maxRunTimeSeven = runTime
        elif runTime <= minRunTimeSeven:
            minRunTimeSeven = runTime
        
        clausesSatisfiedSevenBeforeFlip.append(result[0])
        clausesSatisfiedSevenAfterFlip.append(result[1])
        truthAssignmentSevenBefore.append(copy.deepcopy(result[2]))
        truthAssignmentSevenAfter.append(copy.deepcopy(result[3]))
    averageRunTimeSeven = totalRunTimeSeven/testCount
    ReportGenerator.generateSatSevenReport(runTimesSeven,maxRunTimeSeven, minRunTimeSeven, averageRunTimeSeven,clausesSatisfiedSevenBeforeFlip, clausesSatisfiedSevenAfterFlip, truthAssignmentSevenBefore, truthAssignmentSevenAfter)
    ReportGenerator.generateSATGraphs(runTimesDPLL, runTimesGSAT, runTimesSeven)

###################   GSAT   #########################
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
            
        


# GSAT : input: a set of CL clauses, integers Maxflips, maxtires
# OUTPUT: a satisfying truth assignment of CL, if any is found
# begin: 
#     for i := 1 to maxtries do
#         T = a randomly generated truth assignment
#         for j = 1 to maxflips do
#             if T satisfies CL then return T
#             for each variable p:
#                 let Make[p] = the number of clauses currently unsatisfied by T that would become satisifed if th truth value of p were reversed. 
#                 let Break[p] = the number of clauses currently satisifed by T that would become unsatisfied if the truth value of p were flipped
#                 let diff[p] = Make[p] - Break[p]
#             end for
#             let MaxDiffList = list of variables with the greatest diff
#             p = a random member of maxDiffList
#             T = T with the truth assignment of p flipped
#         end for
#     end for
# return No satisfying assingment found.
# end

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
        print("Truth assignment is", truthValues, truthAssignment) 
        print("FOrmula,", formulaInitial)
        #truthAssignment = a randomly generated truth assignment
        idx = 0
        for literal in truthAssignment:
            rand = random.randint(0,15)
            if rand >=7:
                truthValues[idx] = True
            else:
                truthValues[idx] = False
            idx += 1
        print("Current truthAssignment", truthValues)
        clauseIndex = 0
        for clause in formulaInitial: 
            for literal in clause:
                #If literal is positive
                if literal == abs(literal):
                    print("THe value of the literal", literal)
                    print("Truth assignment of that literal is", truthValues[abs(literal)])
                    if truthValues[literal] == True:
                        trueValuesInTheClause[clauseIndex] += 1
                        #print(trueValuesInTheClause)
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


###############     DPLL    ###################


#Do I need truthAssignmentSoFar?
def DPLL(formulaSoFar, truthAssignmentSoFar):
    truthAssignment = copy.deepcopy(truthAssignmentSoFar)
    formula = formulaSoFar


    #print("Fomrula That came into DPLL", formula)
    returned = unitPropagation(formula, truthAssignment)
    #print("Returned values were,", returned[0], returned[1])
    #print("After the unit Propagation")
    newAssignment = returned[1]
    #print("Newassignment is", newAssignment)
    newFormula = returned[0]
    #print("Returned new formula is: ", newFormula)
    #
    # if newFormula is empty:
    # then return satisfiable with newAssignment as the solution 
    #if empty
    if not newFormula:
        #print( "newFormula was empty")
        return [True], newAssignment
    #Assign newFormula after checking if it is empty. 
    # if newFormula contains an empty clause:
    #     then return UNSATSIFIABLE s
    #print("New Formula was not empty. I will go through clause by clause")
    for clause in newFormula:
        if not clause:
            #print("There was an empty clause. Cannot be satisfied")
            return [False], newAssignment
        #if not empty, it continue
    # let xi be the first variable that is not assigned in newAssignment
#     """"
#     need to find a variable in new assignment that is not assigned yet.
# """
    
    #variable will count as a index here. 
    #idx = -1
    notAssignedVariable = 0
    clause = newFormula[0]
    #print("THe clause I am looking at:" , clause)
    literal = clause[0]
    #print("THe literal is", literal, newAssignment[abs(literal)])

    # if newAssignment[abs(literal)] == None:
    #     notAssignedVariable = literal
    #         #print("Variable was unassigned, the index of a notAssignedVariable is: ", notAssignedVariable)
    #         # add clause (xi) to newFormula
    #     clause = [notAssignedVariable]
    #     newFormula.insert(0,clause)
    #         # add xi = TRUE to newAssignment
    #     newAssignment[abs(notAssignedVariable)] = True
    # else:
    clauseIndex = 0
    while clauseIndex < len(newFormula):
        for literal in newFormula[clauseIndex]:
            if newAssignment[abs(literal)] == None:
                notAssignedVariable = literal
        #print("Variable was unassigned, the index of a notAssignedVariable is: ", notAssignedVariable)
        # add clause (xi) to newFormula
                clause = [notAssignedVariable]
                newFormula.insert(0,clause)
        # add xi = TRUE to newAssignment
                newAssignment[abs(notAssignedVariable)] = True 
                clauseIndex = len(newFormula) + 2
                break
        clauseIndex += 1
            
    #print("THe formula is now in DPLL after adding unassigned:", newFormula)
    # for literal in newAssignment:
    #     idx += 1 

    #     #print("variable from the newAssignment is:", variable)
    #     #if variable is aunassigned and not negated
    #     if newAssignment[idx] == None:   
    #         #In newassignment the index of a variable is this variables number in the clause
    #         notAssignedVariable = idx
    #         #print("Variable was unassigned, the index of a notAssignedVariable is: ", notAssignedVariable)
    #         # add clause (xi) to newFormula
    #         clause = [notAssignedVariable]
    #         newFormula.insert(0,clause)
    #         # add xi = TRUE to newAssignment
    #         newAssignment[notAssignedVariable] = True
    #         break

            
    unAssigned = copy.deepcopy(notAssignedVariable)
    
    # set result = DPLL(newFormula, newAssignment)
    #print("Beinnign recursion")
    result = DPLL(newFormula,newAssignment)
    #print("Finished recursion")
    newAssignment = result[1]
    #print("After the assigning non assigned variable and calling DPLL. The truth assignment is", newAssignment)
    # if result is satisfiable:
    #     then return satisfiable with newAssignment as the solution
    newFormula = result[0]
    #print("New formula after the firt DPLL call", newFormula)
    if newFormula[0] == True:
        return [True], newAssignment
    elif newFormula[0] == False:
        return [False], newAssignment
    #print("I hit the base cases and I am checking if the assignment satisifes or nah. ")
    form = copy.deepcopy(newFormula)
    if satisfies(form, newAssignment):
        return [True], newAssignment
    else:
        #print("Backtracked and flipping the variables truth assignmend. Truthassignmetn now,", unAssigned, newAssignment)
    #replace (xi) with (not xi) in newFormula
        for clause in newFormula:
            if clause.count(unAssigned) > 0:
                    #clause is a list
                index = clause.index(unAssigned)
                unAssigned = -unAssigned
                clause[index] = unAssigned
                newFormula[newFormula.index(clause)] = clause
            # replace xi = true with xi= FALSE in newAssignment
                newAssignment[abs(unAssigned)] = False
            #print("Changed the truth assignment of variable ")
    #print("Calling DPLL in the end of the DPLL. Truthassignment is now", newAssignment)
        return DPLL(newFormula, newAssignment)
        

def unitPropagation(formula, truthAssignmentSoFar):
    #index 0 is the formula to return, 
    #index 1 is the truth assignment
    toReturn = [[],[]]
    truthNow = copy.deepcopy(truthAssignmentSoFar)
    formulaToReturn = copy.deepcopy(formula)
    #if not an empty clause the while loop runs
    #print("The formula in unti propagation is currently", formulaToReturn)
    for clause in formulaToReturn:
        if not clause:
            #print("Empty clause")
            toReturn[1] = truthNow
            toReturn[0] = formulaToReturn
            return toReturn
        else:
            #Unit clause
            if len(clause) == 1:
                #print("It was a unit clause", clause)
                variable = clause[0]
                formulaToReturn.pop(formulaToReturn.index(clause))
                #print("Variable from unit clause is", variable)
                #I pop that unit clause from the formula.
                
                #print("Formula after popping a unit clause", formulaToReturn)
                #print("The variable is", variable)
                #Let xj be the variable in some unit clause
                #if xj appears positively in the unit clause:

                #It appears positively
                if variable == abs(variable):
                    #print("Vairable was positive. set it to true")
                    truthNow[variable] = True
                    for clause in formulaToReturn:
                        #If variable is in the claase
                        if clause.count(variable) > 0:
                            #print("Popped a clause with that variabe")
                        #pop clause from that formula
                            formulaToReturn.pop(formulaToReturn.index(clause))
                    #Remove not xj from every clause in the formula 
                    for clause in formulaToReturn:
                        if clause.count(-variable) > 0:
                            for literal in clause:
                                if literal == -variable:
                                    clause.pop(clause.index(literal))
                        formulaToReturn[formulaToReturn.index(clause)]=clause  
                #It appears negated
                else: 
                    truthNow[abs(variable)] = False
                    for clause in formulaToReturn:
                        #If variable is in the claase
                        if clause.count(variable) > 0:
                        #pop clause from that formula
                            formulaToReturn.pop(formulaToReturn.index(clause))
                    #Remove xj from every clause in the formula 
                    for clause in formulaToReturn:
                        if clause.count(abs(variable)) > 0:
                            for literal in clause:
                                if literal == abs(variable):
                                    clause.pop(clause.index(literal))
                        formulaToReturn[formulaToReturn.index(clause)]= clause 
        #print("THe formula is ", formulaToReturn)
    toReturn[0] = formulaToReturn
    toReturn[1] = truthNow
    #print("The propagated formula is", formulaToReturn)
    return toReturn

# """"

# unitPropagation(formula, truthAssignmentSoFar)
# while formula contains a unit clause but not an empty cluase
#     Let xj be the variable in some unti clause
#     if xj appears positively in the unit clause
#         then begin:
#             add xj = TRUE to truthAssignmentSoFar
#             remove every clause that contains xj from formula
#             remove not xj from every cluase in fomrula containing not xj
#             end
#         else begin
#             add xj = False to truthAssignmentSoFar
#             remove every clause that contains not xj from formula
#             remove xj from every clause in formula containing xj
#             end
# end while
# return truthAssignmentSoFar and formula
# """

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

###########  7/8 approximation ######################

# #Assign a random truth assignment
#Flip it. 
#Return it. 
def sevenEight(formula, truthAssignment):
    idx = -1
    satisfiedClausesBefore = 0
    satisfiedClausesAfter = 0
    truthAssignmentFlipped = copy.deepcopy(truthAssignment)

    for literal in truthAssignment:
        idx += 1
        rand = random.randint(0,10)
        if rand >=5:
            truthAssignment[idx] = True
        else:
            truthAssignment[idx] = False
    idx = -1
    for literal in truthAssignment:
        idx += 1
        if literal == True:
            truthAssignmentFlipped[idx] = False
        else:
            truthAssignmentFlipped[idx] = True

    formulaToCheck = copy.deepcopy(formula)
    satisfiedClausesBefore = howManySatsified(formulaToCheck, truthAssignment)
    formulaToCheck = copy.deepcopy(formula)
    satisfiedClausesAfter = howManySatsified(formulaToCheck, truthAssignmentFlipped)
    
    return satisfiedClausesBefore, satisfiedClausesAfter, truthAssignment, truthAssignmentFlipped


generate3SAT()





