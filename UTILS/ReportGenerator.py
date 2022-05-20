import os
import statistics

from matplotlib import pyplot as plt



def generateReportKnapSackSolve(listSolveTimes, solveMinTime, solveMaxTime, solveAverage, optimalResults, weightValues):
    medianRunTime = round(statistics.median(listSolveTimes),3)
    solveMinTime = round(solveMinTime, 3)
    solveMaxTime = round(solveMaxTime, 3)
    solveAverage = round(solveAverage, 3)
    file = open("knapSackSolveReport.txt", "a")
    file.write(f"The median runtime of Dynamic Programming knapsack algorithm was {medianRunTime} seconds. \n")
    file.write(f"The maximum runtime of the algorithm: {solveMaxTime} seconds. \n The minimum runtime: {solveMinTime} seconds. \n")
    file.write(f"The average runtime of the algorithm: {solveAverage} seconds. \n")
    file.write("Here are all the optimal solutions: \n")

    idx = -1
    for optimal in optimalResults:
        idx += 1
        file.write(f"The optimal solution for a test {idx} was {optimal} with the weight {weightValues[idx]}.\n")
    file.write("############################### \n \n")
    file.close()
    # x axis values
    value = []
    for i in range(0, len(listSolveTimes)):
        value.append(i)
    x = None
    y = None
    x = value
    # corresponding y axis values
    y = listSolveTimes
    
    plt.figure()
    # plotting the points
    plt.plot(x, y, markerfacecolor='blue', markersize = 10)
    
    # naming the x axis
    plt.xlabel('Number of a test')
    # naming the y axis
    plt.ylabel('Runtime of the algorithm.')
    
    # giving a title to my graph
    plt.title('DP algorithm for KnapSack!')
    # function to show the plot
    plt.savefig("knapSackDP.jpg")

def generateReportMaxKnapSack(listSolveTimes, solveMinTime, solveMaxTime, solveAverage, optimalResults, weightValues, maxKnapSolutions):
    medianRunTime = round(statistics.median(listSolveTimes),3)
    solveMinTime = round(solveMinTime, 3)
    solveMaxTime = round(solveMaxTime, 3)
    solveAverage = round(solveAverage, 3)
    file = open("knapSackSolveReport.txt", "a")
    
    file.write(f"The median runtime of Max knapsack algorithm was {medianRunTime} seconds. \n")
    file.write(f"The maximum runtime of the algorithm was {solveMaxTime} seconds and the minimum was {solveMinTime} seconds. \n")
    file.write(f"The average runtime of the algorithm was {solveAverage} seconds. \n")
    file.write("Here are all the optimal solutions: \n")

    idx = -1
    for optimal in optimalResults:
        idx += 1
        file.write(f" For instance {idx} Optimal solution: {optimal} \t Actually was: {maxKnapSolutions[idx]} with the weight {weightValues[idx]} \n")
        # file.write(f"The optimal solution for a test {idx} was {optimal} with the weight {weightValues[idx]}.\n")
        # file.write(f"The result from maxKnap for a test {idx} was {maxKnapSolutions[idx]} with the weight {weightValues[idx]}\n")
    file.write("############################### \n \n")
    file.close()

    # x axis values
    value = []
    for i in range(0, len(listSolveTimes)):
        value.append(i)
    x = None
    y = None 
    x = value
    # corresponding y axis values
    y = listSolveTimes
    
    plt.figure()
    # plotting the points
    plt.plot(x, y, markerfacecolor='blue', markersize = 10)
    
    # naming the x axis
    plt.xlabel('Number of a test')
    # naming the y axis
    plt.ylabel('Runtime of the algorithm.')
    
    # giving a title to my graph
    plt.title('Max KnapSack algorithm!')
    
    # function to show the plot
    plt.savefig("knapSackMax.jpg")

def generateReportModifedKnapSack(listSolveTimes, solveMinTime, solveMaxTime, solveAverage, optimalResults, weightValues, modifiedSolutions):
    medianRunTime = round(statistics.median(listSolveTimes),3)
    solveMinTime = round(solveMinTime, 3)
    solveMaxTime = round(solveMaxTime, 3)
    solveAverage = round(solveAverage, 3)
    file = open("knapSackSolveReport.txt", "a")
    file.write(f"The median runtime of ModifiedGreedy knapsack algorithm was {medianRunTime} seconds. \n")
    file.write(f"The maximum runtime of the algorithm was {solveMaxTime} seconds and the minimum was {solveMinTime} seconds. \n")
    file.write(f"The average runtime of the algorithm was {solveAverage} seconds. \n")
    file.write("Here are all the optimal solutions: \n")

    idx = -1
    for optimal in optimalResults:
        idx += 1
        file.write(f" For instance {idx}  Optimal solution: {optimal} \t Actually was: {modifiedSolutions[idx]} with the weight {weightValues[idx]}\n")

    file.write("############################### \n \n")   
        #file.write(f"The optimal solution for a test {idx} was {optimal} with the weight {weightValues[idx]}.\n")
    file.close()
    # x axis values
    value = []
    for i in range(0, len(listSolveTimes)):
        value.append(i)
    x = None
    y = None
    x = value
    # corresponding y axis values
    y = listSolveTimes
    
    # plotting the points
    plt.figure()
    plt.plot(x, y, markerfacecolor='blue', markersize = 10)
    
    # naming the x axis
    plt.xlabel('Number of a test')
    # naming the y axis
    plt.ylabel('Runtime of the algorithm.')
    
    # giving a title to my graph
    plt.title('Modified Greedy algorithm for KnapSack!')
    # function to show the plot
    plt.savefig("ModifiedGreedy.jpg")


def generateReportKnapSackApproximation(listSolveTimes, solveMinTime, solveMaxTime, solveAverage, optimalResults, scaleFactor, approxSolutions, weightValues):
    medianRunTime = round(statistics.median(listSolveTimes),3)
    solveMinTime = round(solveMinTime, 3)
    solveMaxTime = round(solveMaxTime, 3)
    solveAverage = round(solveAverage, 3)
    print("")
    file = open("knapSackSolveReport.txt", "a")
    file.write(f"The median runtime of Approximation knapsack algorithm was {medianRunTime} seconds. \n")
    file.write(f"The maximum runtime of the algorithm was {solveMaxTime} seconds and the minimum was {solveMinTime} seconds. \n")
    file.write(f"The average runtime of the algorithm was {solveAverage} seconds. \n")
    file.write("Here are all the optimal solutions: \n")
    idx = -1
    for optimal in optimalResults:
        idx += 1
        file.write(f" For instance {idx} . Optimal solution: {optimal} Actually was: {approxSolutions[idx]} with the weight {weightValues[idx]}\n ")
        #file.write(f"The optimal solution for a test {idx} was {optimal}.\n")
    file.write("############################### \n \n")
    file.close()
    # x axis values
    value = []
    for i in range(0, len(listSolveTimes)):
        value.append(i)


    x = value
    # corresponding y axis values
    y = listSolveTimes
    
    # plotting the points
    plt.figure()
    plt.plot(x, y, markerfacecolor='blue', markersize = 10)
    
    # naming the x axis
    plt.xlabel('Number of a test')
    # naming the y axis
    plt.ylabel('Runtime of the algorithm.')
    
    # giving a title to my graph
    plt.title('Approximation algorithm for KnapSack!')
    
    # function to show the plot
    plt.savefig("approximation.jpg")

def generateRunGraph(knapRunTimes, modifiedRunTimes, maxRuntimes, approxRuntimes):
    value = []
    for i in range(0, len(knapRunTimes)):
        value.append(i)
    # naming the x axis
    plt.xlabel('Number of a test')
    # naming the y axis
    plt.ylabel('Runtime of the algorithm.')
    

    

    x = value
    y = knapRunTimes
    
    plt.plot(x, y, markerfacecolor='blue', markersize = 10, label = "KnapSack Solve")

    y = maxRuntimes
    plt.plot(x, y, markerfacecolor='red', markersize = 10 , label = "Max KnapSack")

    y = modifiedRunTimes
    plt.plot(x, y, markerfacecolor='green', markersize = 10, label = "Modified Greedy")

    y = approxRuntimes
    plt.plot(x, y, markerfacecolor='orange', markersize = 10, label = "FPTAS")

    leg = plt.legend()
    # giving a title to my graph
    plt.title('Runtime of all algorithms')
    
    # function to show the plot
    plt.savefig("allRuntimes.jpg")

def generateSATGraphs(runTimesDPLL, runTimesGSAT, runTimesSeven):
    value = []
    for i in range(0, len(runTimesDPLL)):
        value.append(i)
    # naming the x axis
    plt.xlabel('Number of a test')
    # naming the y axis
    plt.ylabel('Runtime of the algorithm.')
    

    

    x = value
    y = runTimesDPLL
    
    plt.plot(x, y, markerfacecolor='blue', markersize = 10, label = "DPLL")

    y = runTimesGSAT
    plt.plot(x, y, markerfacecolor='red', markersize = 10 , label = "GSAT")

    y = runTimesSeven
    plt.plot(x, y, markerfacecolor='green', markersize = 10, label = "7/8 approx")


    leg = plt.legend()
    # giving a title to my graph
    plt.title('Runtime of all algorithms')
    
    # function to show the plot
    plt.savefig("allRuntimesSAT.jpg")
    

def generateSatReport(runTimes,maxRunTime, minRunTime,averageRunTime, clausesSatisfied,truthAssignment, DPLL, GSAT):
    if DPLL == True:
        file = open("dpllReport.txt", "a")
        file.write("DPLL test results\n")
    elif GSAT == True:
        file = open("gsatReport.txt", "a")
        file.write("GSAT results\n")
    
    medianRunTime = round(statistics.median(runTimes),3)
    minTime = round(minRunTime, 3)
    maxTime = round(maxRunTime, 3)
    average = round(averageRunTime, 3)
    file.write(f"The median runTime was {medianRunTime} seconds. \n The minimum time was {minTime} seconds. \n The max time was {maxTime} seconds. \n On average it took {average} seconds per instance \n")

    idx = 0
    while idx < len(runTimes):
        
        file.write(f"For test {idx}. The clauses satisfied were {clausesSatisfied[idx]}\n")
        file.write(f"Runtime was {runTimes[idx]}\n")
        file.write(f"The Truth assignment {truthAssignment[idx]} \n")
        idx += 1
    file.close()

    # x axis values
    value = []
    for i in range(0, len(runTimes)):
        value.append(i)


    x = value
    # corresponding y axis values
    y = runTimes
    
    # plotting the points
    plt.figure()
    plt.plot(x, y, markerfacecolor='blue', markersize = 10)
    
    # naming the x axis
    plt.xlabel('Number of a test')
    # naming the y axis


    plt.ylabel('Runtime of thealgorithm.')
    
    if DPLL == True:

    # giving a title to my graph
        plt.title('Runtime of the DPLL algorithm')
    else:
        plt.title("RUntime of GSAT algorithm")
    
    # function to show the plot

    if DPLL == True:

        plt.savefig("dpllalg.jpg")
    else: 
        plt.savefig("gsatalg.jpg")

def generateSatSevenReport(runTimes,maxRunTime, minRunTime, averageRunTime,clausesSatisfiedBefore, clausesSatisfiedAfter, truthAssignmentBefore, truthAssignmentAfter):
    file = open("sevenSatReport.txt", "a")
    file.write("Seven eight approximation. \n")
    medianRunTime = round(statistics.median(runTimes),3)
    minTime = round(minRunTime, 3)
    maxTime = round(maxRunTime, 3)
    average = round(averageRunTime, 3)
    file.write(f"The median runTime was {medianRunTime} seconds. \n The minimum time was {minTime} seconds. \n The max time was {maxTime} seconds. \n On average it took {average} seconds per instance\n")

    idx = 0
    while idx < len(runTimes):
        
        file.write(f"For test {idx}. The clauses satisfied before flip were {clausesSatisfiedBefore[idx]} and after {clausesSatisfiedAfter[idx]}\n")
        file.write(f"Runtime was {runTimes[idx]}\n")
        file.write(f"The Truth assignment before {truthAssignmentBefore[idx]} and after {truthAssignmentAfter[idx]} \n")
        idx += 1
    file.close()

    # x axis values
    value = []
    for i in range(0, len(runTimes)):
        value.append(i)


    x = value
    # corresponding y axis values
    y = runTimes
    
    # plotting the points
    plt.figure()
    plt.plot(x, y, markerfacecolor='blue', markersize = 10)
    
    # naming the x axis
    plt.xlabel('Number of a test')
    # naming the y axis
    plt.ylabel('Runtime of the algorithm.')
    
    # giving a title to my graph
    plt.title('7/8 th Approximation algorithm for SAT!')
    
    # function to show the plot
    plt.savefig("sevenEight.jpg")
        
