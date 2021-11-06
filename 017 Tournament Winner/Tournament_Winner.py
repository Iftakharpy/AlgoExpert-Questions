# Not Good
# time O(n) + O(n) -> O(n)
# space O(k) - where k is the number of unique team in competitions
def tournamentWinner(competitions, results):
    scores = {}
    for match, res in zip(competitions, results):
        team_won = match[1] if res == 0 else match[0]
        if not team_won in scores:
            scores[team_won] = 3
        else:
            scores[team_won] += 3
    
    high_score = 0
    winner = ""
    for participent, score in scores.items():
        if score>high_score:
            winner = participent
            high_score = score
    return winner

# Best
# time O(n) - n is the len(results)
# space O(k) - where k is unique teams
def tournamentWinner(competitions, results):
    current_best = ""
    scores = {current_best: 0}
    
    for match, res in zip(competitions, results):
        won = match[1] if res == 0 else match[0]
        
        if won not in scores:
            scores[won] = 0
        scores[won] += 1
        
        if scores[won] > scores[current_best]:
            current_best = won
    
    return current_best
