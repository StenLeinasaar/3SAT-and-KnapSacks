#  @Author :  Sten Leinasaar
#  Computer Science 306 Computability and Complexity final project




#Do I need truthAssignmentSoFar?
import copy


def DPLL(formulaSoFar, truthAssignmentSoFar):
    truthAssignment = copy.deepcopy(truthAssignmentSoFar)
    formula = copy.deepcopy(formulaSoFar)


    #print("Fomrula That came into DPLL", formula)
    returned = unitPropagation(formula, truthAssignment)
    #print("Returned values were,", returned[0], returned[1])
    #print("After the unit Propagation")
    newAssignment = returned[1]
    newFormula = returned[0]
    #print("Returned newFormula is", newFormula)
    #print("Returned new Assignment is: ", newAssignment)
    #
    # if newFormula is empty:
    # then return satisfiable with newAssignment as the solution 
    #if empty
    if not newFormula:
        #print( "newFormula was empty")
        return True, newAssignment
    #Assign newFormula after checking if it is empty. 
    # if newFormula contains an empty clause:
    #     then return UNSATSIFIABLE s
    #print("New Formula was not empty. I will go through clause by clause")
    for clause in newFormula:
        if not clause:
            #print("There was an empty clause. Cannot be satisfied")
            return False, newAssignment
        #if not empty, it continue
    # let xi be the first variable that is not assigned in newAssignment
#     """"
#     need to find a variable in new assignment that is not assigned yet.
# """
    
    #variable will count as a index here. 
    idx = -1
    notAssignedVariable = 0
    for variable in newAssignment:
        
        idx += 1
        #print("variable from the newAssignment is:", variable)
        #if variable is aunassigned and not negated
        if variable == None:
            #In newassignment the index of a variable is this variables number in the clause
            notAssignedVariable = idx
            #print("Variable was unassigned, the index of a notAssignedVariable is: ", notAssignedVariable)
            # add clause (xi) to newFormula
            clause = [notAssignedVariable]
            newFormula.insert(0,clause)
            # add xi = TRUE to newAssignment
            newAssignment[notAssignedVariable] = True
            break
    
    unAssigned = copy.deepcopy(notAssignedVariable)
    
    # set result = DPLL(newFormula, newAssignment)
    result = DPLL(newFormula,newAssignment)
    
    
    
    newAssignment = result[1]
    #print("After the assigning non assigned variable and calling DPLL. The truth assignment is", newAssignment)
    # if result is satisfiable:
    #     then return satisfiable with newAssignment as the solution
    newFormula = result[0]


    if newFormula == True:
        #print("It was satisfiable. Returning True")
        return True, newAssignment
    # elif newFormula == False:
    #     #print("It was not satisfiable. Returning False")
    #     return False, newAssignment
    #print("There is still work to do")
    #print("THe value at newFOrmula[0] is",newFormula[0])
    if not newFormula:
        #print("if not newFormula was true", newFormula)
        return True, newAssignment

    #     else begin:
    for clause in newFormula:
        if not clause: 
            return False, newAssignment
    
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
    return DPLL(newFormula, newAssignment)

""""

DPLL( formulaSoFar, TruthAssignmentSoFar):
    call unitpropagation(formula, truthAssignmentSoFar)
    set newFormula to the formua returned
    set newassignment to the turthassignemnt returned
    if newFormula is empty:
        then return satisfiable with newAssignment as the solution 
    if newFormula contains an empty clause:
        then return UNSATSIFIABLE
    let xi be the first variable that is not assigned in newAssignment
    add clause (xi) to newFormula
    add xi = TRUE to newAssignment
    set result = DPLL(newFormula, newAssignment)
    if result is satisfiable:
        then return satisfiable with newAssignment as the solution
        else begin:
            replace (xi) with (not xi) in newFormula
            replace xi = true with xi= FALSE in newAssignment
            return DPLL(newFormula, newAssignment)
        end

"""


        

def unitPropagation(formula, truthAssignmentSoFar):
    #index 0 is the formula to return, 
    #index 1 is the truth assignment
    toReturn = [[],[]]
    truthNow = copy.deepcopy(truthAssignmentSoFar)
    formulaToReturn = copy.deepcopy(formula)
    #if not an empty clause the while loop runs
    #print("The formula is currently", formulaToReturn)
    for clause in formulaToReturn:
        if not clause:
            toReturn[1] = truthNow
            toReturn[0] = formulaToReturn
            return toReturn
        else:
            #Unit clause
            if len(clause) == 1:
                #print("It was a unit clause", clause)
                variable = clause.pop()
                #I pop that unit clause from the formula.
                formulaToReturn.pop(formulaToReturn.index(clause))
                #print("Formula after popping the unit clause", formulaToReturn)
                #print("The variable is", variable)
                #Let xj be the variable in some unit clause
                #if xj appears positively in the unit clause:
                if variable == abs(variable):
                    truthNow[variable] = True
                else:
                    #Else the variable is negated
                    truthNow[abs(variable)] = False

    #remove every clause in formula containing variable assigned to true
    idx = -1
    for variable in truthNow:
        idx += 1
        if variable == True:
            #If variable is true, check for each clause and if they have this variable.  
            for clause in formulaToReturn:
                #If variable is in the cluase
                if clause.count(idx) > 0:
                    #pop clause from that formula
                    formulaToReturn.pop(formulaToReturn.index(clause))

            #remove negatedxj from every clause in formula containing negated xj
            for clause in formulaToReturn:
                #If negated variable is in the clause
                if clause.count(-idx) > 0:
                    #Index of that -variable is the poppoing place.
                    for literal in clause:
                        if literal == -idx: 
                            clause.pop(clause.index(literal))
                    formulaToReturn[formulaToReturn.index(clause)]=clause
        #Else the variable without negation is false.
        elif variable == False:
            #Remove every clause that contains negated xj from formula. Because that would be true
            for clause in formulaToReturn:
                #If clause has this negated variable. Remove it
                if clause.count(-idx) > 0:
                    #pop that clause
                    #print("Removing a clause with that variable from the formula")
                    formulaToReturn.pop(formulaToReturn.index(clause))
            #remove xj from every clause in formula containing xj
            for clause in formulaToReturn:
                if clause.count(idx) > 0:
                    for literal in clause:
                        if literal == idx:          
                            clause.pop(clause.index(literal))
                    #formulaToReturn.insert(formulaToReturn.index(clause), clause)
                    formulaToReturn[formulaToReturn.index(clause)] = clause
    toReturn[0] = formulaToReturn
    toReturn[1] = truthNow
    return toReturn

""""

unitPropagation(formula, truthAssignmentSoFar)
while formula contains a unit clause but not an empty cluase
    Let xj be the variable in some unit clause
    if xj appears positively in the unit clause
        then begin:
            add xj = TRUE to truthAssignmentSoFar
            remove every clause that containsxj from formula
            remove not xj from every cluase in fomrula containing not xj
            end
        else begin
            add xj = False to truthAssignmentSoFar
            remove every clause that contains not xj from formula
            remove xj from every clause in formula containing xj
            end
end while
return truthAssignmentSoFar and formula
"""