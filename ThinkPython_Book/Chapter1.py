#Problem Solving trait is crucial in computer science!!!

#1.1 The Python Programming Language--------------------------------------------------
"""
Python is a high-level programming language with other high-level languages such as C++, C# and Java. In addition, high-level languages are portable and easier to code.

Low-Level languages are "machine languages" or "assembly languages" which are only used in computers. Programs written in high-level languages are procssed into low-level languages before being executed.

An interpreter processes the program by reading lines and performing computations. While a compiler translates the code into an object code, which is run by hardware executers (hardware executers are also called CPU).

Python is an interpreted language. It has an interactive mode and a script mode. In interactive mode, you type the program then the interpreter displays the result. Meanwhile, the script mode stores code in a file (a script) which normally ends with .py extensions.
"""

#1.2 What is a Program?--------------------------------------------------------------
"""
A program is a sequence of instructions that tell the computer what to do.

input: Getting data from the user.
output: Displaying data to the user.
math: Performing basic arithmetic operations.
conditional execution: check certain conditions and execute a block of code based on the condition.
repetition (loop): performing the same task multiple times.
"""

#1.3 What is Debugging?--------------------------------------------------------------
"""
In programming, we will encounter bugs (programming errors) and the process to track them down is called debugging. Errors that often occur are; syntax errors, runtime errors, logical errors, and semantic errors.

Syntax errors: Errors in the structure and rule of the code (syntax).

Runtime errors: Errors that occur during the execution of the code (runtime).

Logical errors: Errors in the logic of the code (logical).

Semantic errors: Errors that occur due to the meaning of the code (semantic). The program will run with no error but not the way we expect it to run.

Experimental Debugging: The process of finding and fixing errors in the code during the development of a program.

"When you have eleminated the impossible, whatever remains, however improbable, must be the truth." (A. Conan Doyle, The Sign of Four)
"""

#1.4 Formal and Natural Languages-------------------------------------------------
"""
Natural Languages: Languages that humans use to communicate such as English, Japanese, French, etc.

Formal Languages: Languages that are designed for specific purposes such as computer programming languages. "Programming languages are formal languages that have been designed to express computations"

Exercise 1.1
Write a well-structured English sentence with invalid tokens in it. Then, write another sentence with all valid tokens but with invalid structure.

Answer:
Invalid Tokens Well-Structured English Sentence:
tHe quick $rown fox (jumps over) th+ lazy dog.

Valid Tokens Invalid Structure English Sentence:
Fox brown dog jumps the the quick over lazy.

When you read the sentence, you would have to figure out the structure of the sentence, this is called parsing.

Differences in Formal and Natural Languages:
Ambiguity: Ambiguity is the state of having more than one possible meaning for a word or phrase. Natural languages have a lot of ambiguity while formal languages do not with a sole purpse of representing one meaning for any statement.

Redundancy: Redundancy is the state of having more than one possible meaning for a word or phrase. Redundancy is the opposite of ambiguity. Natural languages have lots of redundancy while formal languages do not and are more concise.

Literalness: Literalness is the state of having a single meaning for a word or phrase. Literalness is the opposite of redundancy. Natural languages are more literal while formal languages means exactly what you say.
"""

#1.5 The First Program---------------------------------------------------------------
print("Hello World!")

"""
Used the print statement to print "Hello World!" which just displays the string value.
"""

#1.6 Debugging-----------------------------------------------------------------------
"""
We will face struggles with a difficult bug as people naturally respond to computer as if they were humans.

So, your job is to be a good manager and find the best ways to resolve the problem.
"""

#1.7 Glossary------------------------------------------------------------------------
"""
Problem Solving: The process of formulating a problem and finding a solution to it.

High-Level Programming Language: A programming language that is high-level and easy to understand.

Low-Level Programming Language: A programming language that is low-level and easy to understand for computers.

Portability: The ability of a programming language to be used on multiple platforms.

Interpreter: A program that processes a program written in a high-level language and then executes it.

Compiler: A program that translates a program written in a high-level language into a low-level language and then executes it.

Source code: The code written in a programming language.

Object code: The code generated by the compiler.

Executable code: The code that is executed by the interpreter.

Prompt: A message that is displayed to the user when the interpreter is waiting for input.

Script: A file that contains code written in a programming language.

Interactive mode: The process of getting input from the user and displaying the output.

Script mode: The process of getting input from a file and displaying the output.

Program: A sequence of instructions that tell the computer what to do.

Algorithm: A sequence of instructions that tell the computer what to do.

Bug: An error in a program.

Syntax: The structure and rule of the code.

Syntax error: An error in the structure and rule of the code.

Exception: An error that occurs during the execution of the code.

Semantics: The meaning of the code.

Semantic error: An error that occurs due to the meaning of the code.

Natural Language: A language that humans use to communicate.

Formal Language: A language that is designed for specific purposes.

Token: A word or phrase in a programming language.

Parse: To examine a program and determine its structure.

Print: To display a message to the user.
"""

#1.8 Exercises------------------------------------------------------------------
"""
Exercise 1.2
Use a web browser to go to the Python website http: // python. org . This page
contains information about Python and links to Python-related pages, and it gives you the ability to
search the Python documentation.

Exercise 1.3
Start the Python interpreter and type help() to start the online help utility. Or you
can type help('print') to get information about the print statement. If this example does not work, you may need to install additional Python documentation or set an
environment variable; the details depend on your operating system and version of Python

Exercise 1.4
Start the Python interpreter and use it as a calculator. Python’s syntax for math
operations is almost the same as standard mathematical notation. For example, the symbols +, - and
/ denote addition, subtraction and division, as you would expect. The symbol for multiplication is
*.
If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What
is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).
"""

#Exercise 1.4 Answer
km = 10
miles = km * 1.61
time = 43 * 60 + 30
avg_time = "{:.4f}".format(time / miles)
avg_speed = "{:.4f}".format(miles / time)

print("Average time per mile", avg_time)
print("Average speed in miles per hour", avg_speed)
#Added {:.4f} to print the result with 4 decimal places, used format function.