# PRIMM: Predict Activity
#
# Instructions: Read the following Python code snippet. Without running it,
# predict the final value and data type for the variables `result_1` and `result_2`.
# Write down your prediction and your reasoning in the comments below.

# Variables for calculation
num_items = 15
price_per_item = 4.50
shipping_cost = 10

# Calculate the results
result_1 = num_items * price_per_item + shipping_cost
result_2 = num_items * (price_per_item + shipping_cost)

# --- Your Prediction ---
#
# `result_1` Value: 77.5
# `result_1` Data Type: float
# Reasoning: the reason why i got these predictions is because 15 x 4.5 = 67.5 +10 =77.5.
# Then i got the data type from the data types being used being: float * int=float then, float + int=float, and if float is in the equation it will become a float type.
#
# `result_2` Value: 217.5
# `result_2` Data Type: float
# Reasoning: the reason why i got these predictions is because (10 + 4.5)= 14.5 15 * 14.5 =217.5.
# Then i got the data type from the data types being used being: (float + int)=float then, float * int = float, and if float is in the equation it will become a float type.




# PRIMM: Predict Activity
#
# Instructions: Read the following Python code snippet. Without running it,
# predict the final value for the variables `minutes` and `seconds`.
# Write down your prediction and a brief explanation in the comments below.

# A total duration in seconds
total_seconds = 395

# Convert to minutes and seconds
minutes = total_seconds // 60
seconds = total_seconds % 60

# --- Your Prediction ---
#
# `minutes` Value: 6
# `seconds` Value: 35
# Reasoning: // is a division so 395 divided by 60 would equal 6. We can also check this by multiplying 60 x 6 = 360.
# then for the seconds we can take 395 and do % 60 which would equal 35 which is the remainder of 395/60
