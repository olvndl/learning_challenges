# Correct Brackets Sequence

## Description
Given a string s consisting of different types of brackets ((), {}, []), implement a function to check if the brackets are correctly matched and nested. 

A valid sequence means:
* Every opening bracket has a corresponding closing bracket. 
* Brackets are properly nested (e.g., ([]) is valid, but {[)]} is not).

What to do:
* Implement the function def correct_brackets_sequence(s: str) -> bool.
* Use a stack to ensure that every opening bracket has a corresponding closing bracket.
* Ensure the solution correctly handles different types of brackets and checks for proper nesting.

### Example 1:
```
Input: s = "([])"  
Output: True  
Explanation: The brackets are correctly matched and nested.
``` 

### Example 2:
```
Input: s = "{)"  
Output: False  
Explanation: The opening bracket `{` is not matched with the correct closing bracket `)`.
``` 

### Example 3:
```
Input: s = "{[()()][]}"  
Output: True  
Explanation: All brackets are correctly matched and nested.
``` 
