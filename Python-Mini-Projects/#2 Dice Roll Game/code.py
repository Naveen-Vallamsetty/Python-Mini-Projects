import random

def roll_dice():
    return random.randint(1, 6)

def play_game(num_players, max_score):
    scores = [0] * num_players
    current_player = 0

    while max(scores) < max_score:
        input(f"\nPlayer {current_player + 1}, press Enter to roll the dice:")
        round_score = 0

        while True:
            roll = roll_dice()

            if roll != 1:
                round_score += roll
                print(f"Player {current_player + 1} rolled a {roll}. Your total score is: {scores[current_player] + round_score}")
                continue_round = input("Do you want to roll again? (y/n): ").lower()

                if continue_round != 'y':
                    scores[current_player] += round_score
                    break
            else:
                print(f"Player {current_player + 1} rolled a 1. Your score reset to {scores[current_player]}.")
                break

        print(f"Player {current_player + 1} total score: {scores[current_player]}")

        if scores[current_player] >= max_score:
            print(f"Player {current_player + 1} is the winner!")
            break

        current_player = (current_player + 1) % num_players

if __name__ == "__main__":
    num_players = int(input("Enter the number of players (2 to 4): "))
    
    if num_players < 2 or num_players > 4:
        print("Please enter a number between 2 and 4 (inclusive).")
    else:
        max_score = int(input("Enter the maximum score to win: "))
        play_game(num_players, max_score)
