#############################
# TASK:
#
# 1. Declare 3 variables: one of type int, one of type double, and one of type String.
# 2. Read 3 lines of input from stdin and initialize your 3 variables.
# 3. Use the + operator to perform the following operations:
#
#     a. Print the sum of i plus your int variable on a new line.
#     b. Print the sum of d plus your double variable to a scale of one decimal place on a new line.
#     c. Concatenate s with the string you read as input and print the result on a new line.
#
#
# Input Format
# * The first line contains an integer that you must sum with i
# * The second line contains a double that you must sum with d.
# * The third line contains a string that you must concatenate with s
#
# Output Format
# * Print the sum of both integers on the first line, the sum of both doubles (scaled to 1
# decimal place) on the second line, and then the two concatenated strings on the third line.
#
# Sample Input
# 12
# 4.0
# is the best place to learn and practice coding!
#
# Sample Output
# 16
# 8.0
# HackerRank is the best place to learn and practice coding!

#############################


i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.


# Read and save an integer, double, and String to your variables.
in_int = int(input())
in_double = float(input())
in_str = str(input())

# Print the sum of both integer variables on a new line.
print(i+in_int)
# Print the sum of the double variables on a new line.
print(round(d+in_double, 1)) # rounded to 1 decimal
# Concatenate and print the String variables on a new line
print(s + in_str)
