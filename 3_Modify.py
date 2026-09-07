# PRIMM: Modify Activity
#
# Instructions: Here is a program that converts a temperature from Celsius to Fahrenheit.
# For each modification below, first predict the outcome in the comments,
# then make the change to the code and run it to verify your prediction.

# --- Original Code ---
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")


# --- Modification 1 ---
# Change the formula to convert from a starting `fahrenheit` value of 77 to `celsius`.
# The formula for that is `(fahrenheit - 32) * 5/9`.
#
# Prediction: The result from (77 - 32) * 5/9 will equal the 25 celcius in the original source code because you are reversing the operation
# Verified Result: the program prints that the 77 degrees fahrenheit does indeed equal 25 degrees cecius when the equation takes place


# --- Modification 2 ---
# Go back to the original code. Change the `celsius` variable to `25.5`.
#
# Prediction: What will the new Fahrenheit value be? The fahrenheit value will 77.9 or higher. Will the data type of the `fahrenheit` variable change? No the data type will not change as it is still a float type by "/" being used
# Verified Result: The Fahrenheit value did increase to 77.9 and the data type did reamin the same.


# --- Modification 3 ---
# Go back to the original code. Try to "break" the program by changing the calculation
# to `fahrenheit = (celsius * "9/5") + 32`. Notice the quotes around `9/5`.
#
# Prediction: What kind of error do you think this will cause and why? This will most likely cause a type error due to incompatible types being used.
# Verified Result: A type error did occur by the error message saying that an int type cant be multipied by a string(the "9/5")
