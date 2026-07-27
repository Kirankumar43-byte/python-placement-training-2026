from pathlib import Path
import textwrap

ROOT = Path(r"c:\Users\Kiran Kumar\OneDrive\Desktop\python-placement-training-2026")
ROOT.mkdir(parents=True, exist_ok=True)


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def day_files(day_num, title, date, topics, theory, key_concepts, advantages, features, syntax, examples, real_world, interview_qs, practice_qs, problems, learning_outcome, summary, files_included, notes_content, examples_code):
    folder = ROOT / f"Day-{day_num:02d}_{title.replace(' ', '_').replace('/', '_')}"
    folder.mkdir(parents=True, exist_ok=True)
    write(folder / "README.md", f"""# Day {day_num}: {title}

## Date
{date}

## Topics Covered
{topics}

## Theory Notes
{theory}

## Key Concepts
{key_concepts}

## Advantages
{advantages}

## Features
{features}

## Syntax
{syntax}

## Python Examples
{examples}

## Real-Time Examples
{real_world}

## Interview Questions
{interview_qs}

## LeetCode Problems Practiced
{problems}

## Learning Outcome
{learning_outcome}

## Summary
{summary}

## Files Included
- README.md
- Notes.md
- interview_questions.md
- practice_questions.md
- examples.py
""")
    write(folder / "Notes.md", f"""# Notes for Day {day_num}: {title}

{notes_content}
""")
    write(folder / "interview_questions.md", f"""# Interview Questions - Day {day_num}

{interview_qs}
""")
    write(folder / "practice_questions.md", f"""# Practice Questions - Day {day_num}

{practice_qs}
""")
    write(folder / "examples.py", examples_code)
    write(folder / "learning_summary.md", f"""# Learning Summary - Day {day_num}

{learning_outcome}
""")
    write(folder / "real_time_applications.md", f"""# Real-Time Applications - Day {day_num}

{real_world}
""")
    write(folder / "important_points.md", f"""# Important Points - Day {day_num}

{key_concepts}
""")
    write(folder / "common_mistakes.md", f"""# Common Mistakes - Day {day_num}

- Avoid skipping syntax rules.
- Do not confuse mutable and immutable data types.
- Practice debugging by reading error messages carefully.
- Write readable code with meaningful names.
""")
    return folder


# Root README
root_readme = """# Python Placement Training 2026

![Python Banner](https://img.shields.io/badge/Python-Placement%20Training-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?style=for-the-badge&logo=github)
![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)

This repository documents my complete placement preparation journey in Python during 2026. It combines daily theory notes, practical programs, interview preparation, LeetCode discussion, and project progress in a recruiter-friendly format.

## Table of Contents
- [Repository Overview](#repository-overview)
- [Training Timeline](#training-timeline)
- [Skills Learned](#skills-learned)
- [Daily Progress](#daily-progress)
- [LeetCode Statistics](#leetcode-statistics)
- [MCQ Test Scores](#mcq-test-scores)
- [Project Section](#project-section)
- [Future Learning Goals](#future-learning-goals)

## Repository Overview
This portfolio is designed to show consistency, discipline, and technical growth. Each day contains structured notes, practical examples, coding questions, and interview-focused material.

## Training Timeline
- 06 July 2026 - Training Started
- 10 July 2026 - MCQ Test 1
- 17 July 2026 - MCQ Test 2
- 24 July 2026 - MCQ Test 3
- Ongoing - Daily Python practice and interview preparation

## Skills Learned
- Python Basics and Syntax
- Data Structures and Control Flow
- Functions, Modules, and Exception Handling
- Object-Oriented Programming
- Database Programming with SQLite
- CRUD Operations and Automation
- Interview Preparation and Problem Solving

## Daily Progress
| Day | Topic | Status |
|---|---|---|
| 01 | Python Introduction | Completed |
| 02 | Variables and Data Types | Completed |
| 03 | Conditional Statements | Completed |
| 04 | Loops | Completed |
| 05 | Lists and Tuples | Completed |
| 06 | Sets and Dictionaries | Completed |
| 07 | Functions | Completed |
| 08 | Lambda and Modules | Completed |
| 09 | File Handling | Completed |
| 10 | Exception Handling | Completed |
| 11 | OOP Classes | Completed |
| 12 | OOP Advanced | Completed |
| 13 | Standard Libraries | Completed |
| 14 | SQLite | Completed |
| 15 | CRUD Operations | Completed |
| 16 | Current Progress | Ongoing |

## LeetCode Statistics
- Topics Covered: Arrays, Strings, Hashing, Sorting, Recursion, and Basic Data Structures
- Practice Focus: Problem solving, logic building, and explanation quality
- Current Goal: Improve speed and accuracy for placement rounds

## MCQ Test Scores
| Date | Score |
|---|---:|
| 10 July 2026 | 24/25 |
| 17 July 2026 | 24/25 |
| 24 July 2026 | 24/25 |

## Project Section
The main project is an AI Digital Twin for Personalized Student Learning.

- [AI-Digital-Twin-Project](AI-Digital-Twin-Project/README.md)
- [MCQ Tests](MCQ-Tests/README.md)

## Future Learning Goals
- Strengthen DSA and problem solving
- Build end-to-end Python projects
- Prepare for company-specific interview rounds
- Improve communication and explanation skills

---

## Daily Learning Folders
- [Day 01 - Python Introduction](Day-01_Python_Introduction/README.md)
- [Day 02 - Variables and Data Types](Day-02_Variables_DataTypes/README.md)
- [Day 03 - Conditional Statements](Day-03_Conditional_Statements/README.md)
- [Day 04 - Loops](Day-04_Loops/README.md)
- [Day 05 - Lists and Tuples](Day-05_List_Tuple/README.md)
- [Day 06 - Sets and Dictionaries](Day-06_Sets_Dictionaries/README.md)
- [Day 07 - Functions](Day-07_Functions/README.md)
- [Day 08 - Lambda and Modules](Day-08_Lambda_Modules/README.md)
- [Day 09 - File Handling](Day-09_File_Handling/README.md)
- [Day 10 - Exception Handling](Day-10_Exception_Handling/README.md)
- [Day 11 - OOP Classes](Day-11_OOP_Classes/README.md)
- [Day 12 - OOP Advanced](Day-12_OOP_Advanced/README.md)
- [Day 13 - Standard Libraries](Day-13_Standard_Libraries/README.md)
- [Day 14 - SQLite](Day-14_SQLite/README.md)
- [Day 15 - CRUD Operations](Day-15_CRUD/README.md)
- [Day 16 - Current Progress](Day-16_Current_Progress/README.md)
"""
write(ROOT / "README.md", root_readme)

# MCQ tests docs
write(ROOT / "MCQ-Tests" / "README.md", """# MCQ Tests

## Test History
- 10 July 2026 - Score: 24/25
- 17 July 2026 - Score: 24/25
- 24 July 2026 - Score: 24/25

## Observations
These tests helped strengthen conceptual clarity in Python, logic building, and interview readiness.
""")

# Project docs
write(ROOT / "AI-Digital-Twin-Project" / "README.md", """# AI Digital Twin for Personalized Student Learning

## Overview
This project focuses on building a digital twin platform that can recommend learning paths and adaptively guide students.

## Objectives
- Personalize learning experiences
- Track student progress
- Recommend practice activities
- Improve retention and performance

## Technologies
- Python
- SQLite
- Markdown
- GitHub
- Future expansion into web APIs and dashboards

## Current Progress
- Project idea finalized
- Architecture discussed
- Documentation started
- Viva 1 and Viva 2 completed
- PPT submitted
""")

write(ROOT / "Database_Task.md", """# Database Task

This file summarizes the database tasks completed during Day 14 and Day 15.

## Topics Covered
- SQLite database creation
- Table design
- CRUD operations
- Student, Employee, and Library data handling

## Outcome
The repository now includes practical examples for database creation, insertion, updates, deletion, and querying.
""")

# Day content definitions

day_specs = [
    {
        "day_num": 1,
        "title": "Python Introduction",
        "date": "06-07-2026",
        "topics": "What is Python, History of Python, Advantages, Features, Applications, Python Libraries, OOP Concepts, Python Installation, Python Execution Flow, Compiler vs Interpreter",
        "theory": "Python is a high-level, interpreted, and beginner-friendly programming language. It emphasizes readability and enables developers to build web apps, automation scripts, data science tools, and AI systems quickly. Its history traces back to Guido van Rossum and the language evolved into one of the most popular languages in the world. Python supports multiple programming paradigms, including procedural, functional, and object-oriented approaches.",
        "key_concepts": "Python is easy to read, supports rapid development, uses indentation for structure, and runs through an interpreter. Installation involves downloading Python from the official website and configuring PATH. The execution flow includes source code, parsing, bytecode generation, and runtime execution.",
        "advantages": "Easy syntax, strong community support, cross-platform capability, wide library ecosystem, and strong use in AI, automation, and web development.",
        "features": "Dynamically typed, interpreted, object-oriented, garbage collected, portable, and rich in built-in libraries.",
        "syntax": "```python\nprint('Hello, World!')\nname = 'Alex'\nprint(name)\n```",
        "examples": "- Hello World program\n- Input and output demonstration\n- Arithmetic operation example\n- Simple variable usage\n- Comments and print statements",
        "real_world": "Python is used in automation, web development, data analysis, machine learning, scripting, and backend systems.",
        "interview_qs": "1. What is Python?\n2. Why is Python popular?\n3. What is the difference between compiler and interpreter?\n4. What are Python libraries?\n5. What is OOP in Python?\n6. What is indentation in Python?\n7. What is the purpose of the Python interpreter?\n8. What are the main applications of Python?\n9. What are the advantages of using Python?\n10. What is the difference between script and program?\n11. What is a variable in Python?\n12. What is the role of PEP 8?\n13. Why is Python considered beginner-friendly?\n14. How does Python differ from Java?\n15. What is the role of a REPL?",
        "practice_qs": "1. Write a Python program to print your name.\n2. Write a program to add two numbers.\n3. Write a program to print the sum of three numbers.\n4. Write a program to display your favorite hobby.\n5. Write comments in your code to explain each step.\n6. Write a program that accepts user input and displays it.\n7. Explain the difference between compiler and interpreter in one paragraph.\n8. Install Python and verify the version using the terminal.",
        "problems": "No LeetCode problem assigned on Day 1. Focus was on understanding Python basics and coding mindset.",
        "learning_outcome": "The learner understands the purpose of Python, its ecosystem, execution model, and common applications.",
        "summary": "Day 1 introduced Python as a powerful and beginner-friendly language and established a strong base for future topics.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Python is known for readability and simplicity. It uses indentation instead of braces, which makes code look clean. Python programs can be executed line by line by an interpreter. The language is widely used because of its large user community and extensive libraries. During this day, the focus was on understanding the language at a conceptual level before diving into syntax and logic.",
        "examples_code": "print('Hello, World!')\nprint('Welcome to Python Placement Training')\n\nname = input('Enter your name: ')\nprint('Hello', name)\n\nnum1 = 10\nnum2 = 20\nprint('Sum:', num1 + num2)\n\n# Comments help explain code\n# Python uses indentation to define blocks\n"
    },
    {
        "day_num": 2,
        "title": "Variables and Data Types",
        "date": "07-07-2026",
        "topics": "Variables, Identifiers, Keywords, Data Types, Input Output, Type Conversion, Operators Introduction",
        "theory": "Variables store data values that can be reused during execution. A valid identifier follows naming rules and cannot be a keyword. Python has built-in data types such as integers, floats, strings, booleans, lists, tuples, sets, and dictionaries. Input and output operations help programs interact with users. Type conversion allows us to switch between compatible data types.",
        "key_concepts": "Variables are containers for values. Keywords are reserved words. Identifiers must be descriptive and follow Python naming conventions. Operators perform arithmetic, comparison, and assignment tasks.",
        "advantages": "Strong data handling, easy readability, flexible type conversions, and simple I/O mechanisms.",
        "features": "Dynamic typing, expressive syntax, built-in functions like int(), float(), str(), bool(), and input().",
        "syntax": "```python\nname = 'Sam'\nage = 21\nprint(name, age)\nvalue = int(input('Enter number: '))\n```",
        "examples": "- Variable declaration and printing\n- String concatenation\n- Type conversion example\n- Arithmetic operators\n- Boolean expression example",
        "real_world": "Variables and data types are used in calculators, login systems, recommendation engines, and any software that stores user information.",
        "interview_qs": "1. What is a variable in Python?\n2. What is an identifier?\n3. What are keywords in Python?\n4. How is type conversion performed?\n5. What is the difference between int and float?\n6. What is the purpose of input()?\n7. What is dynamic typing?\n8. What are the common data types in Python?\n9. What is the difference between == and =?\n10. Why is Python considered strongly typed?",
        "practice_qs": "1. Create variables for name, age, and city.\n2. Convert a string input into an integer.\n3. Write a program that swaps two numbers.\n4. Find the area of a rectangle using variables.\n5. Write a program to calculate simple interest.\n6. Write a program to check whether a number is even or odd.\n7. Use arithmetic operators to solve a math task.\n8. Create a program to print the data type of an input value.",
        "problems": "- Fizz Buzz\n- Palindrome Number\n- Reverse Integer\n- Plus One\n- Length of Last Word\n- Valid Palindrome\n- To Lower Case\n- Reverse String",
        "learning_outcome": "The learner can define variables, choose suitable data types, convert values, and work with basic input and output operations.",
        "summary": "Day 2 introduced the core building blocks of Python programs through variables, types, operators, and input handling.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Variables are named locations in memory that hold values. Choosing descriptive names helps readability and maintainability. Python supports many built-in data types, and the same variable can hold different values at different times because Python uses dynamic typing. Operators help perform calculations and comparisons. Type conversion is especially important when receiving user input from the terminal.",
        "examples_code": "name = 'Riya'\nage = 22\nprint('Name:', name)\nprint('Age:', age)\n\nnum = int(input('Enter a number: '))\nprint('Square:', num * num)\n\n# Type conversion examples\nvalue = '100'\nprint(int(value) + 5)\n\n# Boolean example\nprint(10 > 5)\n"
    },
    {
        "day_num": 3,
        "title": "Conditional Statements",
        "date": "08-07-2026",
        "topics": "if, if else, Nested if, elif, Comparison Operators, Logical Operators, Assignment, Identity, Membership, Bitwise Operators",
        "theory": "Conditional statements allow programs to make decisions based on certain conditions. Python uses if, elif, and else to control the flow of execution. Comparison and logical operators evaluate conditions and enable layered decision-making. Identity, membership, and bitwise operators add more flexibility for special cases.",
        "key_concepts": "The if block executes when a condition is true. elif chains multiple conditions and else handles the default case. Conditions are evaluated using Boolean logic.",
        "advantages": "They make programs interactive and adaptive to changing inputs and contexts.",
        "features": "Readable decision trees, support for nested conditions, and flexible combination of operators.",
        "syntax": "```python\nage = 18\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')\n```",
        "examples": "- Voting eligibility check\n- Grade classification\n- Login validation\n- Multiple condition handling\n- Nested if example",
        "real_world": "Conditionals are used in login systems, admission rules, payment validation, and game logic.",
        "interview_qs": "1. What is the difference between if and elif?\n2. What happens in a nested if statement?\n3. What is the purpose of an else block?\n4. How are logical operators used in decision-making?\n5. What is the difference between is and ==?\n6. What are membership operators?\n7. Why are bitwise operators useful?\n8. Can you use multiple conditions in one if statement?\n9. What is a Boolean expression?\n10. Explain the role of indentation in conditionals.",
        "practice_qs": "1. Check whether a number is positive or negative.\n2. Classify marks into Grade A/B/C.\n3. Validate a password length.\n4. Determine the largest of three numbers.\n5. Implement a menu-based calculator.\n6. Write a program to check leap year.\n7. Perform age classification using nested if.\n8. Write a program to test if a value exists in a list.",
        "problems": "- Integer to Roman\n- Jump Game\n- Gas Station\n- Spiral Matrix\n- Set Matrix Zeroes\n- Container With Most Water\n- 3Sum\n- Rotate Image",
        "learning_outcome": "The learner can write decision-based programs and understand how conditions drive the application's behavior.",
        "summary": "Day 3 focused on controlling program flow using conditional logic and operator-based decision making.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Decision-making is one of the main pillars of programming. Conditional statements help the code choose one path over another based on truth values. Python’s structured indentation style makes these blocks easy to read. In practice, conditions are usually combined with comparison and logical operators to build more meaningful business rules.",
        "examples_code": "age = 20\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')\n\nmarks = 82\nif marks >= 90:\n    grade = 'A'\nelif marks >= 75:\n    grade = 'B'\nelse:\n    grade = 'C'\nprint('Grade:', grade)\n\n# Membership operator\nfruits = ['apple', 'banana']\nprint('apple' in fruits)\n"
    },
    {
        "day_num": 4,
        "title": "Loops",
        "date": "09-07-2026",
        "topics": "for, while, Nested Loops, break, continue, pass, Real-Time Loop Applications",
        "theory": "Loops allow repeated execution of code blocks. A for loop is commonly used over a range or collection, while a while loop continues until a condition becomes false. break exits early, continue skips the current iteration, and pass acts as a placeholder. Loops are critical for automation, iteration, and repetitive tasks.",
        "key_concepts": "A loop repeats code efficiently. The iteration variable changes with each cycle. Proper loop control helps avoid infinite loops and manage flow precisely.",
        "advantages": "Saves time, reduces repetitive code, and supports data processing at scale.",
        "features": "Range-based iteration, condition-based iteration, and loop control statements.",
        "syntax": "```python\nfor i in range(5):\n    print(i)\n\nwhile count < 3:\n    print(count)\n    count += 1\n```",
        "examples": "- Print numbers 1 to 10\n- Sum of first n integers\n- Pattern printing\n- Prime number check\n- Factorial loop",
        "real_world": "Loops are used in dashboards, file scanning, sending emails, processing records, and monitoring systems.",
        "interview_qs": "1. What is the difference between for and while?\n2. What does break do?\n3. What does continue do?\n4. What is pass used for?\n5. How do you avoid infinite loops?\n6. What are nested loops?\n7. How do loops help in data processing?\n8. What is a range in Python?\n9. Can you use loops with strings?\n10. What is the role of iteration variables?",
        "practice_qs": "1. Print numbers from 1 to 20.\n2. Print even numbers up to 50.\n3. Calculate the sum of numbers from 1 to 100.\n4. Find the factorial of a number.\n5. Check if a number is prime.\n6. Print a pattern of stars.\n7. Reverse a string using a loop.\n8. Count vowels in a word.\n9. Print the multiplication table.\n10. Find the largest element in a list.\n11. Print the Fibonacci series.\n12. Sum the digits of a number.\n13. Print all factors of a number.\n14. Use a while loop to reverse a number.\n15. Create a nested loop for a matrix pattern.\n16. Print odd numbers in descending order.\n17. Use continue to skip even values.\n18. Use break when a condition is met.\n19. Print the first 10 triangular numbers.\n20. Build a simple countdown program.",
        "problems": "Loop-based coding challenges were practiced across pattern printing, number analysis, and iteration tasks.",
        "learning_outcome": "The learner can write iterative programs and control loop execution effectively.",
        "summary": "Day 4 strengthened problem-solving skills by teaching structured iteration and loop control techniques.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Loops make repetition manageable and readable. They are often used when a task needs to be repeated a known number of times or until a condition is met. Understanding loop control is important because a small logic issue can easily produce an infinite loop. In interviews, loop-based problems often test consistency, edge case awareness, and clarity of thought.",
        "examples_code": "for i in range(1, 6):\n    print(i)\n\ncount = 1\nwhile count <= 5:\n    print('Count:', count)\n    count += 1\n\nfor i in range(1, 4):\n    for j in range(1, 4):\n        print(i, j)\n\n# break and continue\nfor x in range(1, 10):\n    if x == 5:\n        break\n    print(x)\n"
    },
    {
        "day_num": 5,
        "title": "Lists and Tuples",
        "date": "10-07-2026",
        "topics": "Lists, Tuples, Operations, Methods, Advantages, Differences, Mutability",
        "theory": "Lists and tuples are common sequence data structures in Python. Lists are mutable, meaning they can be changed after creation, whereas tuples are immutable and often used when the data should remain constant. Both support indexing, slicing, and iteration. Their choice depends on whether flexibility or safety is more important.",
        "key_concepts": "Lists support methods like append, remove, insert, and sort. Tuples are useful for fixed data collections. Understanding mutability helps in writing secure and efficient code.",
        "advantages": "Lists are flexible and powerful; tuples provide stability and can be safer for fixed data.",
        "features": "Indexing, slicing, methods, iteration, and support for mixed data types.",
        "syntax": "```python\nfruits = ['apple', 'banana']\nfruits.append('mango')\n\npoint = (10, 20)\nprint(point[0])\n```",
        "examples": "- Create and print lists\n- Append and remove items\n- Sort a list\n- Convert a tuple to a list\n- Iterate through a list",
        "real_world": "Lists and tuples are used in product catalogs, student records, task management apps, and data processing pipelines.",
        "interview_qs": "1. What is the difference between a list and a tuple?\n2. Why are lists mutable?\n3. What are common list methods?\n4. What is indexing?\n5. How do you slice a list?\n6. Why might you choose a tuple over a list?\n7. Can a list contain different data types?\n8. What is the difference between append and extend?\n9. What is a nested list?\n10. How do you remove an element from a list?",
        "practice_qs": "1. Create a list of five fruits.\n2. Add a new fruit to the list.\n3. Remove a specific fruit.\n4. Sort the list in alphabetical order.\n5. Reverse a list.\n6. Find the length of a list.\n7. Access the last item of a tuple.\n8. Create a list of numbers and find the sum.",
        "problems": "- Replace Elements with Greatest Element on Right Side\n- Squares of Sorted Array\n- Height Checker\n- Best Time to Buy and Sell Stock\n- Transpose Matrix\n- Sort Array by Parity",
        "learning_outcome": "The learner can manipulate sequences, choose between lists and tuples, and solve array-related problems with confidence.",
        "summary": "Day 5 built a strong foundation in Python sequences, showing how data can be stored, accessed, and transformed efficiently.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Lists are one of the most used structures in Python because they are flexible and convenient. Tuples offer immutability, which makes them suitable for representing fixed values. Both structures support common operations like indexing and slicing, but their behavior differs when modifications are required. Understanding this distinction is crucial during interviews and when writing production-grade code.",
        "examples_code": "numbers = [1, 2, 3, 4]\nnumbers.append(5)\nprint(numbers)\n\nfruits = ['apple', 'banana']\nfruits.remove('banana')\nprint(fruits)\n\npoint = (10, 20)\nprint(point[0])\n\n# Sorting\nvalues = [5, 2, 9, 1]\nvalues.sort()\nprint(values)\n"
    },
    {
        "day_num": 6,
        "title": "Sets and Dictionaries",
        "date": "11-07-2026",
        "topics": "Sets, Dictionary, Dictionary Methods, Set Operations, List Comprehension, Nested Comprehension",
        "theory": "Sets are unordered collections of unique elements, while dictionaries store data as key-value pairs. Sets are useful for membership testing and eliminating duplicates. Dictionaries support fast lookups and are widely used for structured data. Comprehensions make it easy to build collections in a compact way.",
        "key_concepts": "Use sets for unique values and dictionaries for mappings. Comprehensions offer concise syntax for building lists, sets, and dictionaries.",
        "advantages": "Efficient operations, strong support for uniqueness, and intuitive mapping behavior.",
        "features": "Union, intersection, difference, add, remove, update, and dictionary methods like get and items.",
        "syntax": "```python\nnums = {1, 2, 3}\nstudent = {'name': 'Asha', 'age': 21}\nprint(student['name'])\n```",
        "examples": "- Create a set\n- Remove duplicates from a list\n- Build a dictionary\n- Use dictionary methods\n- Use comprehension",
        "real_world": "Dictionaries and sets are used in search engines, caching, configuration files, analytics, and data cleaning.",
        "interview_qs": "1. What is a set in Python?\n2. What is a dictionary?\n3. What is the difference between a list and a set?\n4. What is a comprehension?\n5. What is a nested dictionary?\n6. How do you add keys to a dictionary?\n7. What does items() return?\n8. What is the purpose of set union?\n9. Why are sets useful for duplicates?\n10. How do you access values in a dictionary?",
        "practice_qs": "1. Create a set of five numbers.\n2. Remove duplicates from a list using a set.\n3. Create a dictionary of student marks.\n4. Update a dictionary value.\n5. Use set intersection on two sets.\n6. Write a list comprehension for squares.\n7. Create a nested dictionary of courses.\n8. Print all keys and values from a dictionary.",
        "problems": "- 217. Contains Duplicate\n- 1748. Sum of Unique Elements\n- 387. First Unique Character in a String\n- 389. Find the Difference",
        "learning_outcome": "The learner can work with mappings and unique collections and use comprehension techniques for compact code.",
        "summary": "Day 6 introduced collections that are optimized for uniqueness and quick lookup.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Sets and dictionaries are both highly practical structures in everyday Python programming. Sets help manage uniqueness, while dictionaries are ideal for mapping one value to another. Comprehensions allow you to express transformations elegantly. These structures appear frequently in coding interviews, especially around frequency counting and duplicate detection.",
        "examples_code": "nums = [1, 2, 2, 3, 4, 4]\nunique_nums = set(nums)\nprint(unique_nums)\n\nstudent = {'name': 'Asha', 'age': 21}\nstudent['city'] = 'Bengaluru'\nprint(student)\n\n# Comprehension\nsquares = [x * x for x in range(5)]\nprint(squares)\n"
    },
    {
        "day_num": 7,
        "title": "Functions",
        "date": "12-07-2026",
        "topics": "Functions, Parameters, Arguments, Return, Default Arguments, Keyword Arguments, Variable Length Arguments, Recursion",
        "theory": "Functions are reusable blocks of code that perform a specific task. They improve modularity and simplify code organization. Parameters allow input values to be passed into a function, and return values let the function provide a result. Advanced function concepts include default arguments, keyword arguments, variable-length arguments, and recursion.",
        "key_concepts": "Functions reduce repetition, improve readability, and make debugging easier. Recursion is a powerful technique where a function calls itself with smaller inputs.",
        "advantages": "Reusability, readability, easier testing, and maintainability.",
        "features": "Arguments, returns, optional parameters, scope, and recursion.",
        "syntax": "```python\ndef add(a, b):\n    return a + b\n\nprint(add(2, 3))\n```",
        "examples": "- Greeting function\n- Sum function\n- Function with default arguments\n- Variable length arguments\n- Recursive factorial",
        "real_world": "Functions are used in calculators, API handlers, game logic, and reusable business operations.",
        "interview_qs": "1. What is a function?\n2. What is the difference between a parameter and an argument?\n3. What is a return value?\n4. What are default arguments?\n5. What are keyword arguments?\n6. What are variable-length arguments?\n7. What is recursion?\n8. What is the base case in recursion?\n9. Why are functions important?\n10. How does scope affect variables?",
        "practice_qs": "1. Write a function to add two numbers.\n2. Write a function to check even/odd.\n3. Write a recursive function to calculate factorial.\n4. Write a function with default parameter values.\n5. Create a function that accepts any number of arguments.\n6. Write a function to reverse a string.\n7. Use a function to calculate area of a circle.\n8. Write a function that returns the largest of three numbers.",
        "problems": "- 739. Daily Temperatures\n- 438. Find All Anagrams in a String\n- 200. Number of Islands",
        "learning_outcome": "The learner can create modular code using functions and understand recursive thinking.",
        "summary": "Day 7 focused on reusable logic, modular programming, and problem decomposition through functions.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Functions are the building blocks of organized programs. They allow a single task to be implemented once and used at multiple locations. Good function design improves clarity and reduces duplication. In interviews, function-based questions often test parameter passing, return behavior, and the ability to break a problem into manageable parts.",
        "examples_code": "def greet(name):\n    return f'Hello {name}'\n\nprint(greet('Neha'))\n\ndef add(a, b=5):\n    return a + b\n\nprint(add(3))\n\ndef show(*args):\n    print(args)\n\nshow(1, 2, 3)\n\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))\n"
    },
    {
        "day_num": 8,
        "title": "Lambda, Map, Filter, Reduce and Modules",
        "date": "13-07-2026",
        "topics": "Lambda, Map, Filter, Reduce, Modules, Packages, Scope, Global, Local, Built-in Modules",
        "theory": "Lambda functions provide concise anonymous functions. map(), filter(), and reduce() are functional tools that process collections elegantly. Modules and packages help organize related code and make Python extensible. Scope determines the accessibility of variables in different parts of a program.",
        "key_concepts": "Lambda expressions are compact. map transforms items, filter selects items, and reduce combines values. Global and local scope affect where variables can be accessed.",
        "advantages": "Shorter code, expressive transformations, and modular design.",
        "features": "Anonymous functions, collection processing, reusable modules, and lexical scoping.",
        "syntax": "```python\nresult = list(map(lambda x: x * 2, [1, 2, 3]))\nprint(result)\n```",
        "examples": "- Lambda for squaring numbers\n- map() for transformation\n- filter() for selection\n- reduce() for accumulation\n- import math and random",
        "real_world": "These concepts are used in data transformation, analytics pipelines, and compact code writing.",
        "interview_qs": "1. What is a lambda function?\n2. What is the difference between map and filter?\n3. What does reduce do?\n4. What is a module?\n5. What is a package?\n6. What is local scope?\n7. What is global scope?\n8. Why are modules helpful?\n9. What is the purpose of import math?\n10. How do you avoid naming conflicts in modules?",
        "practice_qs": "1. Use lambda to square numbers.\n2. Use map to double each item in a list.\n3. Use filter to select even numbers.\n4. Import the math module and use sqrt().\n5. Import random and generate a random number.\n6. Write a small module and import it.\n7. Demonstrate global and local scope.\n8. Use reduce to find the sum of a list.",
        "problems": "- Two Sum\n- Group Anagrams\n- Valid Parentheses\n- Valid Anagram\n- Contains Duplicate II\n- Roman to Integer\n- Longest Common Prefix",
        "learning_outcome": "The learner can write concise functional code and use Python’s built-in libraries effectively.",
        "summary": "Day 8 introduced functional programming patterns and modular coding practices that make Python efficient and expressive.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Functional tools such as lambda and map make code concise when performing simple transformations. Modules and packages allow code to be organized into meaningful units, which is important in larger projects. Scope rules explain how variables behave depending on where they are defined, and this knowledge becomes essential when debugging complex programs.",
        "examples_code": "from functools import reduce\nimport math\nimport random\n\nnums = [1, 2, 3, 4]\nprint(list(map(lambda x: x * 2, nums)))\nprint(list(filter(lambda x: x % 2 == 0, nums)))\nprint(reduce(lambda a, b: a + b, nums))\nprint(math.sqrt(16))\nprint(random.randint(1, 10))\n"
    },
    {
        "day_num": 9,
        "title": "File Handling",
        "date": "14-07-2026",
        "topics": "Read, Write, Append, With Statement, CSV, Text Files",
        "theory": "File handling enables Python programs to read and write data to disk. Common operations include opening a file, reading its contents, writing or appending data, and safely closing the file. The with statement ensures that system resources are released correctly. CSV and text files are frequently used for storing records and data logs.",
        "key_concepts": "Files can be opened in read, write, append, or binary modes. The with statement is preferred for safe file management. CSV files are commonly used for tabular data.",
        "advantages": "Data persistence, logging, report generation, and structured input/output.",
        "features": "read(), write(), append(), open(), and file iteration.",
        "syntax": "```python\nwith open('sample.txt', 'w') as f:\n    f.write('Hello file')\n```",
        "examples": "- Create a text file\n- Read from a file\n- Append content\n- Read CSV data\n- Mini project using files",
        "real_world": "File handling is used in loggers, report builders, inventory systems, and data export tools.",
        "interview_qs": "1. What is the difference between write and append mode?\n2. Why is the with statement used?\n3. What is a CSV file?\n4. How do you read a file line by line?\n5. What happens if a file does not exist in read mode?\n6. What is the difference between text and binary files?\n7. How do you close a file safely?\n8. What is file buffering?\n9. What is a practical use of file handling?\n10. How can you write structured data to a file?",
        "practice_qs": "1. Write a note to a text file.\n2. Read and print the contents of a file.\n3. Append a new line to an existing file.\n4. Store student names in CSV format.\n5. Create a mini diary program.\n6. Build a program that counts words in a file.\n7. Create a file organizer script.\n8. Read a CSV file and print rows.",
        "problems": "File handling practice included reading, writing, appending, and parsing structured data.",
        "learning_outcome": "The learner can manage persistent data using files and understand how to work with text and CSV formats.",
        "summary": "Day 9 introduced data persistence through file operations, which are essential in real-world software.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Working with files is a major step because it allows programs to remember data between runs. File operations are used everywhere from log generation to storing user records. The with statement is especially important because it closes the file automatically, reducing errors and improving reliability. CSV files make it easy to work with spreadsheets-like data.",
        "examples_code": "with open('notes.txt', 'w') as f:\n    f.write('Python file handling demo\\n')\n\nwith open('notes.txt', 'r') as f:\n    print(f.read())\n\nwith open('notes.txt', 'a') as f:\n    f.write('Appended line\\n')\n\n# CSV example\nimport csv\nwith open('students.csv', 'w', newline='') as f:\n    writer = csv.writer(f)\n    writer.writerow(['Name', 'Age'])\n    writer.writerow(['Asha', 21])\n"
    },
    {
        "day_num": 10,
        "title": "Exception Handling",
        "date": "15-07-2026",
        "topics": "try, except, finally, raise, Custom Exceptions",
        "theory": "Exception handling helps programs respond gracefully to runtime errors. The try block contains code that may fail, except handles the error, finally runs regardless of success, and raise allows custom exceptions to be triggered. Good error handling makes an application more reliable and user-friendly.",
        "key_concepts": "Exceptions are errors that occur during execution. They should be caught and handled instead of crashing the program. Custom exceptions help communicate business-specific issues.",
        "advantages": "Improved reliability, easier debugging, and better user experience.",
        "features": "Specific exception handling, custom exception classes, and cleanup in finally.",
        "syntax": "```python\ntry:\n    x = int('abc')\nexcept ValueError:\n    print('Invalid value')\nfinally:\n    print('Done')\n```",
        "examples": "- Handling division by zero\n- Catching invalid input\n- Custom exception example\n- Resource cleanup example\n- Raising an exception",
        "real_world": "Exception handling is used in banking apps, API clients, and payment systems to prevent crashes.",
        "interview_qs": "1. What is an exception?\n2. What is the purpose of try and except?\n3. When is finally used?\n4. What is a custom exception?\n5. What is the difference between error and exception?\n6. What is raising an exception?\n7. Why should exceptions be handled?\n8. What is the role of finally in cleanup?\n9. How do you handle multiple exceptions?\n10. What happens if an exception is not handled?",
        "practice_qs": "1. Handle division by zero gracefully.\n2. Catch invalid integer conversion.\n3. Create a custom exception for age less than 18.\n4. Write a program that always prints a cleanup message.\n5. Handle multiple exceptions in one block.\n6. Raise an exception for negative input.\n7. Build a calculator with safe error handling.\n8. Create a file reading program with exception handling.",
        "problems": "Exception handling practice focused on debugging, resilience, and user-friendly error messages.",
        "learning_outcome": "The learner can write robust programs that recover from errors gracefully.",
        "summary": "Day 10 emphasized reliability by teaching structured error handling and defensive programming.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Errors are inevitable in software development. Instead of letting the program crash, Python enables developers to manage them explicitly. Exception handling improves the quality of applications by separating normal logic from recovery logic. In interviews, this topic often appears when discussing stability, robustness, and defensive coding.",
        "examples_code": "try:\n    num = int(input('Enter a number: '))\n    print(10 / num)\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')\nexcept ValueError:\n    print('Please enter a valid number')\nfinally:\n    print('Execution completed')\n\nclass AgeError(Exception):\n    pass\n\ntry:\n    age = int(input('Enter age: '))\n    if age < 18:\n        raise AgeError('Age must be 18 or above')\nexcept AgeError as e:\n    print(e)\n"
    },
    {
        "day_num": 11,
        "title": "OOP Classes and Objects",
        "date": "16-07-2026",
        "topics": "Classes, Objects, Constructor, Inheritance, Single, Multiple, Multilevel, Hierarchical",
        "theory": "Object-Oriented Programming organizes code around classes and objects. A class is a blueprint, and an object is an instance of that class. Constructors initialize attributes, while inheritance allows one class to reuse the behavior of another. Different inheritance types enable flexible code organization for real-world models.",
        "key_concepts": "Encapsulation, inheritance, and reuse are central to OOP. Constructors define initialization behavior, and inheritance helps build specialized classes.",
        "advantages": "Code reuse, better structure, maintainability, and a closer match to real-world entities.",
        "features": "Attributes, methods, constructors, inheritance, and polymorphism.",
        "syntax": "```python\nclass Student:\n    def __init__(self, name):\n        self.name = name\n```",
        "examples": "- Student class\n- Bank account class\n- Library book class\n- Inheritance example\n- Constructor example",
        "real_world": "OOP is widely used in banking systems, e-commerce platforms, school management systems, and game development.",
        "interview_qs": "1. What is a class?\n2. What is an object?\n3. What is a constructor?\n4. What is inheritance?\n5. What is the difference between single and multiple inheritance?\n6. What is multilevel inheritance?\n7. Why is OOP useful?\n8. What is an attribute?\n9. What is a method?\n10. How does polymorphism relate to OOP?",
        "practice_qs": "1. Create a Student class.\n2. Create a BankAccount class with deposit and withdraw methods.\n3. Build a Book class for a library system.\n4. Implement single inheritance.\n5. Implement multilevel inheritance.\n6. Use a constructor to initialize values.\n7. Create a class with methods and attributes.\n8. Explain how inheritance improves code reuse.",
        "problems": "OOP practice included designing reusable class structures for real-world entities and inheritance-based extensions.",
        "learning_outcome": "The learner can model real-world entities using classes and apply inheritance to build extensible programs.",
        "summary": "Day 11 introduced object-oriented design, which is essential for building scalable and maintainable software.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "OOP helps developers represent real-world systems more naturally. Classes define the structure, while objects store actual data and behavior. Inheritance reduces duplication by allowing new classes to build on existing ones. This topic is highly relevant in interviews because many enterprise applications are written with object-oriented principles.",
        "examples_code": "class Student:\n    def __init__(self, name, grade):\n        self.name = name\n        self.grade = grade\n\n    def show(self):\n        print(self.name, self.grade)\n\nclass GraduateStudent(Student):\n    def __init__(self, name, grade, project):\n        super().__init__(name, grade)\n        self.project = project\n\nobj = GraduateStudent('Mina', 'A', 'AI')\nobj.show()\nprint(obj.project)\n"
    },
    {
        "day_num": 12,
        "title": "OOP Advanced",
        "date": "17-07-2026",
        "topics": "Encapsulation, Abstraction, Polymorphism, Method Overriding, Method Overloading Explanation",
        "theory": "Advanced OOP concepts make software design more robust and expressive. Encapsulation hides internal details and exposes only necessary interfaces. Abstraction focuses on essential behavior rather than implementation specifics. Polymorphism enables a single interface to work for multiple types, while method overriding and overloading show dynamic and static behavior in class hierarchies.",
        "key_concepts": "Encapsulation protects data, abstraction simplifies interaction, and polymorphism adds flexibility. Method overriding is the process of redefining a parent method in a child class.",
        "advantages": "Improved design quality, stronger code organization, and clearer object collaboration.",
        "features": "Private attributes, abstract methods, and dynamic dispatch.",
        "syntax": "```python\nclass Animal:\n    def speak(self):\n        pass\n```",
        "examples": "- Encapsulation example\n- Abstraction class\n- Method overriding example\n- Polymorphism example\n- Real-world design pattern",
        "real_world": "These concepts are used in frameworks, enterprise systems, UI libraries, and simulation tools.",
        "interview_qs": "1. What is encapsulation?\n2. What is abstraction?\n3. What is polymorphism?\n4. What is method overriding?\n5. What is method overloading?\n6. Why is encapsulation useful?\n7. How does polymorphism improve flexibility?\n8. What is an abstract class?\n9. What is the difference between abstraction and encapsulation?\n10. How are these concepts used in real projects?",
        "practice_qs": "1. Create a class with private attributes.\n2. Design an abstract base class.\n3. Implement method overriding.\n4. Demonstrate polymorphism using a common method.\n5. Compare encapsulation and abstraction in one paragraph.\n6. Build a shape hierarchy with overridden methods.\n7. Create a base class and two derived classes.\n8. Explain why polymorphism helps in maintenance.",
        "problems": "Advanced OOP practice included design thinking, inheritance-based behavior, and interface-oriented coding.",
        "learning_outcome": "The learner can design cleaner and more professional object-oriented systems using advanced principles.",
        "summary": "Day 12 moved beyond basic classes and explored the deeper design ideas behind robust OOP systems.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "Advanced OOP concepts are commonly tested in interviews because they reflect real engineering maturity. Encapsulation prevents accidental misuse of data, abstraction reduces complexity, and polymorphism allows code to be reused across different object types. Understanding these ideas helps developers design classes that are easier to maintain and extend.",
        "examples_code": "class BankAccount:\n    def __init__(self, balance):\n        self.__balance = balance\n\n    def deposit(self, amount):\n        self.__balance += amount\n\n    def get_balance(self):\n        return self.__balance\n\nclass Animal:\n    def speak(self):\n        print('Animal sound')\n\nclass Dog(Animal):\n    def speak(self):\n        print('Bark')\n\naccount = BankAccount(100)\naccount.deposit(50)\nprint(account.get_balance())\n\ndog = Dog()\ndog.speak()\n"
    },
    {
        "day_num": 13,
        "title": "Standard Libraries",
        "date": "18-07-2026",
        "topics": "os, sys, math, random, datetime, time, json, shutil",
        "theory": "Python’s standard library provides powerful modules for everyday programming tasks. os and shutil help with file and folder operations; sys supports runtime arguments and environment access; math and random support numerical and random operations; datetime and time manage date and time; json helps with structured data exchange.",
        "key_concepts": "Built-in modules are available without installation and help developers solve common problems quickly. They are especially useful for automation and scripting.",
        "advantages": "Fast development, reliability, and strong support for common tasks.",
        "features": "Automation, file operations, date handling, random generation, and JSON serialization.",
        "syntax": "```python\nimport os\nprint(os.getcwd())\n```",
        "examples": "- File organizer script\n- Rename files\n- Random password generator\n- Folder cleaner\n- JSON saving and loading",
        "real_world": "Standard libraries are used in automation scripts, configuration managers, backup tools, and analytics workflows.",
        "interview_qs": "1. What is the standard library?\n2. What is the os module used for?\n3. What is the json module useful for?\n4. How is random used?\n5. What is datetime used for?\n6. What does shutil help with?\n7. Why are built-in modules important?\n8. What is the difference between os and shutil?\n9. How do you read command-line arguments with sys?\n10. How can Python automate repetitive tasks?",
        "practice_qs": "1. List files in a folder using os.\n2. Rename a file using os.\n3. Generate a random password.\n4. Print the current date and time.\n5. Convert a Python dictionary to JSON.\n6. Clean a folder of temporary files.\n7. Create a file organizer script.\n8. Use math to calculate the square root of a number.",
        "problems": "Standard library exercises included automation tasks, file operations, and utility scripting.",
        "learning_outcome": "The learner can use Python’s built-in modules to automate tasks and solve everyday problems efficiently.",
        "summary": "Day 13 introduced the standard library, which makes Python practical for automation and productivity tasks.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "The standard library is one of Python’s strongest advantages. It includes many modules that cover everything from file operations to networking and data handling. By using these modules, developers can finish practical tasks quickly without depending on third-party packages. This is particularly important for beginners who are learning to build real solutions early.",
        "examples_code": "import os\nimport json\nimport random\nfrom datetime import datetime\n\nprint(os.getcwd())\nprint(datetime.now())\n\npassword = ''.join(random.choice('abc123') for _ in range(8))\nprint(password)\n\nstudent = {'name': 'Asha', 'age': 21}\nprint(json.dumps(student))\n"
    },
    {
        "day_num": 14,
        "title": "SQLite Database",
        "date": "19-07-2026",
        "topics": "Create Database, Create Table, Insert, Update, Delete, Select, WHERE, ORDER BY, GROUP BY, JOIN",
        "theory": "SQLite is a lightweight database engine that is easy to use in Python. It allows developers to create databases and tables, store records, and query data efficiently. SQLite is especially useful for desktop applications, small web apps, and prototypes. SQL clauses such as WHERE, ORDER BY, GROUP BY, and JOIN help retrieve meaningful information.",
        "key_concepts": "A database stores structured data. Tables define the schema, and SQL commands manage records. Joining tables helps combine related data.",
        "advantages": "Lightweight, serverless, easy to set up, and ideal for beginner database projects.",
        "features": "Persistent storage, SQL queries, relational modeling, and straightforward integration with Python.",
        "syntax": "```python\nimport sqlite3\nconn = sqlite3.connect('students.db')\n```",
        "examples": "- Create a student database\n- Create a table\n- Insert a row\n- Update a record\n- Query records",
        "real_world": "SQLite is used in mobile apps, desktop applications, analytics prototypes, and local storage systems.",
        "interview_qs": "1. What is SQLite?\n2. What is the difference between SQL and SQLite?\n3. How do you create a table?\n4. What is the purpose of WHERE?\n5. What is the difference between UPDATE and DELETE?\n6. What is a JOIN?\n7. Why is ORDER BY used?\n8. What is GROUP BY?\n9. How do you connect Python to SQLite?\n10. What is a database schema?",
        "practice_qs": "1. Create a database for students.\n2. Create a table with student information.\n3. Insert three student records.\n4. Update one student's grade.\n5. Delete one record.\n6. Select all students.\n7. Filter students by age.\n8. Use ORDER BY and GROUP BY in queries.",
        "problems": "Database practice included CRUD logic, table design, and basic SQL query building.",
        "learning_outcome": "The learner can create and interact with a lightweight relational database using Python and SQLite.",
        "summary": "Day 14 introduced database programming and SQL fundamentals through SQLite.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "SQLite is an excellent starting point for learning database concepts because it is lightweight and does not require a separate server. Structured data can be stored in tables, and SQL queries help retrieve specific records. Understanding joins and grouping is essential for modeling more complex systems later.",
        "examples_code": "import sqlite3\n\nconn = sqlite3.connect('students.db')\ncur = conn.cursor()\ncur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)')\ncur.execute('INSERT INTO students (name, marks) VALUES (\\'Asha\\', 90)')\nconn.commit()\ncur.execute('SELECT * FROM students')\nprint(cur.fetchall())\nconn.close()\n"
    },
    {
        "day_num": 15,
        "title": "CRUD Operations",
        "date": "20-07-2026",
        "topics": "Student Database Project, Employee Database Project, Library Database Project, Expense Tracker, SQL Interview Questions",
        "theory": "CRUD stands for Create, Read, Update, and Delete. These four operations form the foundation of most database-driven applications. A well-built CRUD system allows users to manage information through forms, scripts, or command-line programs. This day focused on implementing CRUD patterns for realistic use cases such as students, employees, books, and expenses.",
        "key_concepts": "Create inserts data, Read fetches it, Update modifies it, and Delete removes it. A practical CRUD flow is central to business applications.",
        "advantages": "Standardized data handling, easier maintenance, and strong relevance to real software systems.",
        "features": "Menu-based operations, persistent storage, input validation, and query execution.",
        "syntax": "```python\ncur.execute('INSERT INTO students (name) VALUES (?)', ('Ravi',))\n```",
        "examples": "- Student CRUD menu\n- Employee record manager\n- Library records\n- Expense tracker\n- SQL interview questions",
        "real_world": "CRUD systems power HR tools, school portals, inventory systems, and account management dashboards.",
        "interview_qs": "1. What is CRUD?\n2. What is the difference between INSERT and UPDATE?\n3. What is the role of a primary key?\n4. Why are SQL queries important?\n5. How do you delete a record safely?\n6. How do you filter records by a condition?\n7. What is a database transaction?\n8. What is the role of a foreign key?\n9. Why is validation important in CRUD?\n10. What is the difference between a database and a table?",
        "practice_qs": "1. Create a student CRUD program.\n2. Build an employee CRUD program.\n3. Create a library catalog manager.\n4. Build an expense tracker with storage.\n5. Practice SQL interview questions.\n6. Add search functionality to a database app.\n7. Implement delete confirmation.\n8. Use a menu-driven interface for CRUD operations.",
        "problems": "CRUD tasks included building complete database applications with insertion, retrieval, updates, and deletion flow.",
        "learning_outcome": "The learner can design and implement practical database applications using Python and SQL.",
        "summary": "Day 15 connected database concepts with real product thinking by implementing CRUD-based projects.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "CRUD is one of the most important concepts in application development. Almost every software system stores data and needs ways to create, access, modify, and delete it. In this day, the focus shifted from isolated SQL statements to full workflows that resemble real applications. This is where theory becomes practical and interview readiness becomes stronger.",
        "examples_code": "import sqlite3\n\nconn = sqlite3.connect('students.db')\ncur = conn.cursor()\ncur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)')\n\n# Create\ncur.execute('INSERT INTO students (name, marks) VALUES (\\'Ravi\\', 88)')\nconn.commit()\n\n# Read\ncur.execute('SELECT * FROM students')\nprint(cur.fetchall())\n\n# Update\ncur.execute('UPDATE students SET marks = 92 WHERE name = \\'Ravi\\'')\nconn.commit()\n\n# Delete\ncur.execute('DELETE FROM students WHERE name = \\'Ravi\\'')\nconn.commit()\nconn.close()\n"
    },
    {
        "day_num": 16,
        "title": "Current Progress",
        "date": "21-07-2026",
        "topics": "Placement Training Status, MCQ Tests, AI Digital Twin Project, Viva, PPT Submission",
        "theory": "This day reviews the overall progress made so far in training. It highlights daily consistency, academic scoring, project development, and professional communication. It also reflects the balance between learning, practice, and documentation that is essential for placement preparation.",
        "key_concepts": "Progress tracking, project documentation, and continuous learning are key to sustained growth. The training status shows both technical and communication readiness.",
        "advantages": "Clear visibility of improvements, stronger portfolio building, and better preparation for interviews.",
        "features": "Training summary, test results, project overview, future tasks, and milestone tracking.",
        "syntax": "```text\nStatus: Ongoing\nTraining Started: 06 July 2026\nCurrent Focus: Python, SQL, DSA, and Projects\n```",
        "examples": "- Progress summary\n- MCQ score review\n- Project milestone checklist\n- Viva preparation notes\n- Future roadmap",
        "real_world": "Progress tracking is vital in education, internships, and job readiness. It helps candidates communicate achievements clearly.",
        "interview_qs": "1. What is your current training status?\n2. What projects are you working on?\n3. What were your MCQ test scores?\n4. What is your future learning plan?\n5. How did you document your progress?\n6. What is your strongest topic so far?\n7. What is your current challenge?\n8. Why is documentation important?\n9. How did Viva experiences improve your confidence?\n10. What are you preparing next?",
        "practice_qs": "1. Prepare a personal progress report.\n2. Summarize your learning journey in a paragraph.\n3. Create a roadmap for the next month.\n4. Write a short project description.\n5. Prepare 5 interview talking points.\n6. Review your strongest and weakest topics.\n7. Make a weekly study plan.\n8. Draft a professional GitHub portfolio summary.",
        "problems": "Current progress focused on portfolio building, documentation quality, and reflection on practical growth.",
        "learning_outcome": "The learner understands the importance of tracking progress and presenting technical growth professionally.",
        "summary": "Day 16 consolidated the training journey and highlighted readiness for placement interviews and project discussions.",
        "files_included": "README.md, Notes.md, interview_questions.md, practice_questions.md, examples.py",
        "notes_content": "This stage is not just about learning concepts; it is about demonstrating growth. A strong portfolio shows activity, reflection, and consistency. In interviews, candidates are often judged not only on technical knowledge but also on how clearly they explain what they have built and how they have improved over time.",
        "examples_code": "training_started = '06 July 2026'\nstatus = 'Ongoing'\nscore_1 = '24/25'\nscore_2 = '24/25'\nscore_3 = '24/25'\n\nprint('Training started on:', training_started)\nprint('Status:', status)\nprint('MCQ scores:', score_1, score_2, score_3)\n"
    },
]

for spec in day_specs:
    title = spec['title'].replace(' ', '_').replace('/', '_')
    day_files(spec['day_num'], title, spec['date'], spec['topics'], spec['theory'], spec['key_concepts'], spec['advantages'], spec['features'], spec['syntax'], spec['examples'], spec['real_world'], spec['interview_qs'], spec['practice_qs'], spec['problems'], spec['learning_outcome'], spec['summary'], spec['files_included'], spec['notes_content'], spec['examples_code'])

print('Repository generated successfully.')
