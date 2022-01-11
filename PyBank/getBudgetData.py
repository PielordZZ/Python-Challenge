import csv

def getBudgetData(path):

    with open(path, newline='') as file:


        data = csv.reader(file, delimiter = ',')
    return data
