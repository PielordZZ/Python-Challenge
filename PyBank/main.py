#get finctions from other files and time for creating file names.
import fileFunctions
import bankCalculations
import time

#path to data assuming you are running from the repository base level
path = 'PyBank\\Resources\\budget_data.csv'

# get the budget data as a dictionary of dates with profit/loss for the day as values
budget = fileFunctions.getBudgetData(path)



#make lists of data for months based on keys from the dictionary
months = []
for item in budget.keys():
    months.append(item)

print(months)
#make a list of data where it takes the values of the dictionary as the profit/loss for the corresponding day in the months list.  it gives a value of 0 if the value is not a number.
profits = bankCalculations.getProfits(budget.values())


#uses funcion in calculation to tell how many months of data are in the dataset
durration= bankCalculations.timeframe(months)


#uses funciton in calculation file
TotalProfit = bankCalculations.netProfit(profits)  #bankCalculations.netProfit(<monthly profit list>) returns sum of all profits/losses
changes = bankCalculations.changes(profits)  #calculation.changes(<monthly profit list>) returns list of changes between the profit between one month to the next 
avgProf = bankCalculations.averageProfit(changes) #calculation.averageProfit(<list from bankCalculations.changes()/month to month profit changes>) returns the average of the change between months

maxIncrease = bankCalculations.greatestGain(changes,months) #calculations.greatestGain(<list of change in profit b>,<corresponding list of months to the changes>)  finds the month that profit increased most from previous month  
maxDecrease = bankCalculations.greatestLoss(changes,months)#calculations.greatestLoss(<list of change in profit b>,<corresponding list of months to the changes>)  finds the month that profit decreased most from previous month

#create a readable message with statistics calculated in this program
Analysis =f"""
Financial Analysis
--------------------------------------
Total Months: {durration}
Total: ${TotalProfit}
Average Change: ${avgProf:.2f}
Greatest Increase in Profits: {maxIncrease[0]} (${maxIncrease[1]:.2f})
Greatest Decrease in Profits: {maxDecrease[0]} (${maxDecrease[1]:.2f})
"""
#displays results to terminal
print(Analysis)

#finds the date the program was run and splits it into file nameable strings
dateTime=time.asctime(time.localtime())
fileTime =  dateTime.split()
#writes the results to a file with the name of <month-day-year>Analysis.txt to a file in the Analysis folder provided in the repository
fileFunctions.writeNewFile(f'PyBank\\Analysis\\{fileTime[1]}{fileTime[2]}{fileTime[4]}Analysis.txt',Analysis)
