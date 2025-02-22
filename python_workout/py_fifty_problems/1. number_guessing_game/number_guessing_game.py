from random import randint


def play_guessing_game(first_round):
    MIN_NUMBER = 0
    MAX_NUMBER = 100
    MAX_ATTEMPTS = 6

    correct_answer = randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    if first_round:
        print("Welcome to the Guessing Game! ", end="")
    else:
        print("Welcome back to the Guessing Game! ", end="")

    print(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}.\n")

    while attempts < MAX_ATTEMPTS:
        try:
            user_answer = int(input("What is your guess? "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == correct_answer:
            print(f"Congratulations! You guessed the correct number: {user_answer}.")
            break
        elif user_answer > correct_answer:
            print(f"Your guess {user_answer} is too high!")
        else:
            print(f"Your guess {user_answer} is too low!")

        attempts += 1

    else:
        print(f"Sorry, you've used all {MAX_ATTEMPTS} attempts."
              f" The correct number was {correct_answer}.")


def main():
    first_run = True

    while True:
        play_guessing_game(first_run)

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break

        first_run = False


if __name__ == "__main__":
    main()
