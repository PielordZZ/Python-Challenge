

def timeframe(months):
    return len(months)

def netProfit(profits):
    profit = 0
    for value in profits:
        profit += value

    return profit


def changes(netProfits):
    lastProf = None
    changes=[]
    for profit in netProfits:
        if lastProf:
           changes.append(profit-lastProf)

        lastProf = profit 
    return changes


def averageProfit(changes):
    return (sum(changes)/(len(changes)))

def greatestLoss(changes,months):
    month = months[changes.index(min(changes))]
    print(month)
    return [month,min(changes)]

def greatestProfit(changes,months):
    month = months[changes.index(max(changes))]
    print(month)
    return [month,max(changes)]