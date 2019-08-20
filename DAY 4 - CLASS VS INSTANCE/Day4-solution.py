class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0..")
            self.age = 0
        else:
            self.age = initialAge

    def yearPasses(self):
        self.age += 1 # Note: i++ way of incrementing like java doesnt work in python
        # Increment the age of the person


    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")