import random

options = ("rock", "paper", "scissors") # a tuple because we don't need to add or remove options, we just want to access them by index
beats = { "rock": "scissors", "paper": "rock", "scissors": "paper"} # a dictionary because i want to associate each option with the option it beats


rounds = 0
while rounds <= 0:
    rounds = int(input("How many rounds? "))
    if rounds <= 0:
        print("Must be at least 1 round")

wins = 0
losses = 0
ties = 0


for r in range(rounds):
    print(f"\nRound {r + 1}")
    print("1) rock  2) paper  3) scissors")

    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input("Pick 1, 2, or 3: "))
        if choice < 1 or choice > 3:
            print("Must be 1, 2, or 3")

    player = options[choice - 1]
    computer = random.choice(options)
    print(f"You picked: {player}")
    print(f"Computer picked: {computer}")

    if player == computer:
        ties += 1
        print("Tie!")
    elif beats[player] == computer:
        wins += 1
        print("You win!")
    else:
        losses += 1
        print("Computer wins!")


print("\n------- Results -------")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Ties: {ties}")