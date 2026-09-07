# PRIMM: Investigate Activity
#
# Instructions: Now, let's investigate the code from the first Predict activity.
# Run this file and then answer the questions in the comments below.

# Variables for calculation
num_items = 15
price_per_item = 4.50
shipping_cost = 10

# Calculate the results
result_1 = num_items * price_per_item + shipping_cost
result_2 = num_items * (price_per_item + shipping_cost)

print(f"Result 1 is: {result_1}, Type: {type(result_1)}")
print(f"Result 2 is: {result_2}, Type: {type(result_2)}")


# --- Answer the following questions ---
#
# 1.  In the calculation for `result_1`, which operation happens first:
#     the multiplication (`*`) or the addition (`+`)? Why does Python
#     choose this order? (This is called "operator precedence").
#
#     Your Answer: The operation that happens first is multiplication. This is because the operation gets executed based on the order of operation going from
#     parenthesis, exponents, multiplication/division, add/subtract from left to right on the code line, with multiplication happening before addition because of its operator precedence.
#
# 2.  What is the data type of `result_1`? Why is it that type, even though
#     `num_items` and `shipping_cost` are integers?
#
#     Your Answer: The data type of result_1 is float. The reason why it is float is because, even if integers are there, if the type float is present the outcome will become a float automatically.
#
# 3.  How do the parentheses `()` in the calculation for `result_2` change
#     the order of operations compared to `result_1`?
#
#     Your Answer: The parentheses in Result_2 change the order of operations by overiding the usual left to right order to instead do the parathesis first then do revert back to left to right.


# PRIMM: Investigate Activity
#
# Instructions: Let's investigate a program that calculates the area of a circle.
# Run this file and then answer the questions in the comments below.

import math

radius = 7
area = math.pi * radius ** 2

print(f"The area of a circle with radius {radius} is {area}")


# --- Answer the following questions ---
#
# 1.  What does the `import math` line do? What do you predict would happen
#     if you deleted that line and tried to run the code?
#
#     Your Answer:The import math line imports the math module of python allowing for commands like math.pi to be available.
#     if import math were to be removed then the code would instead bring up an error because the pi command wouldn't work.
#
# 2.  What is `math.pi`? Based on how it's used, do you think it is a
#     function or a variable defined inside the `math` module?
#
#     Your Answer:math.pi is a function that is made to represent the pi symbol in math. The Variable math.pi is a variable because it has no parentheses.
#
# 3.  In the expression `math.pi * radius ** 2`, which operation happens first:
#     the multiplication (`*`) or the exponentiation (`**`)? How could you confirm this?
#
#     Your Answer: The exponent ** happens first because it it higher on the order of operations than multiplication(*).
#     You can confirm this by using parantheses on radius ** 2 to get the same result or by doing a simple equation such as 3 * 10**2 and seeing the results
