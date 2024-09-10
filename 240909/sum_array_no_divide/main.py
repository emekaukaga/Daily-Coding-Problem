# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('there! Welcome to my solution for the September 9, 2024 Daily Challenge!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Defining the array we will use for the problem as well as product array
array = [1, 2, 3, 4, 5]
#array_product = [1, 1, 1, 1, 1]
array_product = [1] * len(array)

# Passing arrays through loop multiplying by all numbers to the left of the index "i"
left_product =1
for i in range(len(array)):
    # print(array[i])
    # print(array_product[i])
    array_product[i] = left_product
    left_product *= array[i]

# Passing arrays through loop multiplying by all numbers to the right of the index "i"
right_product = 1
for i in range(len(array) - 1, -1, -1):
    # print(array[i])
    # print(array_product[i])
    array_product[i] *= right_product
    right_product *= array[i]

print(array_product)