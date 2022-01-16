import csv


#imports the csv from the path provided in dictionary form assuming there are only 2 values per line
def getBudgetData(path):#getBudgetData(<path to file>)

    with open(path, newline='') as file:

        data = csv.reader(file, delimiter = ',')
        budgetDict = {}

        for item in data:
            budgetDict[item[0]]= item[1]
    return budgetDict

from os.path import exists

#writes the text to a new file if it doesn't exist and checks if the user wants to overwrite data if the file alredy exists
def writeNewFile(filePath,filetext):#(<location and name of file>,<text to put into file>)
    if not exists(filePath):
        f = open(filePath, 'w')
        f.write(filetext)
        f.close()
    else:
        userInput= input('file exists overwrite with new data? (y/n)')
        if userInput == 'y':
            f = open(filePath, 'w')
            f.write(filetext)
            f.close()


