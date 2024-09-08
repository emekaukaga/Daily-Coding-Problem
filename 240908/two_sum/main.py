# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Emeka!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


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

########################################
########################################

# Defining array to be passed through "numbers" as well as sum value "k"
#numbers = [10, 15, 3, 7]
#k = 17

# Calling function "two_sum" to evaluate the array "numbers" and sum value "k"

def two_sum(numbers, k):
    # Adding input validation and error handling for code first.

    # Check if 'numbers' is a list
    if not isinstance(numbers, list):
        raise ValueError("Input 'numbers' must be a list of integers.")

    # Check if 'k' is a number
    if not isinstance(k, (int, float)):
        raise ValueError("Input 'k' must be a number.")

    # Check if all elements in the list are integers or floats
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError(f"All elements in 'numbers' must be integers or floats. Found: {num}")

    # Check if the list has at least two elements
    if len(numbers) < 2:
        return False  # No pairs can be formed from fewer than 2 numbers

    # Now moving into evaluating function

    check_set = set()  # Initialize an empty set to store numbers

    for x in numbers:
        complement = k - x  # Calculate complement

        if complement in check_set:  # Check if complement exists in set
            return True  # Pair found, return True

        check_set.add(x)  # Add the current number to the set

    return False  # If no pair is found, return False

#def two_sum(numbers, k):
#    # If any two values in array "numbers" add up to "k" will output result.
#    for x in numbers:
#        check_set.append(x)
#        #print(check_set)
#        complement = k-x
#    # If no two values in array "numbers" add up to "k" will output null message.
#    pass

# Now I am entering the testing stage.

# Defining function to pause in between program tests.
def wait_for_user():
    input("Press Enter to continue...")

print("Would you like to test with valid inputs? k=17 and numbers = [10, 15, 3, 7]?")
wait_for_user()  # Pauses the program until the user presses Enter

# Test with valid inputs
numbers = [10, 15, 3, 7]
k = 17
result = two_sum(numbers, k)
print(result)  # Expected output: True

print("Note: Looking good! Would you like to test with invalid inputs? k=17 and numbers = [10, '15', 3, 7]?")
wait_for_user()  # Pauses the program until the user presses Enter

# Test with invalid input (non-numeric)
try:
    numbers = [10, '15', 3, 7]
    k = 17
    result = two_sum(numbers, k)
except ValueError as e:
    print(e)  # Expected output: Error message about non-integer

print("Note: Looks like it's catching those errors! Would you like to finally test with an empty list? k=17 and numbers = []?")
wait_for_user()  # Pauses the program until the user presses Enter

# Test with an empty list
numbers = []
k = 17
result = two_sum(numbers, k)
print(result)  # Expected output: False (since no pairs can be found)

print("Note: Nice work! Looks like everything is in order. :)")