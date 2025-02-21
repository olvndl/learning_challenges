from random import randint


def guessing_game():
    correct_answer = randint(0, 3)

    while True:
        try:
            user_answer = int(input("What is your guess? "))
        except ValueError:
            print("Not a number, please use integers only")
            continue

        if user_answer == correct_answer:
            print(f'Right! Correct answer is: {user_answer}')
            break
        elif user_answer > correct_answer:
            print(f"'Your answer is: {user_answer}, is too high!')")
        else:
            print(f"'Your answer is: {user_answer}, is too low!')")

    play_agan = input("Do you want to play again y/n? ")

    if play_agan == "y":
        guessing_game()


guessing_game()
