import random

# Functie om een dobbelsteen te gooien, kun je deze laten werken?
import Week4dobbelen_functies

# Main program
# Get the number of players
num_players = (input("Voer het aantal spelers in: "))

# Create players
players = []
for i in range(num_players):
name = input(f"Voer naam in voor Speler {i + 1}: ")
player = {'name': name, 'score': 0}
players.append(player)

# Play the dice game for 5 rounds
play_dice_game(players, 5)

# Find the winner(s)
winners = find_winner(players)

# Display the results
print("Spelresultaten:")
for player in players:
   print(f"Speler: {player['name']} | Score: {player['score']}")

print("Winnaar(s):")
for winner in winners:
    print(winner)
