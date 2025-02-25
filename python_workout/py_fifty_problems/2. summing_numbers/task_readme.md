# Custom mysum function

## Description
Implement a function mysum that calculates the sum of a variable number of numeric arguments. The function should take a variable number of arguments and return their sum. If any of the arguments are not numeric (i.e., neither integers nor floats), the function should return -1 and print an error message. The function should behave similarly to the built-in sum() function but without using it.

What to do:
* Implement the function def mysum(*numbers) -> int.
* Ensure that the function works for any number of arguments, and that each argument must be a number (either integer or float).
* If a non-numeric argument is provided, return -1 and print “Not all values are of numeric type!”.

### Example 1:
```
Input: mysum(1, 2, 3)  
Output: 6  
Explanation: The sum of the numbers 1, 2, and 3 is 6.
``` 

### Example 2:
```
Input: mysum(10, 20, 30, 40, 50)  
Output: 150  
Explanation: The sum of the numbers 10, 20, 30, 40, and 50 is 150.
``` 

### Example 3:
```
Input: mysum(1, 2, '3')  
Output: -1  
Explanation: '3' is not a numeric type, so the function returns -1 and prints "Not all values are of numeric type!".
```