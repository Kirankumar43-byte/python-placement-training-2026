# Day 9: File Handling

## Date
14-07-2026

## Topics Covered
Read, Write, Append, With Statement, CSV, Text Files

## Theory Notes
File handling allows programs to read and store data on disk. Common operations include opening files, reading content, writing new content, appending records, and closing files safely. The with statement ensures resources are released correctly after the operation. CSV files are commonly used for tabular data.

## Key Concepts
Files can be opened in read, write, append, or binary modes. The with statement is the preferred way to manage file resources.

## Advantages
Persistent storage, logging, report generation, and data exchange.

## Features
read(), write(), append(), open(), and iteration over file content.

## Syntax
```python
with open('sample.txt', 'w') as f:
    f.write('Hello file')
```

## Python Examples
- Create a text file
- Read from a file
- Append content
- Read CSV data
- Mini file project

## Real-Time Examples
File handling is used in log systems, report creators, inventory tools, and document storage apps.

## Interview Questions
1. What is the difference between write and append mode?
2. Why is the with statement used?
3. What is a CSV file?
4. How do you read a file line by line?
5. What happens if a file does not exist in read mode?
6. What is the difference between text and binary files?
7. How do you safely close a file?
8. Why is file handling important?
9. What is file buffering?
10. How do you write structured data to a file?

## LeetCode Problems Practiced
File handling practice focused on reading, writing, appending, and parsing structured data.

## Learning Outcome
The learner can manage data persistence using files and understand text and CSV formats.

## Summary
Day 9 introduced data persistence through file operations.

## Files Included
- README.md
- Notes.md
- interview_questions.md
- practice_questions.md
- leetcode.md
- examples.py
