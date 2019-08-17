

# Declare integer, double, and String variables.

i = 4
d = 4.0
s = 'Yellow '

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

# Sample Input
# 12
# 4.0
# is Lovely
#
# Sample Output
# 16
# 8.0
# Yellow is Lovely
