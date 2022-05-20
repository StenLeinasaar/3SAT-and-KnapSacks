

#Assign a random truth assignment
#Flip it. 
#Return it. 

###########  7/8 approximation ######################

# #Assign a random truth assignment
#Flip it. 
#Return it. 
import copy
import random


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


