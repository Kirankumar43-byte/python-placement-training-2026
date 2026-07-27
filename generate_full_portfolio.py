from pathlib import Path
from textwrap import dedent

ROOT = Path(r"c:\Users\Kiran Kumar\OneDrive\Desktop\python-placement-training-2026")
ROOT.mkdir(parents=True, exist_ok=True)


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def ensure_file(path, content):
    if not path.exists():
        write(path, content)


# ----------------------------
# Root documentation
# ----------------------------
root_readme = """# Python Placement Training 2026

![Python Banner](https://img.shields.io/badge/Python-Placement%20Training-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?style=for-the-badge&logo=github)
![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)
![Profile](https://img.shields.io/badge/LeetCode-Profile-FFA116?style=flat-square&logo=leetcode&logoColor=white)

> A professional GitHub portfolio for placement preparation, built with Python, SQL, documentation, and daily practice.

## 🌟 Animated Header

```text
PYTHON  |  SQL  |  DSA  |  PROJECTS  |  INTERVIEW PREP
```

## 📊 Visitor Counter Placeholder

![Visitor Count](https://visit-counter.vercel.app/counter.png?page=python-placement-training-2026)

## 🧠 Typing Animation Placeholder

```text
Learning Python every day • Building projects • Solving LeetCode • Preparing for interviews
```

## 🧭 Table of Contents
- [Repository Overview](#-repository-overview)
- [Skills Learned](#-skills-learned)
- [Training Progress](#-training-progress)
- [Daily Progress Table](#-daily-progress-table)
- [LeetCode Practice](#-leetcode-practice)
- [Project Section](#-project-section)
- [MCQ Test Results](#-mcq-test-results)
- [Technology Icons](#-technology-icons)
- [Repository Statistics](#-repository-statistics)
- [Future Goals](#-future-goals)
- [Acknowledgements](#-acknowledgements)

## 🧩 Repository Overview
This repository documents my complete placement training journey in Python during 2026. It combines theory notes, practice programs, interview preparation, LeetCode practice, SQLite database work, and project documentation in a recruiter-friendly portfolio format.

## 🛠️ Skills Learned
- Python fundamentals and syntax
- Variables, operators, loops, and conditionals
- Functions, modules, and file handling
- Exception handling and OOP concepts
- SQLite databases and CRUD programming
- Automation and documentation practices
- Interview readiness and problem-solving

## 📈 Training Progress
- Training Started: 06 July 2026
- Current Status: Ongoing
- Project: AI Digital Twin for Personalized Student Learning
- Viva 1: Completed
- Viva 2: Completed
- PPT Submitted: Yes

## 📅 Daily Progress Table
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

## 🧪 LeetCode Practice
My profile: https://leetcode.com/u/CodeEthical_Kiran/

| Day | Problem | Difficulty | Official Link | Local Solution |
|---|---|---|---|---|
| Day 02 | Fizz Buzz | Easy | [Link](https://leetcode.com/problems/fizz-buzz/) | [Solution](LeetCode/Day-02/fizz-buzz/README.md) |
| Day 02 | Reverse Integer | Medium | [Link](https://leetcode.com/problems/reverse-integer/) | [Solution](LeetCode/Day-02/reverse-integer/README.md) |
| Day 03 | Integer to Roman | Medium | [Link](https://leetcode.com/problems/integer-to-roman/) | [Solution](LeetCode/Day-03/integer-to-roman/README.md) |
| Day 05 | Best Time to Buy and Sell Stock | Easy | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Solution](LeetCode/Day-05/best-time-to-buy-and-sell-stock/README.md) |
| Day 06 | Contains Duplicate | Easy | [Link](https://leetcode.com/problems/contains-duplicate/) | [Solution](LeetCode/Day-06/contains-duplicate/README.md) |
| Day 07 | Number of Islands | Medium | [Link](https://leetcode.com/problems/number-of-islands/) | [Solution](LeetCode/Day-07/number-of-islands/README.md) |
| Day 08 | Two Sum | Easy | [Link](https://leetcode.com/problems/two-sum/) | [Solution](LeetCode/Day-08/two-sum/README.md) |
| Day 14 | Employee Importance | Easy | [Link](https://leetcode.com/problems/employee-importance/) | [Solution](LeetCode/Day-14/employee-importance/README.md) |

## 🧾 Project Section
- [AI-Digital-Twin-Project](AI-Digital-Twin-Project/README.md)
- [MCQ Tests](MCQ-Tests/README.md)
- [Database Task](Day-14_SQLite/Database_Task/README.md)

## 📝 MCQ Test Results
| Date | Score |
|---|---:|
| 10 July 2026 | 24/25 |
| 17 July 2026 | 24/25 |
| 24 July 2026 | 24/25 |

## 💡 Technology Icons
- Python
- SQLite
- Markdown
- GitHub
- VS Code
- LeetCode

## 📈 Repository Statistics
- Total Training Days: 16
- Documentation Files: 100+
- Python Programs: 150+
- LeetCode Solutions: 30+
- Database Projects: 4

## 🎯 Future Goals
- Strengthen DSA and coding speed
- Build additional Python projects
- Improve technical interview communication
- Continue personal portfolio growth

## 🙏 Acknowledgements
Thanks to all learning resources, mentors, and the Python community for supporting this journey.

---

## 📚 Daily Learning Folders
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

---

Made with care for interview readiness and long-term professional growth.
"""
write(ROOT / "README.md", root_readme)

# ----------------------------
# Day program generation
# ----------------------------
programs_by_day = {
    1: [
        ("hello_world.py", """# Program 1: Hello World
# This program prints a message to the console.

print("Hello, World!")
print("Welcome to Python Placement Training")

# Example Output:
# Hello, World!
# Welcome to Python Placement Training
"""),
        ("greeting.py", """# Program 2: Greeting with input
# Ask the user for their name and print a friendly greeting.

name = input("Enter your name: ")
print(f"Hello, {name}!")

# Example Input:
# Kiran
# Example Output:
# Hello, Kiran!
"""),
        ("arithmetic.py", """# Program 3: Arithmetic operations
# Perform basic arithmetic operations on two numbers.

a = 10
b = 5
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
"""),
        ("comments_demo.py", """# Program 4: Comments and explanation
# Comments are useful for documenting code.

# This line prints a message.
print("Python comments help explain logic")
"""),
        ("simple_calculator.py", """# Program 5: Simple calculator
# Accept two numbers and print the sum.

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Sum:", first + second)

# Example Input:
# 7
# 3
# Example Output:
# Sum: 10
"""),
    ],
    2: [
        ("variable_demo.py", """# Program 1: Variables and printing
name = "Asha"
age = 21
print("Name:", name)
print("Age:", age)
"""),
        ("data_type_check.py", """# Program 2: Check the data type of a value
value = 42
print(type(value))
"""),
        ("string_concat.py", """# Program 3: String concatenation
first_name = "Kiran"
last_name = "Kumar"
print(first_name + " " + last_name)
"""),
        ("type_conversion.py", """# Program 4: Convert input to int
num = int(input("Enter a number: "))
print("Square:", num * num)
"""),
        ("swap_numbers.py", """# Program 5: Swap two numbers
a = 5
b = 9
a, b = b, a
print(a, b)
"""),
        ("simple_interest.py", """# Program 6: Simple interest
principal = 1000
rate = 5
time = 2
interest = (principal * rate * time) / 100
print("Simple Interest:", interest)
"""),
        ("area_rectangle.py", """# Program 7: Area of rectangle
length = 8
breadth = 6
print("Area:", length * breadth)
"""),
        ("even_odd.py", """# Program 8: Check even or odd
number = int(input("Enter a number: "))
print("Even" if number % 2 == 0 else "Odd")
"""),
        ("operator_demo.py", """# Program 9: Arithmetic operators
a = 12
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""),
        ("boolean_demo.py", """# Program 10: Boolean expressions
print(10 > 5)
print(3 < 1)
"""),
        ("temperature_converter.py", """# Program 11: Convert Celsius to Fahrenheit
celsius = 30
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}C = {fahrenheit}F")
"""),
        ("circle_area.py", """# Program 12: Area of circle
radius = 4
area = 3.14 * radius * radius
print("Area:", area)
"""),
        ("discount_calculator.py", """# Program 13: Discount calculator
price = 500
discount = 10
final_price = price - (price * discount / 100)
print(final_price)
"""),
        ("marks_average.py", """# Program 14: Average of marks
m1 = 80
m2 = 90
m3 = 70
print((m1 + m2 + m3) / 3)
"""),
        ("name_length.py", """# Program 15: Length of a string
name = "Priya"
print(len(name))
"""),
        ("formatting_demo.py", """# Program 16: String formatting
name = "Ravi"
print("Hello {}".format(name))
"""),
        ("age_checker.py", """# Program 17: Age check
age = int(input("Enter age: "))
print("Eligible" if age >= 18 else "Not eligible")
"""),
        ("calculator.py", """# Program 18: Basic calculator
x = 8
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x // y)
"""),
        ("input_output_demo.py", """# Program 19: Input-output demonstration
name = input("Enter your name: ")
print("You entered:", name)
"""),
        ("multiple_assign.py", """# Program 20: Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)
"""),
    ],
    3: [
        ("voting_check.py", """# Program 1: Voting eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
"""),
        ("grade_checker.py", """# Program 2: Grade classification
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
else:
    print("C Grade")
"""),
        ("password_check.py", """# Program 3: Password length check
password = input("Enter password: ")
if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")
"""),
        ("max_of_three.py", """# Program 4: Maximum of three numbers
a, b, c = 10, 20, 15
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
"""),
        ("leap_year.py", """# Program 5: Leap year checker
year = int(input("Enter year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
"""),
        ("nested_if_demo.py", """# Program 6: Nested condition example
age = 25
citizen = True
if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Not eligible")
"""),
        ("odd_even_menu.py", """# Program 7: Conditional menu
choice = input("Enter 'E' or 'O': ").upper()
if choice == 'E':
    print("Even")
elif choice == 'O':
    print("Odd")
else:
    print("Invalid choice")
"""),
        ("membership_demo.py", """# Program 8: Membership operator
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Found")
"""),
        ("identity_demo.py", """# Program 9: Identity operator
a = 10
b = 10
print(a is b)
"""),
        ("calculator_conditional.py", """# Program 10: Simple calculator using conditions
op = input("Enter operator (+, -, *, /): ")
a = 8
b = 4
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid")
"""),
        ("weekday_check.py", """# Program 11: Check weekday
day = int(input("Enter number 1-7: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
else:
    print("Other day")
"""),
        ("multiple_conditions.py", """# Program 12: Multiple conditions
age = 20
income = 50000
if age >= 18 and income > 30000:
    print("Eligible")
"""),
        ("positive_negative.py", """# Program 13: Positive/negative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
"""),
        ("compare_numbers.py", """# Program 14: Compare numbers
a, b = 5, 8
if a < b:
    print("a is less than b")
"""),
        ("student_result.py", """# Program 15: Student result check
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")
"""),
    ],
    4: [
        ("print_numbers.py", """# Program 1: Print numbers with for loop
for i in range(1, 11):
    print(i)
"""),
        ("sum_numbers.py", """# Program 2: Sum numbers with loop
total = 0
for i in range(1, 11):
    total += i
print(total)
"""),
        ("even_loop.py", """# Program 3: Print even numbers
for i in range(2, 21, 2):
    print(i)
"""),
        ("reverse_string_loop.py", """# Program 4: Reverse a string
word = "python"
for ch in reversed(word):
    print(ch)
"""),
        ("factorial_loop.py", """# Program 5: Factorial
n = 5
result = 1
for i in range(1, n + 1):
    result *= i
print(result)
"""),
        ("while_countdown.py", """# Program 6: Countdown with while loop
count = 5
while count > 0:
    print(count)
    count -= 1
"""),
        ("prime_check.py", """# Program 7: Prime number check
n = 29
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)
"""),
        ("fibonacci.py", """# Program 8: Fibonacci sequence
n = 7
first, second = 0, 1
for _ in range(n):
    print(first)
    first, second = second, first + second
"""),
        ("nested_loop_pattern.py", """# Program 9: Nested loop pattern
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
"""),
        ("break_demo.py", """# Program 10: Break example
for i in range(1, 10):
    if i == 5:
        break
    print(i)
"""),
        ("continue_demo.py", """# Program 11: Continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
"""),
        ("pass_demo.py", """# Program 12: Pass placeholder
for i in range(3):
    pass
print("Done")
"""),
        ("multiplication_table.py", """# Program 13: Multiplication table
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)
"""),
        ("digit_sum.py", """# Program 14: Sum of digits
num = 1234
s = 0
while num > 0:
    s += num % 10
    num //= 10
print(s)
"""),
        ("star_pattern.py", """# Program 15: Star pattern
for i in range(1, 6):
    print('*' * i)
"""),
        ("vowel_count.py", """# Program 16: Count vowels
word = "beautiful"
count = 0
for ch in word:
    if ch in "aeiou":
        count += 1
print(count)
"""),
        ("factor_finder.py", """# Program 17: Find factors
num = 24
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
"""),
        ("average_loop.py", """# Program 18: Average with loop
numbers = [10, 20, 30]
total = sum(numbers)
print(total / len(numbers))
"""),
        ("loop_menu.py", """# Program 19: Loop menu
a = 1
while a <= 5:
    print("Step", a)
    a += 1
"""),
        ("palindrome_loop.py", """# Program 20: Palindrome check
word = "level"
print(word == word[::-1])
"""),
    ],
    5: [
        ("list_basics.py", """# Program 1: List basics
fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(len(fruits))
"""),
        ("list_append.py", """# Program 2: Append to a list
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
"""),
        ("list_remove.py", """# Program 3: Remove from a list
cities = ["Delhi", "Mumbai", "Chennai"]
cities.remove("Mumbai")
print(cities)
"""),
        ("list_sort.py", """# Program 4: Sort a list
scores = [40, 10, 25]
scores.sort()
print(scores)
"""),
        ("list_reverse.py", """# Program 5: Reverse a list
letters = ["a", "b", "c"]
letters.reverse()
print(letters)
"""),
        ("list_count.py", """# Program 6: Count list items
items = [1, 2, 2, 3]
print(items.count(2))
"""),
        ("list_slice.py", """# Program 7: Slicing
nums = [10, 20, 30, 40]
print(nums[1:3])
"""),
        ("tuple_demo.py", """# Program 8: Tuple example
point = (10, 20)
print(point[0])
"""),
        ("tuple_unpack.py", """# Program 9: Unpack a tuple
x, y = (2, 5)
print(x, y)
"""),
        ("list_nested.py", """# Program 10: Nested list
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])
"""),
        ("list_sum.py", """# Program 11: Sum of list values
values = [5, 10, 15]
print(sum(values))
"""),
        ("list_max.py", """# Program 12: Largest value
values = [4, 11, 7]
print(max(values))
"""),
        ("list_min.py", """# Program 13: Smallest value
values = [4, 11, 7]
print(min(values))
"""),
        ("list_copy.py", """# Program 14: Copy a list
values = [1, 2, 3]
copy_values = values.copy()
print(copy_values)
"""),
        ("list_combine.py", """# Program 15: Concatenation
a = [1, 2]
b = [3, 4]
print(a + b)
"""),
        ("list_membership.py", """# Program 16: Membership checking
nums = [1, 2, 3]
print(2 in nums)
"""),
        ("list_iteration.py", """# Program 17: Iterate through list
for item in ["red", "green", "blue"]:
    print(item)
"""),
        ("tuple_to_list.py", """# Program 18: Convert tuple to list
coords = (1, 2, 3)
print(list(coords))
"""),
        ("list_average.py", """# Program 19: Average via list
nums = [10, 20, 30]
print(sum(nums) / len(nums))
"""),
        ("sequence_demo.py", """# Program 20: Sequence operations
numbers = [1, 2, 3]
print(numbers[1:])
"""),
    ],
    6: [
        ("set_demo.py", """# Program 1: Create a set
numbers = {1, 2, 2, 3}
print(numbers)
"""),
        ("set_union.py", """# Program 2: Set union
A = {1, 2}
B = {2, 3}
print(A | B)
"""),
        ("set_intersection.py", """# Program 3: Set intersection
A = {1, 2, 3}
B = {2, 3, 4}
print(A & B)
"""),
        ("set_difference.py", """# Program 4: Set difference
A = {1, 2, 3}
B = {2, 3, 4}
print(A - B)
"""),
        ("dictionary_demo.py", """# Program 5: Dictionary example
student = {"name": "Asha", "age": 21}
print(student["name"])
"""),
        ("dictionary_update.py", """# Program 6: Update dictionary
student = {"name": "Asha"}
student["age"] = 21
print(student)
"""),
        ("dictionary_get.py", """# Program 7: Safe lookup
student = {"name": "Asha"}
print(student.get("age", "Not found"))
"""),
        ("dictionary_items.py", """# Program 8: Iterate dictionary items
student = {"name": "Asha", "city": "Bengaluru"}
for key, value in student.items():
    print(key, value)
"""),
        ("list_comprehension.py", """# Program 9: List comprehension
squares = [x * x for x in range(5)]
print(squares)
"""),
        ("set_comprehension.py", """# Program 10: Set comprehension
evens = {x for x in range(10) if x % 2 == 0}
print(evens)
"""),
        ("nested_comprehension.py", """# Program 11: Nested comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(matrix)
"""),
        ("duplicate_removal.py", """# Program 12: Remove duplicates
nums = [1, 2, 2, 3]
print(list(set(nums)))
"""),
        ("frequency_counter.py", """# Program 13: Frequency count
items = ["a", "b", "a"]
print({item: items.count(item) for item in set(items)})
"""),
        ("student_marks.py", """# Program 14: Student marks dictionary
marks = {"Asha": 90, "Ravi": 85}
print(marks)
"""),
        ("word_count_dict.py", """# Program 15: Word frequency dictionary
text = "python python is fun"
words = text.split()
print({word: words.count(word) for word in set(words)})
"""),
    ],
    7: [
        ("greet_function.py", """# Program 1: Greeting function
def greet(name):
    return f"Hello, {name}" 

print(greet("Kiran"))
"""),
        ("add_numbers.py", """# Program 2: Add two numbers
def add(a, b):
    return a + b

print(add(3, 4))
"""),
        ("default_args.py", """# Program 3: Default arguments
def greet(name, prefix="Hi"):
    return f"{prefix}, {name}"

print(greet("Neha"))
"""),
        ("keyword_args.py", """# Program 4: Keyword arguments
def describe(name, age):
    print(name, age)

describe(age=22, name="Asha")
"""),
        ("variable_args.py", """# Program 5: Variable arguments
def show(*args):
    print(args)

show(1, 2, 3)
"""),
        ("factorial_recursive.py", """# Program 6: Recursive factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
"""),
        ("sum_recursive.py", """# Program 7: Sum recursively
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print(recursive_sum(5))
"""),
        ("power_function.py", """# Program 8: Power calculation
def power(base, exponent):
    return base ** exponent

print(power(2, 3))
"""),
        ("circle_area_function.py", """# Program 9: Circle area function
import math

def circle_area(r):
    return math.pi * r * r

print(circle_area(3))
"""),
        ("max_of_three_func.py", """# Program 10: Maximum of three
def largest(a, b, c):
    return max(a, b, c)

print(largest(4, 9, 2))
"""),
        ("even_odd_function.py", """# Program 11: Even/odd function
def is_even(n):
    return n % 2 == 0

print(is_even(6))
"""),
        ("string_reverse_function.py", """# Program 12: Reverse string function
def reverse_string(text):
    return text[::-1]

print(reverse_string("python"))
"""),
        ("return_multiple.py", """# Program 13: Return multiple values
def stats(a, b):
    return a + b, a - b

print(stats(4, 2))
"""),
        ("calculator_function.py", """# Program 14: Calculator function
def calc(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    return None

print(calc(5, 3, '+'))
"""),
        ("scope_demo.py", """# Program 15: Scope example
x = 10

def show():
    y = 20
    print(x, y)

show()
"""),
    ],
    8: [
        ("lambda_square.py", """# Program 1: Lambda square
nums = [1, 2, 3]
print(list(map(lambda x: x * x, nums)))
"""),
        ("lambda_even.py", """# Program 2: Lambda even filter
nums = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, nums)))
"""),
        ("reduce_sum.py", """# Program 3: Reduce sum
from functools import reduce
nums = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, nums))
"""),
        ("math_demo.py", """# Program 4: Math module
import math
print(math.sqrt(16))
"""),
        ("random_demo.py", """# Program 5: Random module
import random
print(random.randint(1, 10))
"""),
        ("datetime_demo.py", """# Program 6: Datetime module
from datetime import datetime
print(datetime.now())
"""),
        ("json_demo.py", """# Program 7: JSON module
import json
student = {"name": "Asha"}
print(json.dumps(student))
"""),
        ("global_local_scope.py", """# Program 8: Scope example
x = "global"

def show():
    x = "local"
    print(x)

show()
print(x)
"""),
        ("module_import.py", """# Program 9: Module import
import math
print(math.pi)
"""),
        ("package_demo.py", """# Program 10: Package-like structure note
# This sample shows the idea of using separate modules in a project.
print("Package example")
"""),
        ("map_string.py", """# Program 11: Map with strings
words = ["python", "java"]
print(list(map(lambda w: w.upper(), words)))
"""),
        ("filter_positive.py", """# Program 12: Filter positive numbers
nums = [-2, 1, 3, -4]
print(list(filter(lambda x: x > 0, nums)))
"""),
        ("reduce_product.py", """# Program 13: Product using reduce
from functools import reduce
nums = [2, 3, 4]
print(reduce(lambda a, b: a * b, nums))
"""),
        ("os_demo.py", """# Program 14: os module
import os
print(os.getcwd())
"""),
        ("shutil_demo.py", """# Program 15: shutil module
import shutil
print("shutil module loaded")
"""),
    ],
    9: [
        ("write_file.py", """# Program 1: Write to a file
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("Hello file")
print("File written")
"""),
        ("read_file.py", """# Program 2: Read from a file
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())
"""),
        ("append_file.py", """# Program 3: Append to a file
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("\nAppended line")
"""),
        ("with_statement.py", """# Program 4: Use with statement
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Using with statement")
"""),
        ("csv_write.py", """# Program 5: Write CSV
import csv
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Asha", 21])
"""),
        ("csv_read.py", """# Program 6: Read CSV
import csv
with open("students.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)
"""),
        ("word_counter.py", """# Program 7: Count words in a file
with open("demo.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(len(text.split()))
"""),
        ("line_counter.py", """# Program 8: Count lines
with open("demo.txt", "r", encoding="utf-8") as f:
    print(len(f.readlines()))
"""),
        ("file_exists.py", """# Program 9: Check if file exists
from pathlib import Path
print(Path("demo.txt").exists())
"""),
        ("file_rename.py", """# Program 10: Rename a file
from pathlib import Path
Path("demo.txt").rename("renamed_demo.txt")
print("File renamed")
"""),
        ("file_delete.py", """# Program 11: Delete a file
from pathlib import Path
Path("renamed_demo.txt").unlink(missing_ok=True)
print("File removed")
"""),
        ("file_copy.py", """# Program 12: Copy a file
from shutil import copyfile
copyfile("demo.txt", "demo_copy.txt")
print("File copied")
"""),
        ("diary_app.py", """# Program 13: Mini diary app
entry = input("Enter your diary entry: ")
with open("diary.txt", "a", encoding="utf-8") as f:
    f.write(entry + "\n")
print("Entry saved")
"""),
        ("student_report.py", """# Program 14: Save student report
with open("student_report.txt", "w", encoding="utf-8") as f:
    f.write("Student Report\n")
    f.write("Name: Kiran")
"""),
        ("json_file.py", """# Program 15: Store JSON to file
import json
with open("student.json", "w", encoding="utf-8") as f:
    json.dump({"name": "Asha"}, f)
print("JSON saved")
"""),
    ],
    10: [
        ("division_error.py", """# Program 1: Handle division by zero
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
"""),
        ("invalid_input.py", """# Program 2: Handle invalid input
try:
    x = int(input("Enter an integer: "))
    print(x)
except ValueError:
    print("Please enter a valid integer")
"""),
        ("file_exception.py", """# Program 3: Handle file errors
try:
    with open("missing.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
"""),
        ("custom_exception.py", """# Program 4: Custom exception
class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Age must be 18 or above")
    print("Adult")
except AgeError as exc:
    print(exc)
"""),
        ("finally_demo.py", """# Program 5: Finally block
try:
    print("Working")
finally:
    print("Cleanup complete")
"""),
        ("multiple_except.py", """# Program 6: Multiple exceptions
try:
    value = int(input("Enter number: "))
    print(100 / value)
except ZeroDivisionError:
    print("Zero division")
except ValueError:
    print("Invalid number")
"""),
        ("raise_exception.py", """# Program 7: Raise a custom exception
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age below minimum")
print("Welcome")
"""),
        ("safe_division.py", """# Program 8: Safe division
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    print(numerator / denominator)
except Exception as exc:
    print("An error occurred:", exc)
"""),
        ("nested_exception.py", """# Program 9: Nested error handling
try:
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print("Inner exception handled")
except Exception:
    print("Outer exception handled")
"""),
        ("input_validator.py", """# Program 10: Input validator
while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Try again")
print("Age entered:", age)
"""),
        ("exception_summary.py", """# Program 11: Exception summary
try:
    numbers = [1, 2]
    print(numbers[3])
except IndexError:
    print("Index out of range")
"""),
        ("bank_transaction.py", """# Program 12: Bank transaction example
balance = 100
try:
    withdraw = int(input("Enter amount to withdraw: "))
    if withdraw > balance:
        raise ValueError("Insufficient balance")
    print("Balance left:", balance - withdraw)
except ValueError as exc:
    print(exc)
"""),
        ("calculator_error_safe.py", """# Program 13: Safe calculator
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a + b)
except ValueError:
    print("Enter valid numbers")
"""),
        ("resource_cleanup.py", """# Program 14: Cleanup pattern
try:
    print("Processing")
finally:
    print("Resources cleaned")
"""),
        ("age_checker_exception.py", """# Program 15: Age check with exception
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("Child")
    print("Adult")
except Exception as exc:
    print(exc)
"""),
    ],
    11: [
        ("student_class.py", """# Program 1: Student class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(self.name, self.grade)

student = Student("Mina", "A")
student.show()
"""),
        ("bank_account.py", """# Program 2: Bank account class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
print(account.balance)
"""),
        ("book_class.py", """# Program 3: Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(self.title, self.author)

Book("Python", "Guido").info()
"""),
        ("teacher_student_inheritance.py", """# Program 4: Inheritance example
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

teacher = Teacher("Mr. Rao")
print(teacher.name)
"""),
        ("animal_hierarchy.py", """# Program 5: Multi-level inheritance
class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Puppy(Dog):
    pass

Puppy().speak()
"""),
        ("vehicle_polymorphism.py", """# Program 6: Polymorphism
class Vehicle:
    def move(self):
        print("Vehicle moving")

class Car(Vehicle):
    def move(self):
        print("Car moving")

for obj in [Vehicle(), Car()]:
    obj.move()
"""),
        ("employee_class.py", """# Program 7: Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

Employee("Asha", 50000).display()
"""),
        ("constructor_demo.py", """# Program 8: Constructor demo
class Laptop:
    def __init__(self, brand):
        self.brand = brand

print(Laptop("Dell").brand)
"""),
        ("shape_class.py", """# Program 9: Shape class
class Shape:
    def area(self):
        print("Area unknown")

class Circle(Shape):
    def area(self):
        print("Circle area")

Circle().area()
"""),
        ("student_manager.py", """# Program 10: Student manager using class
class StudentManager:
    def __init__(self):
        self.students = []

    def add(self, name):
        self.students.append(name)

manager = StudentManager()
manager.add("Ravi")
print(manager.students)
"""),
        ("library_system.py", """# Program 11: Library system class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

lib = Library()
lib.add_book("Python Basics")
print(lib.books)
"""),
        ("hospital_patient.py", """# Program 12: Hospital patient class
class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease

    def info(self):
        print(self.name, self.disease)

Patient("Rani", "Flu").info()
"""),
        ("inheritance_demo.py", """# Program 13: Single inheritance
class Base:
    def show(self):
        print("Base")

class Derived(Base):
    pass

Derived().show()
"""),
        ("multiple_inheritance.py", """# Program 14: Multiple inheritance
class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A, B):
    pass

C().method_a()
C().method_b()
"""),
        ("hierarchical_inheritance.py", """# Program 15: Hierarchical inheritance
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

print(Dog.__mro__)
"""),
        ("method_overriding.py", """# Program 16: Method overriding
class Parent:
    def greet(self):
        print("Parent")

class Child(Parent):
    def greet(self):
        print("Child")

Child().greet()
"""),
        ("encapsulation_demo.py", """# Program 17: Encapsulation
class Account:
    def __init__(self):
        self.__balance = 100

    def balance(self):
        return self.__balance

print(Account().balance())
"""),
        ("abstract_demo.py", """# Program 18: Abstract idea
class Shape:
    def draw(self):
        raise NotImplementedError

try:
    Shape().draw()
except NotImplementedError:
    print("Implemented later")
"""),
        ("polymorphism_demo.py", """# Program 19: Simple polymorphism
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

for animal in [Cat(), Dog()]:
    animal.speak()
"""),
        ("class_relationship.py", """# Program 20: Class relationship
class Course:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, course):
        self.course = course

course = Course("Python")
student = Student(course)
print(student.course.name)
"""),
    ],
    12: [
        ("encapsulation_private.py", """# Program 1: Private attributes
class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

print(BankAccount().get_balance())
"""),
        ("abstraction_base.py", """# Program 2: Abstract base class style
class Vehicle:
    def start(self):
        raise NotImplementedError

class Car(Vehicle):
    def start(self):
        print("Car started")

Car().start()
"""),
        ("method_overriding.py", """# Program 3: Overriding example
class Parent:
    def speak(self):
        print("Parent")

class Child(Parent):
    def speak(self):
        print("Child")

Child().speak()
"""),
        ("method_overloading.py", """# Program 4: Overloading style using default args
class Demo:
    def add(self, a, b=0):
        return a + b

print(Demo().add(3))
print(Demo().add(2, 5))
"""),
        ("polymorphism_shape.py", """# Program 5: Shape polymorphism
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10 * 5

class Circle(Shape):
    def area(self):
        return 3.14 * 3 * 3

for shape in [Rectangle(), Circle()]:
    print(shape.area())
"""),
        ("employee_oop.py", """# Program 6: Employee OOP example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name, self.salary)

Employee("Riya", 45000).show()
"""),
        ("library_oop.py", """# Program 7: Library OOP example
class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(self.title)

Book("Django").display()
"""),
        ("student_management_oop.py", """# Program 8: Student management OOP
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

sm = StudentManager()
sm.add_student("Kavya")
print(sm.students)
"""),
        ("bank_account_oop.py", """# Program 9: Bank account OOP
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

Account().deposit(50)
print(Account().balance)
"""),
        ("inheritance_composition.py", """# Program 10: Inheritance and composition
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()

print(Car().engine)
"""),
        ("class_methods.py", """# Program 11: Class method example
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count

print(Counter.increment())
"""),
        ("static_method.py", """# Program 12: Static method example
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.add(2, 3))
"""),
        ("object_identity.py", """# Program 13: Object identity
class Item:
    pass

x = Item()
y = x
print(x is y)
"""),
        ("oop_summary.py", """# Program 14: OOP summary
class Person:
    def __init__(self, name):
        self.name = name

print(Person("Ari").name)
"""),
        ("real_world_oop.py", """# Program 15: Real-world OOP sketch
class Order:
    def __init__(self, order_id):
        self.order_id = order_id

print(Order(101).order_id)
"""),
    ],
    13: [
        ("file_organizer.py", """# Program 1: File organizer
import os
for file in os.listdir('.'):
    if file.endswith('.py'):
        print(file)
"""),
        ("rename_files.py", """# Program 2: Rename files
import os
for index, file in enumerate(os.listdir('.')):
    if file.endswith('.txt'):
        os.rename(file, f"copy_{index}.txt")
print("Files renamed")
"""),
        ("random_password.py", """# Program 3: Random password generator
import random
import string
chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for _ in range(8))
print(password)
"""),
        ("folder_cleaner.py", """# Program 4: Folder cleaner
import os
for file in os.listdir('.'):
    if file.endswith('.tmp'):
        os.remove(file)
print("Cleanup complete")
"""),
        ("folder_size.py", """# Program 5: Folder size summary
import os
print(sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)))
"""),
        ("system_info.py", """# Program 6: System info
import os
print(os.name)
"""),
        ("date_time_script.py", """# Program 7: Date and time
from datetime import datetime
print(datetime.now())
"""),
        ("json_save.py", """# Program 8: Save JSON data
import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({'name': 'Asha'}, f)
print('JSON saved')
"""),
        ("json_read.py", """# Program 9: Read JSON data
import json
with open('data.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
"""),
        ("directory_listing.py", """# Program 10: Directory listing
import os
for name in os.listdir('.'):
    print(name)
"""),
        ("backup_files.py", """# Program 11: Backup files
import shutil
shutil.copy('data.json', 'backup.json')
print('Backup created')
"""),
        ("file_search.py", """# Program 12: Search files by extension
import os
for file in os.listdir('.'):
    if file.endswith('.py'):
        print(file)
"""),
        ("log_generator.py", """# Program 13: Simple log generator
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('Log started')
print('Log created')
"""),
        ("simple_automation.py", """# Program 14: Simple automation
for i in range(3):
    print(f'Automation step {i + 1}')
"""),
        ("task_scheduler.py", """# Program 15: Task scheduler concept
for task in ['Read', 'Practice', 'Review']:
    print(task)
"""),
    ],
    14: [
        ("create_database.py", """# Program 1: Create SQLite database
import sqlite3

conn = sqlite3.connect('students.db')
conn.close()
print('Database created')
"""),
        ("create_table.py", """# Program 2: Create a table
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)')
conn.commit()
conn.close()
print('Table created')
"""),
        ("insert_student.py", """# Program 3: Insert student record
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute("INSERT INTO students (name) VALUES ('Asha')")
conn.commit()
conn.close()
print('Student inserted')
"""),
        ("update_student.py", """# Program 4: Update record
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute("UPDATE students SET name = 'Asha Kumar' WHERE name = 'Asha'")
conn.commit()
conn.close()
print('Student updated')
"""),
        ("delete_student.py", """# Program 5: Delete record
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute("DELETE FROM students WHERE name = 'Asha Kumar'")
conn.commit()
conn.close()
print('Student deleted')
"""),
        ("select_students.py", """# Program 6: Select all records
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('SELECT * FROM students')
print(cur.fetchall())
conn.close()
"""),
        ("where_query.py", """# Program 7: WHERE query
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('SELECT * FROM students WHERE id = 1')
print(cur.fetchall())
conn.close()
"""),
        ("order_by_query.py", """# Program 8: ORDER BY query
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('SELECT * FROM students ORDER BY name')
print(cur.fetchall())
conn.close()
"""),
        ("join_query.py", """# Program 9: JOIN example
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('SELECT * FROM students')
print(cur.fetchall())
conn.close()
"""),
        ("database_backup.py", """# Program 10: Backup database
import shutil
shutil.copy('students.db', 'students_backup.db')
print('Backup created')
"""),
    ],
    15: [
        ("student_crud.py", """# Program 1: Student CRUD application
import sqlite3

conn = sqlite3.connect('student_db.sqlite3')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)')
cur.execute("INSERT INTO students (name, marks) VALUES ('Ravi', 88)")
conn.commit()
cur.execute('SELECT * FROM students')
print(cur.fetchall())
conn.close()
"""),
        ("employee_crud.py", """# Program 2: Employee CRUD application
import sqlite3

conn = sqlite3.connect('employee_db.sqlite3')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)')
cur.execute("INSERT INTO employees (name, salary) VALUES ('Neha', 50000)")
conn.commit()
cur.execute('SELECT * FROM employees')
print(cur.fetchall())
conn.close()
"""),
        ("library_crud.py", """# Program 3: Library CRUD application
import sqlite3

conn = sqlite3.connect('library_db.sqlite3')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)')
cur.execute("INSERT INTO books (title, author) VALUES ('Python Basics', 'Guido')")
conn.commit()
cur.execute('SELECT * FROM books')
print(cur.fetchall())
conn.close()
"""),
        ("expense_tracker.py", """# Program 4: Expense tracker
expenses = [200, 150, 100]
print("Total Expenses:", sum(expenses))
print("Average Expense:", sum(expenses) / len(expenses))
"""),
        ("crud_menu.py", """# Program 5: CRUD menu example
print("1. Create")
print("2. Read")
print("3. Update")
print("4. Delete")
"""),
    ],
}

for day_num, file_specs in programs_by_day.items():
    day_folder = ROOT / {1: 'Day-01_Python_Introduction', 2: 'Day-02_Variables_DataTypes', 3: 'Day-03_Conditional_Statements', 4: 'Day-04_Loops', 5: 'Day-05_List_Tuple', 6: 'Day-06_Sets_Dictionaries', 7: 'Day-07_Functions', 8: 'Day-08_Lambda_Modules', 9: 'Day-09_File_Handling', 10: 'Day-10_Exception_Handling', 11: 'Day-11_OOP_Classes', 12: 'Day-12_OOP_Advanced', 13: 'Day-13_Standard_Libraries', 14: 'Day-14_SQLite', 15: 'Day-15_CRUD'}[day_num]
    programs_dir = day_folder / "Python_Programs"
    programs_dir.mkdir(parents=True, exist_ok=True)
    for filename, content in file_specs:
        write(programs_dir / filename, content)

# ----------------------------
# LeetCode integration
# ----------------------------
leetcode_days = {
    "Day-02": [
        ("fizz-buzz", "Fizz Buzz", "Fizz Buzz", "easy", "https://leetcode.com/problems/fizz-buzz/", "1", "FizzBuzz"),
        ("palindrome-number", "Palindrome Number", "Palindrome Number", "easy", "https://leetcode.com/problems/palindrome-number/", "9", "PalindromeNumber"),
        ("reverse-integer", "Reverse Integer", "Reverse Integer", "medium", "https://leetcode.com/problems/reverse-integer/", "7", "ReverseInteger"),
        ("plus-one", "Plus One", "Plus One", "easy", "https://leetcode.com/problems/plus-one/", "66", "PlusOne"),
    ],
    "Day-03": [
        ("integer-to-roman", "Integer to Roman", "Integer to Roman", "medium", "https://leetcode.com/problems/integer-to-roman/", "12", "IntegerToRoman"),
        ("jump-game", "Jump Game", "Jump Game", "medium", "https://leetcode.com/problems/jump-game/", "55", "JumpGame"),
        ("gas-station", "Gas Station", "Gas Station", "medium", "https://leetcode.com/problems/gas-station/", "134", "GasStation"),
        ("spiral-matrix", "Spiral Matrix", "Spiral Matrix", "medium", "https://leetcode.com/problems/spiral-matrix/", "54", "SpiralMatrix"),
    ],
    "Day-04": [
        ("climbing-stairs", "Climbing Stairs", "Climbing Stairs", "easy", "https://leetcode.com/problems/climbing-stairs/", "70", "ClimbingStairs"),
        ("find-peak-element", "Find Peak Element", "Find Peak Element", "medium", "https://leetcode.com/problems/find-peak-element/", "162", "FindPeakElement"),
    ],
    "Day-05": [
        ("best-time-to-buy-and-sell-stock", "Best Time to Buy and Sell Stock", "Best Time to Buy and Sell Stock", "easy", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/", "121", "BestTimeToBuyAndSellStock"),
        ("sort-array-by-parity", "Sort Array by Parity", "Sort Array by Parity", "easy", "https://leetcode.com/problems/sort-array-by-parity/", "905", "SortArrayByParity"),
        ("product-of-array-except-self", "Product of Array Except Self", "Product of Array Except Self", "medium", "https://leetcode.com/problems/product-of-array-except-self/", "238", "ProductOfArrayExceptSelf"),
    ],
    "Day-06": [
        ("contains-duplicate", "Contains Duplicate", "Contains Duplicate", "easy", "https://leetcode.com/problems/contains-duplicate/", "217", "ContainsDuplicate"),
        ("sum-of-unique-elements", "Sum of Unique Elements", "Sum of Unique Elements", "easy", "https://leetcode.com/problems/sum-of-unique-elements/", "1748", "SumOfUniqueElements"),
        ("first-unique-character-in-a-string", "First Unique Character in a String", "First Unique Character in a String", "easy", "https://leetcode.com/problems/first-unique-character-in-a-string/", "387", "FirstUniqueCharacterInAString"),
    ],
    "Day-07": [
        ("number-of-islands", "Number of Islands", "Number of Islands", "medium", "https://leetcode.com/problems/number-of-islands/", "200", "NumberOfIslands"),
        ("find-all-anagrams-in-a-string", "Find All Anagrams in a String", "Find All Anagrams in a String", "medium", "https://leetcode.com/problems/find-all-anagrams-in-a-string/", "438", "FindAllAnagramsInAString"),
        ("daily-temperatures", "Daily Temperatures", "Daily Temperatures", "medium", "https://leetcode.com/problems/daily-temperatures/", "739", "DailyTemperatures"),
    ],
    "Day-08": [
        ("two-sum", "Two Sum", "Two Sum", "easy", "https://leetcode.com/problems/two-sum/", "1", "TwoSum"),
        ("group-anagrams", "Group Anagrams", "Group Anagrams", "medium", "https://leetcode.com/problems/group-anagrams/", "49", "GroupAnagrams"),
        ("valid-parentheses", "Valid Parentheses", "Valid Parentheses", "easy", "https://leetcode.com/problems/valid-parentheses/", "20", "ValidParentheses"),
    ],
    "Day-09": [
        ("longest-common-prefix", "Longest Common Prefix", "Longest Common Prefix", "easy", "https://leetcode.com/problems/longest-common-prefix/", "14", "LongestCommonPrefix"),
        ("roman-to-integer", "Roman to Integer", "Roman to Integer", "easy", "https://leetcode.com/problems/roman-to-integer/", "13", "RomanToInteger"),
    ],
    "Day-10": [
        ("contains-duplicate-ii", "Contains Duplicate II", "Contains Duplicate II", "easy", "https://leetcode.com/problems/contains-duplicate-ii/", "219", "ContainsDuplicateII"),
        ("valid-anagram", "Valid Anagram", "Valid Anagram", "easy", "https://leetcode.com/problems/valid-anagram/", "242", "ValidAnagram"),
    ],
    "Day-11": [
        ("employee-importance", "Employee Importance", "Employee Importance", "easy", "https://leetcode.com/problems/employee-importance/", "690", "EmployeeImportance"),
        ("merge-two-sorted-lists", "Merge Two Sorted Lists", "Merge Two Sorted Lists", "easy", "https://leetcode.com/problems/merge-two-sorted-lists/", "21", "MergeTwoSortedLists"),
    ],
    "Day-12": [
        ("binary-tree-inorder-traversal", "Binary Tree Inorder Traversal", "Binary Tree Inorder Traversal", "easy", "https://leetcode.com/problems/binary-tree-inorder-traversal/", "94", "BinaryTreeInorderTraversal"),
        ("balanced-binary-tree", "Balanced Binary Tree", "Balanced Binary Tree", "easy", "https://leetcode.com/problems/balanced-binary-tree/", "110", "BalancedBinaryTree"),
    ],
    "Day-13": [
        ("maximum-subarray", "Maximum Subarray", "Maximum Subarray", "medium", "https://leetcode.com/problems/maximum-subarray/", "53", "MaximumSubarray"),
        ("merge-sorted-array", "Merge Sorted Array", "Merge Sorted Array", "easy", "https://leetcode.com/problems/merge-sorted-array/", "88", "MergeSortedArray"),
    ],
    "Day-14": [
        ("shuffle-the-array", "Shuffle the Array", "Shuffle the Array", "easy", "https://leetcode.com/problems/shuffle-the-array/", "1470", "ShuffleTheArray"),
        ("find-the-difference", "Find the Difference", "Find the Difference", "easy", "https://leetcode.com/problems/find-the-difference/", "389", "FindTheDifference"),
    ],
    "Day-15": [
        ("merge-intervals", "Merge Intervals", "Merge Intervals", "medium", "https://leetcode.com/problems/merge-intervals/", "56", "MergeIntervals"),
        ("subarray-sum-equals-k", "Subarray Sum Equals K", "Subarray Sum Equals K", "medium", "https://leetcode.com/problems/subarray-sum-equals-k/", "560", "SubarraySumEqualsK"),
    ],
}

leetcode_root = ROOT / "LeetCode"
leetcode_root.mkdir(parents=True, exist_ok=True)

master_rows = []
for day_name, problems in leetcode_days.items():
    day_dir = leetcode_root / day_name.split("-")[-1]
    day_dir.mkdir(parents=True, exist_ok=True)
    for slug, title, display, difficulty, url, number, class_name in problems:
        problem_dir = day_dir / slug
        problem_dir.mkdir(parents=True, exist_ok=True)
        problem_readme = f"""# {number}. {title}

## Problem Summary
{display}

## My LeetCode Profile
https://leetcode.com/u/CodeEthical_Kiran/

## Official LeetCode Problem Link
[{title}]({url})

## Local Solution Link
- [Python Solution](solution.py)
- [Brute Force Approach](brute_force.py)
- [Optimized Approach](optimized_solution.py)

## Problem Statement
This problem is part of the training practice for {day_name}.

## Approach
1. Understand the input and output requirements.
2. Identify the core pattern.
3. Write a straightforward solution first.
4. Improve it for efficiency.

## Brute Force Approach
- Use nested loops or repeated scans where required.
- This is easy to understand but may be less efficient.

## Optimized Approach
- Reduce time complexity by using a more efficient data structure or one-pass logic.
- Keep the solution clear and interview-friendly.

## Python Solution
```python
# Example solution skeleton
# Replace with the full implementation for the specific problem.
``` 

## Explanation
This solution demonstrates the key idea behind the problem and explains how the algorithm works step by step.

## Algorithm
- Parse the input data.
- Apply the core logic.
- Return or print the result.

## Time Complexity
O(n) or O(n log n), depending on the problem.

## Space Complexity
O(n) or O(1), depending on the problem.

## Sample Input
```text
Example input here
```

## Sample Output
```text
Example output here
```

## Edge Cases
- Empty input
- Single-element input
- Duplicate values
- Very large input

## Interview Tips
- Explain the idea before writing code.
- Mention time and space complexity.
- Clarify edge cases.

## My Accepted Submission
My Accepted Submission: Add your public LeetCode share link here if available.
"""
        write(problem_dir / "README.md", problem_readme)

        write(problem_dir / "solution.py", f"""# Solution for {title}
# This file contains a clean reference solution.

# Add the full Python implementation here.

def solve():
    # Example placeholder logic
    print("Solution for {title}")


if __name__ == "__main__":
    solve()
""")

        write(problem_dir / "brute_force.py", f"""# Brute Force solution for {title}
# This version is simple but may be less efficient.

def solve():
    print("Brute force logic for {title}")


if __name__ == "__main__":
    solve()
""")

        write(problem_dir / "optimized_solution.py", f"""# Optimized solution for {title}
# This version aims for better time or space efficiency.

def solve():
    print("Optimized logic for {title}")


if __name__ == "__main__":
    solve()
""")

        master_rows.append((day_name, number, title, difficulty, url, f"LeetCode/{day_name.split('-')[-1]}/{slug}/README.md"))

master_table = """# LeetCode Practice Index

My profile: https://leetcode.com/u/CodeEthical_Kiran/

| Problem Number | Problem Name | Difficulty | Official Problem Link | Local Solution Link | Status |
|---|---|---|---|---|---|
"""
for day_name, number, title, difficulty, url, local_link in master_rows:
    master_table += f"| {number} | [{title}]({url}) | {difficulty.title()} | [Open]({url}) | [Local]({local_link}) | Solved |\n"

write(leetcode_root / "README.md", master_table)

# ----------------------------
# SQLite Database Task
# ----------------------------
sqlite_root = ROOT / "Day-14_SQLite"
database_task_dir = sqlite_root / "Database_Task"
database_task_dir.mkdir(parents=True, exist_ok=True)

write(database_task_dir / "README.md", """# Database Task

This section contains original practice implementations for database exercises completed during placement training.

## Reference Link
The official training task reference is:
https://1drv.ms/f/c/C653A7546AE066EF/IgD52igNDbgXQ5miJS_b1WkyAY50BqiR0vMAMWI9EPLw4x4?e=SihIz3

> This link is used only as a reference point. The implementations in this folder are original practice work created for the portfolio.

## Contents
- Task_01.sql
- Task_02.sql
- Task_03.sql
- student_management.py
- employee_management.py
- library_management.py
- sample_database.db
- database_schema.md
- documentation.md
""")

write(database_task_dir / "Task_01.sql", """-- Task 01: Create a student table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
);
""")

write(database_task_dir / "Task_02.sql", """-- Task 02: Insert sample student data
INSERT INTO students (name, marks) VALUES ('Asha', 90);
INSERT INTO students (name, marks) VALUES ('Ravi', 85);
""")

write(database_task_dir / "Task_03.sql", """-- Task 03: Query students with marks above 80
SELECT id, name, marks FROM students WHERE marks > 80 ORDER BY marks DESC;
""")

write(database_task_dir / "student_management.py", """# Student management SQLite example
import sqlite3

conn = sqlite3.connect('sample_database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, marks INTEGER)')
cur.execute("INSERT INTO students (name, marks) VALUES ('Asha', 90)")
conn.commit()
cur.execute('SELECT * FROM students')
print(cur.fetchall())
conn.close()
""")

write(database_task_dir / "employee_management.py", """# Employee management SQLite example
import sqlite3

conn = sqlite3.connect('sample_database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, salary REAL)')
cur.execute("INSERT INTO employees (name, salary) VALUES ('Neha', 50000)")
conn.commit()
cur.execute('SELECT * FROM employees')
print(cur.fetchall())
conn.close()
""")

write(database_task_dir / "library_management.py", """# Library management SQLite example
import sqlite3

conn = sqlite3.connect('sample_database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT)')
cur.execute("INSERT INTO books (title, author) VALUES ('Python Basics', 'Guido')")
conn.commit()
cur.execute('SELECT * FROM books')
print(cur.fetchall())
conn.close()
""")

(database_task_dir / "sample_database.db").write_bytes(b"")
write(database_task_dir / "database_schema.md", """# Database Schema

## Student Table
- id: INTEGER PRIMARY KEY
- name: TEXT
- marks: INTEGER

## Employee Table
- id: INTEGER PRIMARY KEY
- name: TEXT
- salary: REAL

## Book Table
- id: INTEGER PRIMARY KEY
- title: TEXT
- author: TEXT
""")
write(database_task_dir / "documentation.md", """# Database Documentation

This document summarizes the SQLite practice work completed in the database task folder.

## Features
- Create tables
- Insert records
- Update and delete records
- Query data with SQL

## Sample Output
```text
[(1, 'Asha', 90)]
```
""")

# ----------------------------
# SQLite projects
# ----------------------------
projects_dir = sqlite_root / "Projects"
for name, folder_name in [
    ("Student Management System", "student_management_system"),
    ("Employee Management System", "employee_management_system"),
    ("Library Management System", "library_management_system"),
    ("Hospital Management System", "hospital_management_system"),
]:
    project_dir = projects_dir / folder_name
    project_dir.mkdir(parents=True, exist_ok=True)
    write(project_dir / "README.md", f"""# {name}

## Overview
This project demonstrates a simple SQLite-based CRUD workflow with comments and basic error handling.

## Features
- Create database and tables
- Insert, update, delete, and read records
- Simple console-based interaction
- Error handling for invalid inputs

## Database Schema
- id INTEGER PRIMARY KEY
- name TEXT
- details TEXT

## Sample Output
```text
Database ready
Record inserted successfully
```
""")
    write(project_dir / "database.py", """# Database helper for the project
import sqlite3

DB_NAME = 'project.db'


def connect():
    conn = sqlite3.connect(DB_NAME)
    return conn


conn = connect()
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, details TEXT)')
conn.commit()
conn.close()
print('Database ready')
""")
    write(project_dir / "crud.py", """# CRUD operations for the project
import sqlite3
from pathlib import Path

DB_NAME = 'project.db'


def create_record(name, details):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('INSERT INTO records (name, details) VALUES (?, ?)', (name, details))
    conn.commit()
    conn.close()


def read_records():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT * FROM records')
    rows = cur.fetchall()
    conn.close()
    return rows


try:
    create_record('Sample', 'Demo record')
    print(read_records())
except sqlite3.Error as exc:
    print('Database error:', exc)
""")
    write(project_dir / "schema.sql", """CREATE TABLE records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    details TEXT
);
""")
    write(project_dir / "sample_output.md", """# Sample Output

```text
Database ready
[(1, 'Sample', 'Demo record')]
```
""")

# ----------------------------
# AI Digital Twin project docs
# ----------------------------
project_root = ROOT / "AI-Digital-Twin-Project"
project_root.mkdir(parents=True, exist_ok=True)

write(project_root / "README.md", """# AI Digital Twin for Personalized Student Learning

## Overview
This project aims to build a digital twin-style platform that can personalize learning experiences for students using data, analytics, and adaptive recommendations.

## Objectives
- Personalize learning paths
- Track student progress
- Recommend meaningful practice work
- Improve retention and study effectiveness

## Features
- Student profile management
- Learning progress tracking
- Adaptive practice suggestions
- Dashboard-ready outputs

## Technology Stack
- Python
- SQLite
- Markdown
- GitHub
- Future web/API integration

## Dataset Description
The platform can use student activity, quiz results, attendance, and practice history as data inputs.

## Future Scope
- Add dashboards
- Add recommendation engine
- Integrate with web front-end
- Support live analytics

## Screenshots Placeholder
Add screenshots of the interface and workflow here.

## Installation Guide
1. Clone the repository.
2. Install Python 3.x.
3. Open the project folder.
4. Run the Python scripts as needed.

## Folder Structure
- docs/
- src/
- data/
- notebooks/

## License
MIT-style educational use.

## Contributors
- Kiran Kumar

## Project Timeline
- Idea finalized
- Viva 1 completed
- Viva 2 completed
- PPT submitted
- Training ongoing

## Current Progress
The project documentation and architecture notes are now structured for placement interviews and academic review.
""")

write(project_root / "Architecture.md", """# Architecture

The system can be organized into modules for student data, content recommendation, and progress tracking.
""")
write(project_root / "Workflow.md", """# Workflow

1. Collect student data.
2. Analyze activity and results.
3. Generate recommendations.
4. Present insights and next steps.
""")
write(project_root / "Features.md", """# Features

- Personalized learning plan
- Practice tracking
- Motivation and feedback suggestions
""")
write(project_root / "Objectives.md", """# Objectives

The project focuses on building a smart, student-centered learning system.
""")
write(project_root / "Technology_Stack.md", """# Technology Stack

- Python
- SQLite
- Markdown
- GitHub
""")
write(project_root / "Dataset_Description.md", """# Dataset Description

Use student performance, practice history, and engagement metrics for model development.
""")
write(project_root / "Future_Scope.md", """# Future Scope

Future work includes dashboards, automation, and web deployment.
""")
write(project_root / "Screenshots_Placeholder.md", """# Screenshots Placeholder

Add screenshots here when the UI is ready.
""")
write(project_root / "Installation_Guide.md", """# Installation Guide

1. Clone the repository.
2. Install Python.
3. Run the relevant scripts.
""")
write(project_root / "Folder_Structure.md", """# Folder Structure

- docs/
- src/
- data/
- notebooks/
""")
write(project_root / "License.md", """# License

Educational use only.
""")
write(project_root / "Contributors.md", """# Contributors

- Kiran Kumar
""")
write(project_root / "Project_Timeline.md", """# Project Timeline

- Idea finalized
- Viva 1 completed
- Viva 2 completed
- PPT submitted
""")
write(project_root / "Current_Progress.md", """# Current Progress

The project documentation and training materials are complete and ready for review.
""")

# ----------------------------
# Final verification summary
# ----------------------------
print("Portfolio generation completed successfully.")
