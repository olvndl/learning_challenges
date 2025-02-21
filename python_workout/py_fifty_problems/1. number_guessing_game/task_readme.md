# Number guessing game

## Description
Create a number guessing game where the program selects a random number between 0 and 3, and the user has to guess it. The program should give feedback on whether the guess is too high, too low, or correct. If the user guesses incorrectly, they can continue guessing until they get it right. Once the correct answer is guessed, the program will show the correct number and ask if the user wants to play again.

What to do:
* Implement the function def guessing_game().
* Use the randint() function to generate a random number between 0 and 3.
* Allow the user to input guesses, checking that the input is an integer and giving appropriate feedback.
* After the correct guess, ask the user if they want to play again.

### Example 1:
```
Correct answer: 3
Input: user guesses "2"
Output: "Your answer is: 2, is too low!"
``` 

### Example 2:
```
Correct answer: 1
Input: user guesses "1"
Output: "Right! Correct answer is: 1"
Do you want to play again y/n?
``` 
