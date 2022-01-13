import time
import fileFunctions
import voteFunctions

filePath= 'PyPoll\Resources\election_data.csv'
votes = fileFunctions.getData(filePath)
del votes['Voter ID']
voteCountT = len(votes)
voteList = voteFunctions.anonomousVotes(votes)
candidatesList = voteFunctions.candidates(voteList)
voteCountSeperated = voteFunctions.voteCount(voteList,candidatesList)
votePercentage = voteFunctions.votePercent(voteList,candidatesList)
winner = voteFunctions.winningCandidate(voteCountSeperated)
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
print(text)

dateTime=time.asctime(time.localtime())
fileTime =  dateTime.split()
fileFunctions.writeNewFile(f'PyPoll\\Analysis\\{fileTime[1]}{fileTime[2]}{fileTime[4]}Analysis.txt',text)
