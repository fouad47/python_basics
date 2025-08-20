"""
This is a multi-line comment
You can use this kind of comment to
make longer notes as you are learning.
In python, these are often used as
docstrings.
"""

name = "Janelle Jones"
type_of_car = "Rolls Royce"
school = "Foundation Elementary School"

print(name + school)
print(name + type_of_car)

print(name + " " + school)
print(name + " " + type_of_car)
print(name + " works at " + school + ".")
print(name + " have car type " + type_of_car + ".")
print(name + " works at " + school + " and have car type " + type_of_car + ".")

#python string.format()
print("{} works at {}.".format(name, school))
print("{} works at {} and have car type {}".format(name,school,type_of_car))