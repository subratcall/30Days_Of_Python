
def solve(meal_cost, tip_percent, tax_percent):

    tip_amount = meal_cost * tip_percent / 100

    tax_amount = meal_cost * tax_percent / 100

    total_cost = round(meal_cost + tip_amount + tax_amount)

    print("The total meal cost is " + str(total_cost) + " dollars.")


if __name__ == '__main__':

    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

# Sample Input
# 12.00
# 20
# 8
#
# Sample Output
# 15
