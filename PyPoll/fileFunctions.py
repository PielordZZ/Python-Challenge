import csv
from os.path import exists

#writes data to a dictionary with first term as the key and 2 following terms as values for the key  {'line value 1', ['line value 2','line value 3']}
def getData(path): #getData(<path to csv file>)
    with open(path, newline='') as file:


        data = csv.reader(file, delimiter = ',')
        voteDict = {}

        for item in data:
            voteDict[item[0]]= [item[1], item[2]]
    return voteDict


#writes the text to a new file if it doesn't exist and checks if the user wants to overwrite data if the file alredy exists
def writeNewFile(filePath,filetext): #writeNewFile(<location and name of file>,<text to put into file>)
    #check if the file already exists to ensure it doesn't overwrite existing data
    if not exists(filePath):
        f = open(filePath, 'x')
        f.write(filetext)
        f.close()
    else:
        #prompt user if they want to overwrite the data with new text
        userInput= input('file exists overwrite with new data? (y/n)')
        if userInput == 'y':
            f = open(filePath, 'w')
            f.write(filetext)
            f.close()


