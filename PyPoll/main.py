#import other files for calculations, file operations, and time for file naming
import time
import fileFunctions
import voteFunctions

#path to poll data assuming runing from repository home
filePath= 'PyPoll\Resources\election_data.csv'
#get data from file as per file function which assumes a 3 term per line csv and creates a dictionary with  a 2 value list for each key
votes = fileFunctions.getData(filePath)
#remove header line
del votes['Voter ID']

#coundt votes by counting the number of keys in the dictionary
voteCountT = len(votes.keys())
#does calculations with functions from file "voteFunctions.py"
voteList = voteFunctions.anonomousVotes(votes)
candidatesList = voteFunctions.candidates(voteList)
voteCountSeperated = voteFunctions.voteCount(voteList,candidatesList)
votePercentage = voteFunctions.votePercent(voteList,candidatesList)
winner = voteFunctions.winningCandidate(voteCountSeperated)


#put data into a readable format
text =(f"""
Election Results
----------------------------------------------
Total Votes: {voteCountT}
----------------------------------------------""")
for candidate in candidatesList:
    text = f'{text}\n{candidate}: {votePercentage[candidate]:.00f}% ({voteCountSeperated[candidate]})'
text = f'''{text}
----------------------------------------------'''
text = f'{text}\nWinner: {winner}\n----------------------------------------------'

#prints data to terminal
print(text)

#get date from current time and splits into stings to use for file naming
dateTime=time.asctime(time.localtime())
fileTime =  dateTime.split()
#writes the results to a file with the name of <month-day-year>Analysis.txt to a file in the Analysis folder provided in the repository
fileFunctions.writeNewFile(f'PyPoll\\Analysis\\{fileTime[1]}{fileTime[2]}{fileTime[4]}Analysis.txt',text)
