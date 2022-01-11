from getBudgetData import getBudgetData


import getBudgetData
import calculations
import time
import writeAnalysis
path = 'Resources\\budget_data.csv'

budget = getBudgetData.getBudgetData(path)


#convert data into dictionary for reference in future




#make lists of data for months and profits
months = []
for item in budget.keys():
    months.append(item[0])


netProfits = []
for item in budget.values():
    if str(item).isnumeric():
        netProfits.append(int(item))

durration= calculations.timeframe(months)

TotalProfit = calculations.netProfit(netProfits)
changes = calculations.changes(netProfits)
avgProf = calculations.averageProfit(changes)

maxIncrease = calculations.greatestProfit(changes,months)
maxDecrease = calculations.greatestLoss(changes,months)

Analysis =f"""
Financial Analysis
--------------------------------------
Total Months: {durration}
Total: ${TotalProfit}
Average Change: ${avgProf:.2f}
Greatest Increase in Profits: {maxIncrease[0]} (${maxIncrease[1]:.2f})
Greatest Decrease in Profits: {maxDecrease[0]} (${maxDecrease[1]:.2f})
"""

print(Analysis)
dateTime=time.asctime(time.localtime())
print(dateTime)
fileTime =  dateTime.split()
print(fileTime)
writeAnalysis.writeNewFile(f'Analysis\\{fileTime[1]}{fileTime[2]}{fileTime[4]}Analysis.txt',Analysis)
