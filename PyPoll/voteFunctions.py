
#removes personal info from the dictionary of votes and makes it a list instead
def anonomousVotes(votes):
    Avotes = []
    for vote in votes.values():
            Avotes.append(vote[1])

    return Avotes

#creates a list of candidates from anonomous vote list
def candidates(votes):

    candidates = []
    for candidate in votes:
        if not (candidate in candidates):
            candidates.append(candidate)

    return candidates


#creates a dictionary of votes per candidate with key as candidate and number of votes as value
def voteCount(votes,candidates): #voteCount(<anonomous vote list>,<list of candidates>) = {<candidate>:<number of votes>}

    votePerCandidate = {}

    for candidate in candidates:
        votePerCandidate[candidate] = votes.count(candidate)

    return votePerCandidate

#calculates percentage of votes per candidate
def votePercent(votes,candidates):#voteCount(<anonomous vote list>,<list of candidates>) = {<candidate>:<vote percentage>}

    votePercentCand = {}

    for candidate in candidates:
        votePercentCand[candidate] = votes.count(candidate)/len(votes)*100

    return votePercentCand


#find the winner based on dictionary provided by voteCount or votePercent
def winningCandidate(voteCounts): #winningCandidate(<dictionary of candidates and votes for them>) = <winner of election>
    candidates = list(voteCounts.keys())
    votes = list(voteCounts.values())
    winner = candidates[votes.index(max(votes))]
    return winner
