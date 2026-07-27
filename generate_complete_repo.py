from pathlib import Path
import textwrap

ROOT = Path(r"c:\Users\Kiran Kumar\OneDrive\Desktop\python-placement-training-2026")
ROOT.mkdir(parents=True, exist_ok=True)


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def build_day(day_num, folder_name, title, date, topics, theory_notes, key_concepts, advantages, features, syntax, python_examples, real_time_examples, interview_questions, practice_questions, leetcode_problems, learning_outcome, summary, notes_content, python_code):
    folder = ROOT / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    readme = f"""# Day {day_num}: {title}

## Date
{date}

## Topics Covered
{topics}

## Theory Notes
{theory_notes}

## Key Concepts
{key_concepts}

## Advantages
{advantages}

## Features
{features}

## Syntax
```python
{syntax}
```

## Python Examples
{python_examples}

## Real-Time Examples
{real_time_examples}

## Interview Questions
{interview_questions}

## LeetCode Problems Practiced
{leetcode_problems}

## Learning Outcome
{learning_outcome}

## Summary
{summary}

## Files Included
- README.md
- Notes.md
- interview_questions.md
- practice_questions.md
- leetcode.md
- examples.py
"""
    write(folder / "README.md", readme)
    write(folder / "Notes.md", f"""# Notes for Day {day_num}: {title}

{notes_content}
""")
    write(folder / "interview_questions.md", f"""# Interview Questions - Day {day_num}

{interview_questions}
""")
    write(folder / "practice_questions.md", f"""# Practice Questions - Day {day_num}

{practice_questions}
""")
    write(folder / "leetcode.md", f"""# LeetCode Practice - Day {day_num}

## Problems Covered
{leetcode_problems}

## Practice Notes
Each problem was solved with a focus on understanding the core pattern, writing clear logic, and explaining the approach in simple terms.
""")
    write(folder / "examples.py", python_code)


root_readme = """# Python Placement Training 2026

![Python Banner](https://img.shields.io/badge/Python-Placement%20Training-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?style=for-the-badge&logo=github)
![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)

This repository documents my complete placement preparation journey in Python during 2026. It combines daily theory notes, hands-on practice, interview preparation, LeetCode learning, and project progress in a recruiter-friendly format.

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
This portfolio shows consistency, discipline, and technical growth. Each day includes structured notes, practical examples, interview questions, and coding preparation that can be discussed confidently in placement interviews.

## Training Timeline
- 06 July 2026 - Training Started
- 10 July 2026 - MCQ Test 1
- 17 July 2026 - MCQ Test 2
- 24 July 2026 - MCQ Test 3
- Ongoing - Daily Python practice and interview preparation

## Skills Learned
- Python Basics and Syntax
- Variables, Data Types, and Operators
- Conditional Statements and Loops
- Lists, Tuples, Sets, and Dictionaries
- Functions, Lambda, and Modules
- File Handling and Exception Handling
- OOP Concepts and Advanced Design
- SQLite and CRUD Database Applications
- Automation and project documentation

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
- Arrays, strings, hashing, sorting, and recursion practiced across multiple days
- Focus on understanding patterns and writing clean explanations
- Goal: improve clarity, speed, and confidence for interviews

## MCQ Test Scores
| Date | Score |
|---|---:|
| 10 July 2026 | 24/25 |
| 17 July 2026 | 24/25 |
| 24 July 2026 | 24/25 |

## Project Section
- [AI-Digital-Twin-Project](AI-Digital-Twin-Project/README.md)
- [MCQ Tests](MCQ-Tests/README.md)

## Future Learning Goals
- Strengthen DSA and coding speed
- Build more end-to-end Python projects
- Prepare for company-specific interview rounds
- Improve communication and explanation quality

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

write(ROOT / "MCQ-Tests" / "README.md", """# MCQ Tests

## Test History
- 10 July 2026 - Score: 24/25
- 17 July 2026 - Score: 24/25
- 24 July 2026 - Score: 24/25

## Observations
These tests strengthened conceptual clarity and interview readiness.
""")

write(ROOT / "AI-Digital-Twin-Project" / "README.md", """# AI Digital Twin for Personalized Student Learning

## Overview
This project focuses on building a digital twin platform that can recommend learning paths and adaptively guide students.

## Objectives
- Personalize learning experiences
- Track student progress
- Recommend practice activities
- Improve retention and performance

## Technology Stack
- Python
- SQLite
- Markdown
- GitHub
- Future web/API extensions

## Current Progress
- Project idea finalized
- Architecture discussed
- Documentation started
- Viva 1 completed
- Viva 2 completed
- PPT submitted
""")

write(ROOT / "Database_Task.md", """# Database Task

This file summarizes the database practice completed during Day 14 and Day 15.

## Topics Covered
- SQLite database creation
- Table design
- CRUD operations
- Student, employee, and library data handling

## Outcome
The repository now includes practical examples for database creation, insertion, updates, deletion, and querying.
""")


# Day metadata

days = [
    {
        "folder": "Day-01_Python_Introduction",
        "day": 1,
        "title": "Python Introduction",
        "date": "06-07-2026",
        "topics": "What is Python, History of Python, Advantages, Features, Applications, Python Libraries, OOP Concepts, Python Installation, Python Execution Flow, Difference between Compiler and Interpreter",
        "theory": "Python is a high-level, interpreted language that emphasizes simplicity and readability. It became popular because it allows both beginners and professionals to build working solutions quickly. The execution flow begins with writing source code, which is converted into bytecode and then executed by the Python virtual machine. Python is widely used in automation, web development, data science, and artificial intelligence.",
        "key_concepts": "Python is beginner-friendly, uses indentation for structure, supports multiple programming paradigms, and runs through an interpreter. A compiler translates the entire program before execution, while an interpreter executes it step by step.",
        "advantages": "Easy syntax, large community, strong libraries, cross-platform support, and quick development.",
        "features": "Readable syntax, dynamic typing, built-in data structures, object-oriented support, and rich libraries.",
        "syntax": "print('Hello, World!')\nname = 'Alex'\nprint(name)",
        "python_examples": "- Hello World program\n- Input and output example\n- Arithmetic expression example\n- Variable demonstration\n- Comment usage",
        "real_time_examples": "Python is used in automation scripts, classroom management systems, web applications, and AI tools.",
        "interview_questions": "1. What is Python?\n2. Why is Python popular?\n3. What is the difference between a compiler and an interpreter?\n4. What are Python libraries?\n5. What is the purpose of indentation in Python?\n6. What are common applications of Python?\n7. What makes Python beginner-friendly?\n8. What is the role of the Python interpreter?\n9. What is OOP in Python?\n10. What does PEP 8 mean?\n11. What is a REPL?\n12. How does Python differ from Java?\n13. What is the role of Python in AI?\n14. What are built-in functions?\n15. Why is Python cross-platform?",
        "practice_questions": "1. Write a program to print your name.\n2. Write a program to add two numbers.\n3. Write a program to greet a user.\n4. Explain the difference between compiler and interpreter.\n5. Install Python and check the version.\n6. Create a simple program that prints your favorite hobby.\n7. Write comments in your code to explain each step.\n8. Print a sentence using input from the user.",
        "leetcode_problems": "No official LeetCode problem assigned today. Focus was on Python basics and coding mindset.",
        "learning_outcome": "The learner understands the role of Python, its execution model, and the reasons it is used across industries.",
        "summary": "Day 1 introduced Python as a beginner-friendly language and built the conceptual base for later topics.",
        "notes_content": "Python is known for readability and simplicity. It uses indentation instead of braces for structure, making the code look neat and easy to follow. Understanding the execution flow helps learners connect code writing with runtime behavior. This day also introduced the value of Python in real-world applications such as automation and AI.",
        "python_code": "print('Hello, World!')\nprint('Welcome to Python Placement Training')\n\nname = input('Enter your name: ')\nprint('Hello', name)\n\nnum1 = 10\nnum2 = 20\nprint('Sum:', num1 + num2)\n"
    },
    {
        "folder": "Day-02_Variables_DataTypes",
        "day": 2,
        "title": "Variables and Data Types",
        "date": "07-07-2026",
        "topics": "Variables, Identifiers, Keywords, Data Types, Input Output, Type Conversion, Operators Introduction",
        "theory": "Variables are used to store information that a program needs during execution. Identifiers are the names assigned to variables and functions, while keywords are reserved words in Python. Data types explain what kind of value a variable holds, such as integer, float, string, or boolean. Type conversion helps adapt values to a required format.",
        "key_concepts": "Use descriptive identifiers, understand Python keywords, choose the right data type, and practice input-output flow. Operators help perform calculations and comparisons.",
        "advantages": "Improved readability, flexibility in handling values, and strong support for user interaction.",
        "features": "Dynamic typing, built-in data types, input() and print(), and conversion functions like int() and str().",
        "syntax": "name = 'Riya'\nage = 21\nprint(name, age)\nvalue = int(input('Enter number: '))",
        "python_examples": "- Store a name and age in variables\n- Convert string input to integer\n- Perform arithmetic operations\n- Demonstrate boolean values\n- Print data type of a variable",
        "real_time_examples": "Variables and types are used in calculators, forms, user profiles, and any application that stores data.",
        "interview_questions": "1. What is a variable?\n2. What is an identifier?\n3. What are keywords?\n4. What is dynamic typing?\n5. What is type conversion?\n6. What is the difference between int and float?\n7. What does input() return?\n8. What is a string in Python?\n9. What is the difference between = and ==?\n10. Why are data types important?",
        "practice_questions": "1. Create variables for name, age, and city.\n2. Convert a string input into an integer.\n3. Write a program that swaps two numbers.\n4. Find the area of a rectangle using variables.\n5. Write a program to calculate simple interest.\n6. Print the type of a value.\n7. Use arithmetic operators.\n8. Accept a number and check if it is even or odd.",
        "leetcode_problems": "- Fizz Buzz\n- Palindrome Number\n- Reverse Integer\n- Plus One\n- Length of Last Word\n- Valid Palindrome\n- To Lower Case\n- Reverse String",
        "learning_outcome": "The learner can declare variables, use basic data types, convert values, and work with input-output operations confidently.",
        "summary": "Day 2 introduced foundational programming concepts through variables, data types, and type conversion.",
        "notes_content": "A variable is a named reference to data stored in memory. Understanding identifiers and keywords helps prevent syntax and naming errors. Python’s dynamic typing makes code simpler, but it also requires careful attention to data types. Type conversion becomes especially important when reading input from the user or processing values from external systems.",
        "python_code": "name = 'Riya'\nage = 22\nprint('Name:', name)\nprint('Age:', age)\n\nnum = int(input('Enter a number: '))\nprint('Square:', num * num)\n\nvalue = '100'\nprint(int(value) + 5)\n"
    },
    {
        "folder": "Day-03_Conditional_Statements",
        "day": 3,
        "title": "Conditional Statements",
        "date": "08-07-2026",
        "topics": "if, if else, Nested if, elif, Operators, Comparison, Logical, Assignment, Identity, Membership, Bitwise",
        "theory": "Conditional statements help the program choose between different actions based on a condition. They are the basis of decision-making logic. The if, elif, and else keywords allow programs to branch logically. Python also supports operators that make conditions more expressive and powerful.",
        "key_concepts": "Decision-making is driven by conditions that evaluate to True or False. Indentation is essential because it groups the statements that belong to each conditional block.",
        "advantages": "Programs become interactive and can respond to user input, validations, and changing conditions.",
        "features": "Comparison operators, logical operators, nested conditions, and clean branch structure.",
        "syntax": "age = 18\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
        "python_examples": "- Voting eligibility check\n- Grade classification\n- Login validation\n- Nested if example\n- Multiple condition example",
        "real_time_examples": "Conditionals are used in admission systems, payment approvals, password checks, and game logic.",
        "interview_questions": "1. What is the difference between if and elif?\n2. What is a nested if?\n3. Why is indentation important in conditionals?\n4. What are comparison operators?\n5. What are logical operators?\n6. What is the difference between is and ==?\n7. What are membership operators?\n8. Why are bitwise operators used?\n9. How do you handle multiple conditions?\n10. What is a Boolean expression?",
        "practice_questions": "1. Check whether a number is positive or negative.\n2. Classify marks into grades.\n3. Validate a password length.\n4. Determine the largest of three numbers.\n5. Check whether a year is a leap year.\n6. Build a menu-based calculator.\n7. Apply nested conditions for age categories.\n8. Test if an element exists in a list.",
        "leetcode_problems": "- Integer to Roman\n- Jump Game\n- Gas Station\n- Spiral Matrix\n- Set Matrix Zeroes\n- Container With Most Water\n- 3Sum\n- Rotate Image",
        "learning_outcome": "The learner can write decision-based code and understand how conditions affect program flow.",
        "summary": "Day 3 focused on controlling program flow through logical decision-making.",
        "notes_content": "Conditionals help the program behave differently depending on the state of the data. They are essential in real code because they represent business rules, user decisions, and validation checks. Good condition design is often about deciding which branch should be executed and how to keep the logic readable.",
        "python_code": "age = 20\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')\n\nmarks = 82\nif marks >= 90:\n    grade = 'A'\nelif marks >= 75:\n    grade = 'B'\nelse:\n    grade = 'C'\nprint('Grade:', grade)\n"
    },
    {
        "folder": "Day-04_Loops",
        "day": 4,
        "title": "Loops",
        "date": "09-07-2026",
        "topics": "for, while, Nested Loops, break, continue, pass, Real-Time Loop Applications",
        "theory": "Loops allow repeated execution of code. The for loop is ideal when iterating over a known range or collection, while the while loop continues until a condition becomes false. break stops the loop early, continue skips the current iteration, and pass acts as a placeholder.",
        "key_concepts": "Loops reduce repetition and help process large amounts of data. Careful loop control prevents infinite loops and improves reliability.",
        "advantages": "Cleaner code, efficient repetition, and easier handling of collections.",
        "features": "Range-based iteration, condition-based execution, nested loops, and loop control statements.",
        "syntax": "for i in range(5):\n    print(i)\n\ncount = 1\nwhile count <= 3:\n    print(count)\n    count += 1",
        "python_examples": "- Print numbers from 1 to 10\n- Sum numbers using loops\n- Print a pattern\n- Find prime numbers\n- Reverse a string using loops",
        "real_time_examples": "Loops are used in dashboards, report generation, file scanning, and automated tasks.",
        "interview_questions": "1. What is the difference between for and while?\n2. What does break do?\n3. What does continue do?\n4. What is pass used for?\n5. What is a nested loop?\n6. What is an infinite loop?\n7. How do loops help in data processing?\n8. What is a range in Python?\n9. Can loops work with strings?\n10. Why is loop control important?",
        "practice_questions": "1. Print numbers from 1 to 20.\n2. Print even numbers up to 50.\n3. Calculate the sum from 1 to 100.\n4. Find the factorial of a number.\n5. Check if a number is prime.\n6. Print a star pattern.\n7. Reverse a string using a loop.\n8. Count vowels in a word.\n9. Print the multiplication table.\n10. Create a countdown program.",
        "leetcode_problems": "Loop-based practice included pattern generation, number analysis, and iteration-based problem solving.",
        "learning_outcome": "The learner can write iterative code and control loop execution with confidence.",
        "summary": "Day 4 strengthened problem-solving by teaching structured iteration and loop control.",
        "notes_content": "Loops are one of the most common constructs in programming because they automate repetitive tasks. They are especially useful when the number of iterations depends on data or user input. Understanding how loops terminate is important, as this prevents accidental infinite execution and keeps the program predictable.",
        "python_code": "for i in range(1, 6):\n    print(i)\n\ncount = 1\nwhile count <= 5:\n    print('Count:', count)\n    count += 1\n\nfor i in range(1, 4):\n    for j in range(1, 4):\n        print(i, j)\n"
    },
    {
        "folder": "Day-05_List_Tuple",
        "day": 5,
        "title": "Lists and Tuples",
        "date": "10-07-2026",
        "topics": "Lists, Tuples, Operations, Methods, Advantages, Differences, Mutability",
        "theory": "Lists and tuples are sequence data structures in Python. Lists are mutable and can be changed after creation, while tuples are immutable and preserve fixed values. Both support indexing, slicing, and iteration, making them useful for storing groups of values.",
        "key_concepts": "Lists support dynamic changes; tuples offer reliability and safety. Mutability affects how data can be modified after creation.",
        "advantages": "Lists provide flexibility, while tuples are reliable for fixed data collections.",
        "features": "Indexing, slicing, methods like append() and remove(), and support for repeated operations.",
        "syntax": "fruits = ['apple', 'banana']\nfruits.append('mango')\npoint = (10, 20)",
        "python_examples": "- Create and print a list\n- Append values to a list\n- Remove items from a list\n- Access tuple elements\n- Sort list values",
        "real_time_examples": "Sequences are used in shopping carts, student records, task lists, and contact managers.",
        "interview_questions": "1. What is the difference between a list and a tuple?\n2. What is mutability?\n3. What are common list methods?\n4. What is indexing?\n5. What is slicing?\n6. Why might you choose a tuple over a list?\n7. Can a list contain mixed data types?\n8. What is a nested list?\n9. How do you remove an element from a list?\n10. What is the benefit of using tuples for fixed data?",
        "practice_questions": "1. Create a list of five fruits.\n2. Add a new fruit to the list.\n3. Remove a fruit.\n4. Sort the list.\n5. Reverse the list.\n6. Create a tuple of coordinates.\n7. Access the last tuple element.\n8. Find the sum of numeric values in a list.",
        "leetcode_problems": "- Replace Elements with Greatest Element on Right Side\n- Squares of Sorted Array\n- Height Checker\n- Best Time to Buy and Sell Stock\n- Transpose Matrix\n- Sort Array by Parity",
        "learning_outcome": "The learner can manipulate sequences and choose between mutable and immutable collections appropriately.",
        "summary": "Day 5 built a strong foundation in Python sequences and collection handling.",
        "notes_content": "Lists and tuples are among the most commonly used Python data structures. Lists are suitable when data will change often, while tuples are ideal for read-only information. Learning how to traverse and modify these structures is crucial for solving real coding problems efficiently.",
        "python_code": "numbers = [1, 2, 3, 4]\nnumbers.append(5)\nprint(numbers)\n\nfruits = ['apple', 'banana']\nfruits.remove('banana')\nprint(fruits)\n\npoint = (10, 20)\nprint(point[0])\n"
    },
    {
        "folder": "Day-06_Sets_Dictionaries",
        "day": 6,
        "title": "Sets and Dictionaries",
        "date": "11-07-2026",
        "topics": "Sets, Dictionary, Dictionary Methods, Set Operations, List Comprehension, Nested Comprehension",
        "theory": "Sets store unique values and are useful for membership checks and duplicate removal. Dictionaries store data as key-value pairs, which makes them ideal for mapping and lookup-based tasks. Comprehensions provide a concise way to build such structures.",
        "key_concepts": "Use sets for uniqueness and dictionaries for fast lookups. Comprehensions help write short and readable code.",
        "advantages": "Fast lookup, easy duplicate handling, and compact collection creation.",
        "features": "Union, intersection, difference, add, remove, update, and dictionary methods like get() and items().",
        "syntax": "nums = {1, 2, 3}\nstudent = {'name': 'Asha', 'age': 21}\nprint(student['name'])",
        "python_examples": "- Create a set\n- Remove duplicates from a list\n- Build a dictionary\n- Use dictionary methods\n- Create a list comprehension",
        "real_time_examples": "These structures are used in search engines, configuration files, analytics, and data cleaning tasks.",
        "interview_questions": "1. What is a set?\n2. What is a dictionary?\n3. What is the difference between a list and a set?\n4. What is a comprehension?\n5. What is the role of keys in a dictionary?\n6. What is the difference between add() and update()?\n7. What does items() return?\n8. How do you remove duplicates from data?\n9. Why is a dictionary useful for lookup?\n10. What is a nested dictionary?",
        "practice_questions": "1. Create a set of five numbers.\n2. Remove duplicates from a list using a set.\n3. Create a dictionary of student marks.\n4. Update a dictionary value.\n5. Use set intersection.\n6. Write list comprehension for squares.\n7. Create a nested dictionary.\n8. Print all keys and values from a dictionary.",
        "leetcode_problems": "- 217. Contains Duplicate\n- 1748. Sum of Unique Elements\n- 387. First Unique Character in a String\n- 389. Find the Difference",
        "learning_outcome": "The learner can work with mappings and unique collections and use comprehensions to write concise code.",
        "summary": "Day 6 introduced collections designed for uniqueness, lookup, and concise processing.",
        "notes_content": "Sets and dictionaries are important when data needs to be summarized or looked up quickly. Sets automatically remove duplicates, which makes them ideal for data cleaning. Dictionaries are especially powerful for representing structured records and real-world information in a readable way.",
        "python_code": "nums = [1, 2, 2, 3, 4, 4]\nunique_nums = set(nums)\nprint(unique_nums)\n\nstudent = {'name': 'Asha', 'age': 21}\nstudent['city'] = 'Bengaluru'\nprint(student)\n\nsquares = [x * x for x in range(5)]\nprint(squares)\n"
    },
    {
        "folder": "Day-07_Functions",
        "day": 7,
        "title": "Functions",
        "date": "12-07-2026",
        "topics": "Functions, Parameters, Arguments, Return, Default Arguments, Keyword Arguments, Variable Length Arguments, Recursion",
        "theory": "Functions are reusable blocks of code that perform one specific task. They improve clarity and reduce repetition. Parameters and arguments allow data to enter the function, while return values send results back to the caller. Recursion is a technique in which a function calls itself with a smaller input.",
        "key_concepts": "Functions make programs modular and easier to maintain. Recursion is powerful but should have a clear base case.",
        "advantages": "Better readability, code reuse, easier debugging, and structured design.",
        "features": "Parameters, return values, default arguments, keyword arguments, variable-length arguments, and recursion.",
        "syntax": "def add(a, b):\n    return a + b\n\nprint(add(2, 3))",
        "python_examples": "- Greeting function\n- Sum function\n- Function with default arguments\n- Variable-length arguments\n- Recursive factorial",
        "real_time_examples": "Functions are central to calculators, API handlers, business rules, and reusable component libraries.",
        "interview_questions": "1. What is a function?\n2. What is the difference between a parameter and an argument?\n3. What is a return value?\n4. What are default arguments?\n5. What are keyword arguments?\n6. What is recursion?\n7. What is a base case?\n8. Why are functions important in programs?\n9. What is the difference between local and global variables?\n10. How do functions improve debugging?",
        "practice_questions": "1. Write a function to add two numbers.\n2. Write a function to check even or odd.\n3. Write a recursive function for factorial.\n4. Write a function with default parameters.\n5. Create a function that accepts any number of arguments.\n6. Write a function to reverse a string.\n7. Create a function to calculate the area of a circle.\n8. Write a function to return the largest of three numbers.",
        "leetcode_problems": "- 739. Daily Temperatures\n- 438. Find All Anagrams in a String\n- 200. Number of Islands",
        "learning_outcome": "The learner can decompose tasks into smaller functions and use recursion for elegant solutions.",
        "summary": "Day 7 focused on modular programming and function-based problem-solving.",
        "notes_content": "Functions help organize code into meaningful pieces. A program with many repeated blocks becomes easier to understand when common logic is moved into a function. In interviews, function-based problems often examine whether a candidate can break a larger problem into smaller, testable steps.",
        "python_code": "def greet(name):\n    return f'Hello {name}'\n\nprint(greet('Neha'))\n\ndef add(a, b=5):\n    return a + b\n\nprint(add(3))\n\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))\n"
    },
    {
        "folder": "Day-08_Lambda_Modules",
        "day": 8,
        "title": "Lambda, Map, Filter, Reduce and Modules",
        "date": "13-07-2026",
        "topics": "Lambda, Map, Filter, Reduce, Modules, Packages, Scope, Global, Local, Built-in Modules",
        "theory": "Lambda functions provide compact anonymous functions. Tools like map(), filter(), and reduce() help process collections in a clear and concise way. Modules and packages allow code to be organized and reused. The scope of variables determines where they can be accessed.",
        "key_concepts": "Lambda expressions are useful for short transformations. Scope defines visibility of variables, and modules bring reusable functionality into a program.",
        "advantages": "Concise syntax, expressive data transformation, and clean organization of code.",
        "features": "Anonymous functions, collection processing, reusable modules, and variable scoping.",
        "syntax": "result = list(map(lambda x: x * 2, [1, 2, 3]))\nprint(result)",
        "python_examples": "- Lambda for squaring numbers\n- map() for transformation\n- filter() for selection\n- reduce() for accumulation\n- import math and random",
        "real_time_examples": "These concepts are used in analytics pipelines, data cleaning, and automation tasks.",
        "interview_questions": "1. What is a lambda function?\n2. What is the difference between map and filter?\n3. What does reduce do?\n4. What is a module?\n5. What is a package?\n6. What is local scope?\n7. What is global scope?\n8. Why are modules helpful?\n9. What is the purpose of import math?\n10. How do you avoid naming conflicts in modules?",
        "practice_questions": "1. Use lambda to square numbers.\n2. Use map to double each item in a list.\n3. Use filter to select even numbers.\n4. Import math and use sqrt().\n5. Import random and generate a random number.\n6. Write a small module and import it.\n7. Demonstrate global and local scope.\n8. Use reduce to find the sum of a list.",
        "leetcode_problems": "- Two Sum\n- Group Anagrams\n- Valid Parentheses\n- Valid Anagram\n- Contains Duplicate II\n- Roman to Integer\n- Longest Common Prefix",
        "learning_outcome": "The learner can write concise functional code and use Python’s built-in modules efficiently.",
        "summary": "Day 8 introduced functional programming patterns and modular coding practices.",
        "notes_content": "Functional programming tools allow developers to process data in an elegant manner without writing excessive loops. Modules and packages separate concerns and make code easier to reuse. Understanding scope is important because it determines how variables behave when code grows larger.",
        "python_code": "from functools import reduce\nimport math\nimport random\n\nnums = [1, 2, 3, 4]\nprint(list(map(lambda x: x * 2, nums)))\nprint(list(filter(lambda x: x % 2 == 0, nums)))\nprint(reduce(lambda a, b: a + b, nums))\nprint(math.sqrt(16))\nprint(random.randint(1, 10))\n"
    },
    {
        "folder": "Day-09_File_Handling",
        "day": 9,
        "title": "File Handling",
        "date": "14-07-2026",
        "topics": "Read, Write, Append, With Statement, CSV, Text Files",
        "theory": "File handling allows programs to read and store data on disk. Common operations include opening files, reading content, writing new content, appending records, and closing files safely. The with statement ensures resources are released correctly after the operation. CSV files are commonly used for tabular data.",
        "key_concepts": "Files can be opened in read, write, append, or binary modes. The with statement is the preferred way to manage file resources.",
        "advantages": "Persistent storage, logging, report generation, and data exchange.",
        "features": "read(), write(), append(), open(), and iteration over file content.",
        "syntax": "with open('sample.txt', 'w') as f:\n    f.write('Hello file')",
        "python_examples": "- Create a text file\n- Read from a file\n- Append content\n- Read CSV data\n- Mini file project",
        "real_time_examples": "File handling is used in log systems, report creators, inventory tools, and document storage apps.",
        "interview_questions": "1. What is the difference between write and append mode?\n2. Why is the with statement used?\n3. What is a CSV file?\n4. How do you read a file line by line?\n5. What happens if a file does not exist in read mode?\n6. What is the difference between text and binary files?\n7. How do you safely close a file?\n8. Why is file handling important?\n9. What is file buffering?\n10. How do you write structured data to a file?",
        "practice_questions": "1. Write a note to a text file.\n2. Read and print the contents of a file.\n3. Append a new line to an existing file.\n4. Store student names in CSV format.\n5. Count words in a file.\n6. Build a mini diary program.\n7. Create a file organizer script.\n8. Read a CSV file and print rows.",
        "leetcode_problems": "File handling practice focused on reading, writing, appending, and parsing structured data.",
        "learning_outcome": "The learner can manage data persistence using files and understand text and CSV formats.",
        "summary": "Day 9 introduced data persistence through file operations.",
        "notes_content": "Programs often need to remember information between runs. File handling provides that persistence by writing and reading data to disk. In real applications, file operations are common because they help manage logs, reports, saved settings, and user-generated content.",
        "python_code": "with open('notes.txt', 'w') as f:\n    f.write('Python file handling demo\\n')\n\nwith open('notes.txt', 'r') as f:\n    print(f.read())\n\nwith open('notes.txt', 'a') as f:\n    f.write('Appended line\\n')\n"
    },
    {
        "folder": "Day-10_Exception_Handling",
        "day": 10,
        "title": "Exception Handling",
        "date": "15-07-2026",
        "topics": "try, except, finally, raise, custom exceptions",
        "theory": "Exception handling allows a program to respond gracefully to runtime errors. The try block contains code that may fail, except catches the error, finally runs regardless of the outcome, and raise allows custom exceptions to be triggered when necessary.",
        "key_concepts": "Exceptions are errors that occur during execution. They should be handled to keep the application resilient and user-friendly.",
        "advantages": "Better reliability, easier debugging, and a smoother user experience.",
        "features": "Specific exception handling, custom exception classes, and cleanup logic.",
        "syntax": "try:\n    x = int('abc')\nexcept ValueError:\n    print('Invalid value')",
        "python_examples": "- Handle division by zero\n- Catch invalid input\n- Custom exception example\n- Cleanup with finally\n- Raise an exception",
        "real_time_examples": "Exception handling is used in banking apps, APIs, payment systems, and data processing workflows.",
        "interview_questions": "1. What is an exception?\n2. What is the purpose of try and except?\n3. What is finally used for?\n4. What is a custom exception?\n5. What is the difference between an error and an exception?\n6. What is raising an exception?\n7. Why should exceptions be handled?\n8. What is the role of finally in cleanup?\n9. How do you handle multiple exceptions?\n10. What happens if an exception is not handled?",
        "practice_questions": "1. Handle division by zero gracefully.\n2. Catch invalid integer conversion.\n3. Create a custom exception for age less than 18.\n4. Write a program that always prints a cleanup message.\n5. Raise an exception for negative input.\n6. Build a calculator with safe error handling.\n7. Create a file reading program with exception handling.\n8. Handle multiple exceptions in one block.",
        "leetcode_problems": "Exception handling practice focused on debugging, resilience, and reliable input handling.",
        "learning_outcome": "The learner can write robust programs that recover from errors gracefully.",
        "summary": "Day 10 emphasized defensive programming and graceful failure handling.",
        "notes_content": "Errors are part of programming, but they do not need to crash the application. Good exception handling makes code predictable and easier to debug. In interviews, this topic often demonstrates a developer’s maturity because it reflects attention to stability and user experience.",
        "python_code": "try:\n    num = int(input('Enter a number: '))\n    print(10 / num)\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')\nexcept ValueError:\n    print('Please enter a valid number')\nfinally:\n    print('Execution completed')\n"
    },
    {
        "folder": "Day-11_OOP_Classes",
        "day": 11,
        "title": "OOP Classes and Objects",
        "date": "16-07-2026",
        "topics": "Classes, Objects, Constructor, Inheritance, Single, Multiple, Multilevel, Hierarchical",
        "theory": "Object-Oriented Programming organizes code around classes and objects. A class defines the blueprint, and an object is a concrete instance of that class. Constructors initialize the object with state, and inheritance allows one class to reuse the behavior of another class.",
        "key_concepts": "Classes define structure, objects hold actual data, and inheritance supports code reuse. OOP models real-world systems better than flat procedural code.",
        "advantages": "Better structure, code reuse, maintainability, and scalability.",
        "features": "Attributes, methods, constructors, inheritance, and reusable class design.",
        "syntax": "class Student:\n    def __init__(self, name):\n        self.name = name",
        "python_examples": "- Student class\n- Bank account class\n- Library book class\n- Single inheritance example\n- Multilevel inheritance example",
        "real_time_examples": "OOP is used in banking systems, school software, game development, and e-commerce platforms.",
        "interview_questions": "1. What is a class?\n2. What is an object?\n3. What is a constructor?\n4. What is inheritance?\n5. What is single inheritance?\n6. What is multilevel inheritance?\n7. Why is OOP useful?\n8. What is an attribute?\n9. What is a method?\n10. How does inheritance improve code reuse?",
        "practice_questions": "1. Create a Student class.\n2. Create a BankAccount class with deposit and withdraw methods.\n3. Build a Book class for a library system.\n4. Implement single inheritance.\n5. Implement multilevel inheritance.\n6. Use a constructor to initialize values.\n7. Create a class with methods and attributes.\n8. Explain how inheritance improves code reuse.",
        "leetcode_problems": "OOP practice included designing reusable class structures for real-world entities and inheritance-based extensions.",
        "learning_outcome": "The learner can model real-world entities using classes and apply inheritance to build extensible programs.",
        "summary": "Day 11 introduced the core principles of object-oriented design.",
        "notes_content": "OOP allows developers to think in terms of entities and relationships instead of isolated statements. This makes software easier to organize and maintain as it grows. In interviews, OOP questions often test whether a candidate can connect real-world concepts with the right class structure.",
        "python_code": "class Student:\n    def __init__(self, name, grade):\n        self.name = name\n        self.grade = grade\n\n    def show(self):\n        print(self.name, self.grade)\n\nobj = Student('Mina', 'A')\nobj.show()\n"
    },
    {
        "folder": "Day-12_OOP_Advanced",
        "day": 12,
        "title": "OOP Advanced",
        "date": "17-07-2026",
        "topics": "Encapsulation, Abstraction, Polymorphism, Method Overriding, Method Overloading Explanation",
        "theory": "Advanced OOP concepts make software design more robust and expressive. Encapsulation protects internal state, abstraction hides unnecessary details, and polymorphism allows a common interface to work across different types.",
        "key_concepts": "Use encapsulation to protect data, abstraction to simplify interaction, and polymorphism to increase flexibility.",
        "advantages": "Enhanced design quality, safer data handling, and more maintainable systems.",
        "features": "Private attributes, abstract methods, dynamic dispatch, and method overriding.",
        "syntax": "class Animal:\n    def speak(self):\n        pass",
        "python_examples": "- Encapsulation example\n- Abstraction class\n- Method overriding example\n- Polymorphism example\n- Shape hierarchy",
        "real_time_examples": "Advanced OOP is used in frameworks, UI libraries, simulation tools, and enterprise systems.",
        "interview_questions": "1. What is encapsulation?\n2. What is abstraction?\n3. What is polymorphism?\n4. What is method overriding?\n5. What is method overloading?\n6. Why is encapsulation useful?\n7. How does polymorphism improve flexibility?\n8. What is an abstract class?\n9. What is the difference between abstraction and encapsulation?\n10. How are OOP principles used in projects?",
        "practice_questions": "1. Create a class with private attributes.\n2. Design an abstract base class.\n3. Implement method overriding.\n4. Demonstrate polymorphism.\n5. Compare encapsulation and abstraction.\n6. Build a shape hierarchy.\n7. Create a base class and two derived classes.\n8. Explain why polymorphism helps maintenance.",
        "leetcode_problems": "Advanced OOP practice included design thinking, inheritance-based behavior, and interface-oriented coding.",
        "learning_outcome": "The learner can design cleaner object-oriented systems using advanced principles.",
        "summary": "Day 12 moved beyond basic classes and explored deeper design ideas.",
        "notes_content": "Advanced OOP principles show that a developer can think beyond syntax and toward software architecture. These ideas become more important as projects become larger and more complex. Understanding them helps create code that is easier to test, extend, and maintain over time.",
        "python_code": "class BankAccount:\n    def __init__(self, balance):\n        self.__balance = balance\n\n    def deposit(self, amount):\n        self.__balance += amount\n\n    def get_balance(self):\n        return self.__balance\n\naccount = BankAccount(100)\naccount.deposit(50)\nprint(account.get_balance())\n"
    },
    {
        "folder": "Day-13_Standard_Libraries",
        "day": 13,
        "title": "Standard Libraries",
        "date": "18-07-2026",
        "topics": "os, sys, math, random, datetime, time, json, shutil",
        "theory": "Python’s standard library offers reliable modules for common tasks. The os and shutil modules help with file operations, sys supports runtime interaction, math and random support computation and randomness, datetime and time handle dates and time, and json allows data exchange in a structured form.",
        "key_concepts": "Built-in modules save time and reduce the need for custom implementations. They are especially helpful for scripting and automation.",
        "advantages": "Fast development, reliability, and broad support for real-world tasks.",
        "features": "Automation, file operations, date handling, random generation, and JSON support.",
        "syntax": "import os\nprint(os.getcwd())",
        "python_examples": "- File organizer script\n- Rename files\n- Random password generator\n- Folder cleaner\n- JSON save and load",
        "real_time_examples": "Standard libraries are used in automation scripts, backup tools, analytics workflows, and configuration managers.",
        "interview_questions": "1. What is the standard library?\n2. What is os used for?\n3. What is json useful for?\n4. How is random used?\n5. What is datetime used for?\n6. What does shutil help with?\n7. Why are built-in modules important?\n8. What is the difference between os and shutil?\n9. How do you read command-line arguments with sys?\n10. How can Python automate repetitive tasks?",
        "practice_questions": "1. List files in a folder using os.\n2. Rename a file using os.\n3. Generate a random password.\n4. Print the current date and time.\n5. Convert a dictionary to JSON.\n6. Clean a folder of temporary files.\n7. Create a file organizer script.\n8. Use math to calculate the square root of a number.",
        "leetcode_problems": "Standard library exercises included automation tasks, file operations, and utility scripting.",
        "learning_outcome": "The learner can use Python’s built-in modules to automate tasks and solve everyday problems efficiently.",
        "summary": "Day 13 introduced the standard library, which makes Python practical for automation and productivity tasks.",
        "notes_content": "The standard library is one of Python’s biggest strengths. It includes modules that handle many common programming concerns without installing extra packages. That makes Python an excellent choice for quickly building useful tools and scripts in a real-world environment.",
        "python_code": "import os\nimport json\nimport random\nfrom datetime import datetime\n\nprint(os.getcwd())\nprint(datetime.now())\n\npassword = ''.join(random.choice('abc123') for _ in range(8))\nprint(password)\n\nstudent = {'name': 'Asha', 'age': 21}\nprint(json.dumps(student))\n"
    },
    {
        "folder": "Day-14_SQLite",
        "day": 14,
        "title": "SQLite Database",
        "date": "19-07-2026",
        "topics": "Create Database, Create Table, Insert, Update, Delete, Select, WHERE, ORDER BY, GROUP BY, JOIN",
        "theory": "SQLite is a lightweight database engine that integrates well with Python. It allows developers to create databases and tables, insert rows, update records, and query data without needing a separate server. SQL clauses such as WHERE, ORDER BY, GROUP BY, and JOIN help retrieve meaningful information.",
        "key_concepts": "A database stores data in tables, and SQL commands manage records. Joins combine related data from multiple tables.",
        "advantages": "Lightweight, easy to start, serverless, and perfect for small applications and prototypes.",
        "features": "Persistent storage, relational modeling, SQL queries, and direct integration with Python.",
        "syntax": "import sqlite3\nconn = sqlite3.connect('students.db')",
        "python_examples": "- Create a student database\n- Create a table\n- Insert a row\n- Update a record\n- Query records",
        "real_time_examples": "SQLite is used in mobile apps, desktop tools, prototypes, and local storage systems.",
        "interview_questions": "1. What is SQLite?\n2. What is the difference between SQL and SQLite?\n3. How do you create a table?\n4. What is the purpose of WHERE?\n5. What is the difference between UPDATE and DELETE?\n6. What is a JOIN?\n7. Why is ORDER BY used?\n8. What is GROUP BY?\n9. How do you connect Python to SQLite?\n10. What is a database schema?",
        "practice_questions": "1. Create a database for students.\n2. Create a table with student information.\n3. Insert three student records.\n4. Update one student's grade.\n5. Delete one record.\n6. Select all students.\n7. Filter students by age.\n8. Use ORDER BY and GROUP BY in queries.",
        "leetcode_problems": "Database practice included CRUD logic, table design, and basic SQL query building.",
        "learning_outcome": "The learner can create and interact with a lightweight relational database using Python and SQLite.",
        "summary": "Day 14 introduced database programming and SQL fundamentals through SQLite.",
        "notes_content": "SQLite is a great starting point for learning databases because it is simple and does not require a separate server. The same concepts apply to larger systems later, so mastering SQLite builds a strong foundation for relational database understanding.",
        "python_code": "import sqlite3\n\nconn = sqlite3.connect('students.db')\ncur = conn.cursor()\ncur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)')\ncur.execute('INSERT INTO students (name, marks) VALUES (\'Asha\', 90)')\nconn.commit()\ncur.execute('SELECT * FROM students')\nprint(cur.fetchall())\nconn.close()\n"
    },
    {
        "folder": "Day-15_CRUD",
        "day": 15,
        "title": "CRUD Operations",
        "date": "20-07-2026",
        "topics": "Student Database Project, Employee Database Project, Library Database Project, Expense Tracker, SQL Interview Questions",
        "theory": "CRUD stands for Create, Read, Update, and Delete. These four operations form the foundation of most database-driven applications. A practical CRUD system allows users to manage information through menu-driven scripts or forms.",
        "key_concepts": "Create inserts data, Read fetches it, Update modifies it, and Delete removes it. CRUD is central to business applications and data management systems.",
        "advantages": "Standardized data handling, easier maintenance, and strong relevance to real software systems.",
        "features": "Menu-based operations, validation, persistent storage, and query execution.",
        "syntax": "cur.execute('INSERT INTO students (name) VALUES (?)', ('Ravi',))",
        "python_examples": "- Student CRUD menu\n- Employee record manager\n- Library records\n- Expense tracker\n- SQL interview questions",
        "real_time_examples": "CRUD systems power school portals, HR tools, inventory systems, and banking applications.",
        "interview_questions": "1. What is CRUD?\n2. What is the difference between INSERT and UPDATE?\n3. What is the role of a primary key?\n4. Why are SQL queries important?\n5. How do you delete a record safely?\n6. How do you filter records by a condition?\n7. What is a database transaction?\n8. What is the role of a foreign key?\n9. Why is validation important in CRUD?\n10. What is the difference between a database and a table?",
        "practice_questions": "1. Create a student CRUD program.\n2. Build an employee CRUD program.\n3. Create a library catalog manager.\n4. Build an expense tracker with storage.\n5. Practice SQL interview questions.\n6. Add search functionality to a database app.\n7. Implement delete confirmation.\n8. Use a menu-driven interface for CRUD operations.",
        "leetcode_problems": "CRUD tasks included building complete database applications with insertion, retrieval, updates, and deletion flow.",
        "learning_outcome": "The learner can design and implement practical database applications using Python and SQL.",
        "summary": "Day 15 connected database concepts with real product thinking by implementing CRUD-based projects.",
        "notes_content": "CRUD is one of the most important concepts in application development. Almost every software system stores data and needs ways to create, access, modify, and delete it. Designing this flow clearly is essential because it forms the basis of user-facing applications.",
        "python_code": "import sqlite3\n\nconn = sqlite3.connect('students.db')\ncur = conn.cursor()\ncur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)')\ncur.execute('INSERT INTO students (name, marks) VALUES (\'Ravi\', 88)')\nconn.commit()\ncur.execute('SELECT * FROM students')\nprint(cur.fetchall())\ncur.execute('UPDATE students SET marks = 92 WHERE name = \'Ravi\'')\nconn.commit()\ncur.execute('DELETE FROM students WHERE name = \'Ravi\'')\nconn.commit()\nconn.close()\n"
    },
    {
        "folder": "Day-16_Current_Progress",
        "day": 16,
        "title": "Current Progress",
        "date": "21-07-2026",
        "topics": "Placement Training Status, MCQ Tests, AI Digital Twin Project, Viva, PPT Submission",
        "theory": "This day reviews the progress made so far in training. It highlights daily consistency, test performance, project development, and professional communication. It also reflects the balance between learning, practice, and portfolio building that is essential for placement preparation.",
        "key_concepts": "Progress tracking and documentation are essential for showing growth. A strong portfolio communicates both technical ability and discipline.",
        "advantages": "Clear visibility of growth, stronger portfolio quality, and better preparation for interviews.",
        "features": "Training summary, test scores, project overview, progress review, and future roadmap.",
        "syntax": "status = 'Ongoing'\ntraining_started = '06 July 2026'",
        "python_examples": "- Progress summary\n- MCQ score review\n- Project milestone checklist\n- Viva preparation notes\n- Future roadmap",
        "real_time_examples": "Progress tracking is used in education, internships, and job readiness programs to map growth over time.",
        "interview_questions": "1. What is your current training status?\n2. What projects are you working on?\n3. What were your MCQ test scores?\n4. What is your future learning plan?\n5. How did you document your progress?\n6. What is your strongest topic so far?\n7. What is your current challenge?\n8. Why is documentation important?\n9. How did Viva experiences improve your confidence?\n10. What are you preparing next?",
        "practice_questions": "1. Prepare a personal progress report.\n2. Summarize your learning journey in a paragraph.\n3. Create a roadmap for the next month.\n4. Write a short project description.\n5. Prepare five interview talking points.\n6. Review your strongest and weakest topics.\n7. Make a weekly study plan.\n8. Draft a professional GitHub portfolio summary.",
        "leetcode_problems": "Current progress focused on portfolio building, documentation quality, and continuous reflection on practical growth.",
        "learning_outcome": "The learner understands the importance of tracking progress and presenting technical growth professionally.",
        "summary": "Day 16 consolidated the training journey and highlighted readiness for placement interviews and project discussions.",
        "notes_content": "This stage is not only about learning concepts; it is about demonstrating growth. A strong portfolio shows activity, reflection, and consistency. In interviews, candidates are often judged not only on technical knowledge but also on how clearly they explain what they have built and how they improved over time.",
        "python_code": "training_started = '06 July 2026'\nstatus = 'Ongoing'\nscore_1 = '24/25'\nscore_2 = '24/25'\nscore_3 = '24/25'\n\nprint('Training started on:', training_started)\nprint('Status:', status)\nprint('MCQ scores:', score_1, score_2, score_3)\n"
    },
]

for day in days:
    build_day(
        day["day"],
        day["folder"],
        day["title"],
        day["date"],
        day["topics"],
        day["theory"],
        day["key_concepts"],
        day["advantages"],
        day["features"],
        day["syntax"],
        day["python_examples"],
        day["real_time_examples"],
        day["interview_questions"],
        day["practice_questions"],
        day["leetcode_problems"],
        day["learning_outcome"],
        day["summary"],
        day["notes_content"],
        day["python_code"],
    )

print("Repository generation completed for all days up to Day 16.")
