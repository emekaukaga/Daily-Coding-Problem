# This is for the September 8, 2024 "Daily Coding Problem: Problem #1 [Easy]" from www.dailycodingproblem.com.
# Prompt: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

########################################
########################################

# OVERVIEW: HERE IS MY ATTEMPT AT A SOLUTION

# I am assuming that the array and sum value will be pass through from the environment to the function.
# I am providing a simple function to sum each value in array "numbers" and test against the sum value "k".

### ASSUMPTIONS + EDGE CASES

# If the solution wants there to be a chance to input both the sum value and array values, then
# my solution would include an evaluation for edge cases where non-integers, variables, and other
# inputs were improperly submitted. Additionally, I would need to evaluate to ensure that the array is
# input correctly with numbers separated by commas. If the array was input in a column instead of a row
# I would include a quick fix to transpose this for the user with an alert that this was done.
# Otherwise, I would kick an error message asking for the user to input the array correctly.
