# Day 10: Exception Handling

## Date
15-07-2026

## Topics Covered
try, except, finally, raise, custom exceptions

## Theory Notes
Exception handling allows a program to respond gracefully to runtime errors. The try block contains code that may fail, except catches the error, finally runs regardless of the outcome, and raise allows custom exceptions to be triggered when necessary.

## Key Concepts
Exceptions are errors that occur during execution. They should be handled to keep the application resilient and user-friendly.

## Advantages
Better reliability, easier debugging, and a smoother user experience.

## Features
Specific exception handling, custom exception classes, and cleanup logic.

## Syntax
```python
try:
    x = int('abc')
except ValueError:
    print('Invalid value')
```

## Python Examples
- Handle division by zero
- Catch invalid input
- Custom exception example
- Cleanup with finally
- Raise an exception

## Real-Time Examples
Exception handling is used in banking apps, APIs, payment systems, and data processing workflows.

## Interview Questions
1. What is an exception?
2. What is the purpose of try and except?
3. What is finally used for?
4. What is a custom exception?
5. What is the difference between an error and an exception?
6. What is raising an exception?
7. Why should exceptions be handled?
8. What is the role of finally in cleanup?
9. How do you handle multiple exceptions?
10. What happens if an exception is not handled?

## LeetCode Problems Practiced
Exception handling practice focused on debugging, resilience, and reliable input handling.

## Learning Outcome
The learner can write robust programs that recover from errors gracefully.

## Summary
Day 10 emphasized defensive programming and graceful failure handling.

## Files Included
- README.md
- Notes.md
- interview_questions.md
- practice_questions.md
- leetcode.md
- examples.py
