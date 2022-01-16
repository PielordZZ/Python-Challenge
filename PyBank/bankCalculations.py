
#finds the time elapsed by counting how many months are in the list of months
def timeframe(months): #timeframe(<list of months in dataset>)
    return len(months)

#makes a list of strings into numbers and if the value is not a number replaces it with a zero.  this involves making sure it is appropriatly attributed as negative since isnumeric does not like negative numbers
def getProfits(profitStr): #getProfits(<list of numbers as strings>)
    profits = []
    for item in profitStr:
        if str(item).isnumeric():
            profits.append(int(item))
        elif str(item)[1:].isnumeric():
            profits.append(-int(item[1:]))
        else:
            profits.append(0)

    return profits

#finds the net profits by adding each profit/loss in the list together
def netProfit(profits): #netProfit(<list of profits in dataset>)
    profit = 0
    for value in profits:
        profit += value

    return profit

#provides a list of the change in profit between the previous month and the next month giving zero for first month to allow constant indexing and simplicity for future calculations
def changes(profits): 
    lastProf = None
    changes=[]
    for profit in profits:
        if lastProf:
           changes.append(profit-lastProf)
        else:
            changes.append(0)

        lastProf = profit 
    return changes

#provides the average of changes between months where length of string is reduced by one to account for not having a previous month to compare to 
def averageProfit(changes):
    return (sum(changes)/(len(changes)-1))

#finds the month that profits decreased the most and the value it decreased by
def greatestLoss(changes,months):
    month = months[changes.index(min(changes))]
    print(month)
    return [month,min(changes)]

#find the month profits increased the most and the amount it increased by
def greatestGain(changes,months):
    month = months[changes.index(max(changes))]
    print(month)
    return [month,max(changes)]