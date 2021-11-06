from Tournament_Winner import tournamentWinner

def test_tournamentWinner_case_1():
    assert tournamentWinner(competitions=[['HTML', 'C#'], ['C#', 'Python'], ['Python', 'HTML']], results=[0, 0, 1]) == 'Python'

def test_tournamentWinner_case_2():
    assert tournamentWinner(competitions=[['HTML', 'Java'], ['Java', 'Python'], ['Python', 'HTML']], results=[0, 1, 1]) == 'Java'

def test_tournamentWinner_case_3():
    assert tournamentWinner(competitions=[['HTML', 'Java'], ['Java', 'Python'], ['Python', 'HTML'], ['C#', 'Python'], ['Java', 'C#'], ['C#', 'HTML']], results=[0, 1, 1, 1, 0, 1]) == 'C#'

def test_tournamentWinner_case_4():
    assert tournamentWinner(competitions=[['HTML', 'Java'], ['Java', 'Python'], ['Python', 'HTML'], ['C#', 'Python'], ['Java', 'C#'], ['C#', 'HTML'], ['SQL', 'C#'], ['HTML', 'SQL'], ['SQL', 'Python'], ['SQL', 'Java']], results=[0, 1, 1, 1, 0, 1, 0, 1, 1, 0]) == 'C#'

def test_tournamentWinner_case_5():
    assert tournamentWinner(competitions=[['Bulls', 'Eagles']], results=[1]) == 'Bulls'

def test_tournamentWinner_case_6():
    assert tournamentWinner(competitions=[['Bulls', 'Eagles'], ['Bulls', 'Bears'], ['Bears', 'Eagles']], results=[0, 0, 0]) == 'Eagles'

def test_tournamentWinner_case_7():
    assert tournamentWinner(competitions=[['Bulls', 'Eagles'], ['Bulls', 'Bears'], ['Bulls', 'Monkeys'], ['Eagles', 'Bears'], ['Eagles', 'Monkeys'], ['Bears', 'Monkeys']], results=[1, 1, 1, 1, 1, 1]) == 'Bulls'

def test_tournamentWinner_case_8():
    assert tournamentWinner(competitions=[['AlgoMasters', 'FrontPage Freebirds'], ['Runtime Terror', 'Static Startup'], ['WeC#', 'Hypertext Assassins'], ['AlgoMasters', 'WeC#'], ['Static Startup', 'Hypertext Assassins'], ['Runtime Terror', 'FrontPage Freebirds'], ['AlgoMasters', 'Runtime Terror'], ['Hypertext Assassins', 'FrontPage Freebirds'], ['Static Startup', 'WeC#'], ['AlgoMasters', 'Static Startup'], ['FrontPage Freebirds', 'WeC#'], ['Hypertext Assassins', 'Runtime Terror'], ['AlgoMasters', 'Hypertext Assassins'], ['WeC#', 'Runtime Terror'], ['FrontPage Freebirds', 'Static Startup']], results=[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == 'AlgoMasters'

def test_tournamentWinner_case_9():
    assert tournamentWinner(competitions=[['HTML', 'Java'], ['Java', 'Python'], ['Python', 'HTML'], ['C#', 'Python'], ['Java', 'C#'], ['C#', 'HTML'], ['SQL', 'C#'], ['HTML', 'SQL'], ['SQL', 'Python'], ['SQL', 'Java']], results=[0, 0, 0, 0, 0, 0, 1, 0, 1, 1]) == 'SQL'

def test_tournamentWinner_case_10():
    assert tournamentWinner(competitions=[['A', 'B']], results=[0]) == 'B'

