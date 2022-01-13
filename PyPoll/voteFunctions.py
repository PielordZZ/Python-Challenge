

def anonomousVotes(votes):
    Avotes = []
    for vote in votes.values():
            Avotes.append(vote[1])

    return Avotes
def candidates(votes):

    candidates = []
    for candidate in votes:
        if not (candidate in candidates):
            candidates.append(candidate)

    return candidates

def voteCount(votes,candidates):

    votePerCandidate = {}

    for candidate in candidates:
        votePerCandidate[candidate] = votes.count(candidate)

    return votePerCandidate

def votePercent(votes,candidates):

    votePercentCand = {}

    for candidate in candidates:
        votePercentCand[candidate] = votes.count(candidate)/len(votes)*100

    return votePercentCand

def winningCandidate(voteCounts):
    candidates = list(voteCounts.keys())
    votes = list(voteCounts.values())
    winner = candidates[votes.index(max(votes))]
    return winner
