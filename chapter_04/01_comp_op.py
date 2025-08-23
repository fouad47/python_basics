name = input("What's your name? ")
if name == "Jessica":
    print("Hello, nice to see you {}".format(name))
elif name == "Danielle":
    print("Hello, you are a great person!")
elif name != "Mariah":
    print("You're not Mariah!")
elif name == "Kingston":
    print("Hi, {}, let's have lunch soon!".format(name))
else:
    print("Have a nice day!")


''' 
Code Breakdown
name = input("What's your name? ")

This line prompts the user with the question "What's your name? ".

Whatever the user types is stored as a string in the variable name.

if name == "Jessica":

This is the first condition. It checks if the value of the name variable is exactly "Jessica".

If it is, the code inside this block runs: print("Hello, nice to see you {}".format(name)). The format() method replaces the {} with the value of the name variable, so the output would be "Hello, nice to see you Jessica". The program then exits the if/elif/else structure.

elif name == "Danielle":

This stands for "else if". This condition is only checked if the first if statement was false.

It checks if name is "Danielle".

If true, it prints "Hello, you are a great person!".

elif name != "Mariah":

This condition is checked only if the previous if and elif statements were false.

It checks if name is not equal to "Mariah". This is a very broad condition.

If the user enters anything other than "Mariah", "Jessica", or "Danielle", this condition will be true, and the code will print "You're not Mariah!". The program will then exit the if/elif/else structure.

Because of its position, this line will prevent the next elif from ever being reached for any name that isn't "Mariah", including "Kingston". For example, if the user enters "Kingston", the code will go past the first two checks, hit this line, see that "Kingston" is not "Mariah", and print "You're not Mariah!". The last two blocks will be ignored.

elif name == "Kingston":

This condition is logically flawed due to the previous elif. It will only be reached if the user's input is "Mariah". However, if the user enters "Mariah," this condition is still false. Therefore, this elif block will never be executed.

else:

This is the final catch-all block. It is only executed if all the preceding if and elif conditions are false.

Given the problematic elif name != "Mariah" condition, this else block will only be reached if the user's input is exactly "Mariah".

If the input is "Mariah", the code will print "Have a nice day!".

'''