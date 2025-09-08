#List (ordered, mutable)
fruits = ["apple", "banana", "mango"]
fruits.append("orange")   # add element
print(fruits[0])          # access element
'''
List → Ordered collection of items.
Mutable → You can add, remove, or change elements.
append("orange") adds "orange" at the end → ["apple", "banana", "mango", "orange"].
fruits[0] → indexing (0-based). Prints "apple".
✅ When to use? When you need an ordered collection that you can change.
'''

#Tuple (ordered, immutable)
colors = ("red", "green", "blue")
print(colors[1])
'''
Tuple → Like a list, but immutable (can’t be changed once created).
Useful for fixed collections of values.
colors[1] prints "green".
✅ When to use? When you want a collection that should not be modified (e.g., days of the week).
'''

#Set (unordered, unique values)
unique_nums = {1, 2, 2, 3}
print(unique_nums)   # Output: {1, 2, 3}
'''
Set → Unordered collection of unique elements (no duplicates).
{1, 2, 2, 3} automatically removes the duplicate 2.
Output: {1, 2, 3} (order not guaranteed).
✅ When to use? When you need to store unique values or perform set operations (union, intersection, etc.).
'''

#Dictionary (key-value pairs)
student = {"name": "Fouad", "age": 25}
print(student["name"])
'''
Dictionary → Collection of key-value pairs.
"name" → "Fouad", "age" → 25.
student["name"] prints "Fouad".
✅ When to use? When you want to map keys to values (like JSON data).
'''

'''
⚡ Quick Comparison
Type	Ordered?	Mutable?	Allows Duplicates?	Access by
List	✅ Yes	✅ Yes	✅ Yes	Index
Tuple	✅ Yes	❌ No	✅ Yes	Index
Set	❌ No	✅ Yes	❌ No (unique only)	N/A (by value)
Dictionary	✅ Yes (3.7+)	✅ Yes	❌ No (keys must be unique)	Key
'''