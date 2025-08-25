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
temp_f = 40

while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

for number in range(1,11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(number))


for number in range(1,11):
    if number == 3:
        pass
    else:
        print("The number is {}.".format(number))



