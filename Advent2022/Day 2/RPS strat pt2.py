'''
A for Rock          X for Lose      (0 point)
B for Paper         Y for Draw      (3 points)
C for Scissors      Z for Win       (6 points)

The score for a single round is the score for the shape you selected 
plus the score for the outcome of the round. 
(0 if you lost, 3 if the round was a draw, and 6 if you won).
'''
def round_played(round):
    if round[1] == "X":
        if round[0] == "A":     # Rock
            return 3
        elif round[0] == "B":   # Paper
            return 1
        elif round[0] == "C":   # Scissors
            return 2
    if round[1] == "Y":
        if round[0] == "A":     # Rock
            return 4
        elif round[0] == "B":   # Paper
            return 5
        elif round[0] == "C":   # Lost
            return 6
    if round[1] == "Z":
        if round[0] == "A":     # Rock
            return 8
        elif round[0] == "B":   # Paper
            return 9
        elif round[0] == "C":   # Draw
            return 7

strategy_guide = open("Day 2\input.txt", "r")
total_points = 0

for round in strategy_guide.read().split("\n"):
    if round == '':
        break
    round = round.split(" ")
    total_points += round_played(round)
    
print(total_points)
    
    