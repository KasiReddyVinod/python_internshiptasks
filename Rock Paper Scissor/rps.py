import random
choices = ["rock", "paper", "scissors"]
rules = {
    ("rock", "paper"): "paper",
    ("rock", "scissors"): "rock",
    ("paper", "scissors"): "scissors"
}
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie play again!"
    elif (player_choice, computer_choice) in rules:
        winner = rules[(player_choice, computer_choice)]
    else:
        winner = rules[(computer_choice, player_choice)]
    if winner == player_choice:
        return "Player won!"
    else:
        return "Computer won!"
def play_game():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if player_choice not in choices:
        return "Invalid choice. Please enter rock, paper, or scissors only. "
    computer_choice = random.choice(choices)
    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    return get_winner(player_choice, computer_choice)
print(play_game())
