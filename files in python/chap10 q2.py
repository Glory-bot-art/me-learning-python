import random

def game():
    score = 0
    high_score = 0

    while True:
        # Generate a random number between 1 and 10
        target_number = random.randint(1, 10)

        # Ask the user to guess the number
        user_guess = int(input("Guess the number between 1 and 10: "))

        # Check if the user's guess is correct
        if user_guess == target_number:
            score += 1
            print("Correct! Your score is", score)
        else:
            print("Incorrect! The correct number was", target_number)

        # Check if the user wants to quit
        if input("Do you want to quit? (y/n): ").lower() == 'y':
            break

    # Check if the user's score is higher than the high score
    if score > high_score:
        high_score = score
        print("New high score!", high_score)
    else:
        print("High score:", high_score)

    return score

final_score = game()
print("Final score:", final_score)


with open("hi score.txt", "a") as f:
    f.write(f"{final_score}\n")