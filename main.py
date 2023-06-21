#ASSINGMENT 3
""""
1. Why are functions advantageous to have in your programs?

Overall, functions improve code structure, promote reusability, enhance readability, simplify maintenance,
and support collaboration, making them a valuable asset in program development.
They help in managing complexity, reducing errors, and improving the overall efficiency
and maintainability of your codebase.
"""
"""
2,when code in a function runs when the function is called, not when it is specified or defined.

When you define a function in your code, you are essentially creating a reusable block of code that contains a set of 
instructions to perform a specific task. The code inside the function is not executed at the point of definition; 
instead, it is executed when the function is called or invoked.
"""

""""
3. What statement creates a function?

the def statement is followed by the function name, a set of parentheses, and a colon. 
This defines the function's signature.
"""

""""
4. What is the difference between a function and a function call?

function is like a pre-defined set of instructions that performs a specific task or operation. 
It is created by defining the function's name, parameters (if any), and code block.
On the other hand, a function call is when you actually use the function by invoking it.
It's like pressing the "start" button on a machine. The function call provides any necessary inputs and triggers
the execution of the code within the function's block. Functions give structure and define behavior,
while function calls make those functions actually run at particular points in the program.
"""
"""
5. How many global scopes are there in a Python program? How many local scopes?

there is usually one global scope in a Python program, which exists outside of any function or class.
The number of local scopes depends on the number of functions or blocks of code that create their own scopes.
"""
"""
6. What happens to variables in a local scope when the function call returns?

when a function call returns in Python, the variables within the local scope of that function are destroyed,
freeing up memory, and they cannot be accessed or used outside the function.
"""
"""
7. What is the concept of a return value? Is it possible to have a return value in an expression?

the return value in programming represents the value that a function sends back to the caller to communicate 
the result of its execution. It allows functions to provide output or results,
and it is captured using the return statement. 
The return value can be assigned to variables and used in expressions as needed.

it is not possible to have a return value in an expression itself. The return statement is used within a function
to explicitly specify the value to be returned. It cannot be directly used within an expression outside of a function
to capture the value. However, you can assign the return value to a variable,
which can then be used within an expression.
"""
"""
8.If a function does not have a return statement, what is the return value of a call to that function?

If a function does not have a return statement, the return value of a call to that function is None.
When a function is called without a return statement, it automatically returns None by default.
This means that if you assign the result of a function call that lacks a return statement to a variable,
that variable will hold the value None.

a function does not have a return statement, the return value of a call to that function is None.
"""
"""
9. How do you make a function variable refer to the global variable?

to make a function variable refer to the global variable in Python, you can use the global keyword inside the function.
This keyword allows you to indicate that a variable should be treated as a global variable.

"""
"""
10. what is none datatype?

None is a special constant object in Python that represents the absence of a value or the lack of a specific value.
It is often used to indicate the absence of a meaningful result or to initialize variables
before they are assigned a valid value.
"""
"""

11. What does the sentence import areallyourpetsnamederic do?

attempts to import a module or package named areallyourpetsnamederic.

"""
"""
12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

spam.bacon()
"""
"""
13. What can you do to save a programme from crashing if it encounters an error?

To save a program from crashing when it encounters an error, you can implement error handling techniques.
In Python, you can use try-except blocks to catch and handle exceptions that may occur during program execution.
"""

"""
14. What is the purpose of the try clause? What is the purpose of the except clause?

try clause allows you to execute code that may potentially raise an exception,
and the except clause provides a mechanism to catch and handle specific exceptions,
allowing you to gracefully manage errors and exceptions in your program.

"""
