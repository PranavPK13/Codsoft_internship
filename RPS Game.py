import random

def user():
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    return user_choice

def computer():
    return random.choice(["rock", "paper", "scissors"])

def result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Both chose the same. It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "Congratulations, You win!"
    else:
        return "Computer wins! Better Luck Next Time"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = user()
    computer_choice = computer()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    print(result(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
