"""
Given an array of pairs of teams that compete. With the first team
being home, and the second being away.: [[a,b], [c,d],[a,c]]
And a results array, where 1 means home won, and 0 means away won: [0, 0, 1]
Winner of match gets 3 points.

Return team with most accumulated points after every game is complete.
"""

# Inputs
competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]

results = [0, 0, 1]


# Solution #1
def tournamentWinner(competitions: list, results: list):
    """
    Creates a scores dictionary to keep track of scores, and a
    currentBestTeam variable keeping track of best team. Go through each
    game and update currentBestTeam and scores accordingly.

    time: O(n) -> traversing through each competition
    space: O(t) - > storing dictionary values of up to t number of teams
    """

    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for competition, result in zip(competitions, results):
        if result:
            winner = competition[0]
            if winner in scores:
                scores[winner] += 1
            else:
                scores[winner] = 1
        else:
            winner = competition[1]
            if winner in scores:
                scores[winner] += 1
            else:
                scores[winner] = 1
        if scores[winner] > scores[currentBestTeam]:
            currentBestTeam = winner

    return currentBestTeam
