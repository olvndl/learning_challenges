# Average 10 km Run Time

## Description
Write a function run_timing that repeatedly asks the user for the time (in minutes) it took to run 10 km. The function should continue asking for run times until the user presses Enter without entering a value. At that point, the function should calculate and display the average time of the runs entered, along with the total number of runs.

What to do:
* Implement the function def run_timing().
* The function should accept numeric input from the user representing the time it took to run 10 km in minutes.
* The user should be able to enter multiple run times, and the function should calculate the average of all entered times.
* Once the user presses Enter without entering a value, the program should exit and display the average time along with the number of runs.

### Example 1:
```
Input:
Enter 10 km run time: 15
Enter 10 km run time: 20
Enter 10 km run time: 10
Enter 10 km run time: <enter>

Output:
Average of 15.0, over 3 runs
Explanation: The sum of the run times is 15 + 20 + 10 = 45, and the average is 45 / 3 = 15.0.
``` 

### Example 2:
```
Input:
Enter 10 km run time: 25
Enter 10 km run time: 30
Enter 10 km run time: <enter>

Output:
Average of 27.5, over 2 runs
Explanation: The sum of the run times is 25 + 30 = 55, and the average is 55 / 2 = 27.5.
``` 

### Example 3:
```
Input:
Enter 10 km run time: 12
Enter 10 km run time: <enter>

Output:
Average of 12.0, over 1 run
Explanation: The average time is 12.0 since only one run time was entered.
```