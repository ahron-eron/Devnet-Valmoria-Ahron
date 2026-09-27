"""
LESSON 4: FUNCTIONS IN PYTHON

--- Topic Explanation ---
Functions are named shortcuts for blocks of code you want to reuse.
Instead of copying and pasting the same 5 lines of code every time you need 
something done, you put those lines inside a function and just call its name.

Main Information
- They start with the 'def' keyword.
- You can feed them data to work with (parameters).
- They can hand back a final result when they finish working (return values).

--- Vocabulary ---
- Function: A named block of reusable code.
- Parameter: The variable placeholder defined in the function signature (e.g., 'def greet(name):' -> name is the parameter).
- Argument: The actual value you pass into the function when calling it (e.g., 'greet("Ahron")' -> "Ahron" is the argument).
- Return Value: The value the function gives back using the 'return' statement.
- Local Scope: Variables created inside a function only exist inside that function.
"""

# Function that prints a greeting and calling the function
def say_hello():
    print("Hey there! Welcome to the DevNet lab.")

say_hello()


# A function that takes input and returns a result as well as testing
def calc_discount(price, discount_percent=10):
    """Calculates the price after applying a percentage discount."""
    savings = price * (discount_percent / 100)
    final_price = price - savings
    return final_price

original_price = 250.0
sale_price = calc_discount(original_price, 20)
print(f"Original: ${original_price} | Sale Price: ${sale_price}")


# Quick utility function returning a boolean
def is_even(number):
    return number % 2 == 0

print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")


# --- My mistakes and reflection ---
"""
I tried to execute my function by writing just its name without parentheses. Instead of running the code, Python printed something like 
'<function say_hello at 0x7f8b...>'.

What I learned:
Writing a function's name without parentheses references the function object itself rather 
than executing it. The parentheses '()' are the trigger that tells Python to actually call 
and run the code inside.
"""
