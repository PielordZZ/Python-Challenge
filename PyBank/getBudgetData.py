import csv

def getBudgetData(path):

    with open(path, newline='') as file:


        data = csv.reader(file, delimiter = ',')
        budgetDict = {}

        for item in data:
            budgetDict[item[0]]= item[1]
    return budgetDict
