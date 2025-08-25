x = 3
while x > 0:
    print(x)
    x -= 1

'''

Explanation:
Loop runs while x > 0.

First x=3 → prints 3, then x = x - 1 → 2.

Keeps going until x becomes 0.
'''
print("===========================================")
print("===========================================")

fruits = ["apple", "orange", "pears", "cherries", "grapes"]


for i in fruits:
    print("Would you like {} ?".format(i))


for number in range(1,11):
    print("Number {}".format(number))