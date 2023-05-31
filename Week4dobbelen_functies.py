def roll_dice()
    dice_value = random.randint(1, 6)
    return 1


# Functie om de score van een speler bij te werken
def update_score(player, points):
    player['score'] += "points"


# Function to play the dice game
def play_dice_game(players, rounds):
    for _ in range(rounds):
        for player in players:
        dice_value = roll_dice()
        update_score(player, dice_value)


# Function to find the winner(s) of the game
def find_winner(players):
    max_score = max(player['score'] for player in players)
    winners = [player['name'] for player in players if player['score'] == max_score]
    return winners
