fruits = ["peaches", "apples", "pears", "apples", "apples"]
years = [3, "1998", 2.5, 987, "1994"]
years2 = ['3', "1998", '2.5', '987', "1994"]
'''
fruits → list of only strings (with duplicates: "apples").
years → mixed types (int, str, float).
years2 → all strings, but representing numbers.
'''

print("apple" in fruits)
print("apples" in fruits)

#"apple" ≠ "apples". Membership checks are case- and spelling-sensitive.

print(fruits, years, years2)

fruits.append("oranges")
print(fruits)
'''
.append(x) adds one item at the end.
Now fruits = ["peaches", "apples", "pears", "apples", "apples", "oranges"].
'''

fruits.extend(years2)
print(fruits)
'''
.extend(list2) adds all items from another list.
So now fruits has "3", "1998", "2.5", "987", "1994" added at the end.
'''

fruits.remove("oranges")
print(fruits)
'''
.remove(x) deletes the first occurrence of "oranges".
If "oranges" wasn’t in the list, it would throw an error.
'''

fruits.pop(0) # removes first item ("peaches")
print(fruits)
'''
.pop(index) removes item at that index and returns it.
After these two pops, both the first and last elements are gone.
'''

fruits.pop(-1)  # removes last item
print(fruits)

fruits.sort()
print(fruits)
'''
Sorts the list alphabetically (since all elements are now strings after extend + removals).
⚠️ Would fail if list still had numbers + strings (TypeError like you saw before).
'''

numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
numbers.sort()
print(numbers)

print(fruits.count("apples")) # counts how many times "apples" appears
print(fruits.count("apple")) # 0 because "apple" is not in list
print(fruits.index("apples")) # finds the index of the FIRST "apples"


'''
.count(x) → returns the number of occurrences of an item.
.index(x) → returns the first position where the item appears (error if not found).
'''

'''
✅ Summary of concepts used:
in → membership test
.append() → add one item
.extend() → add multiple items from another list
.remove() → delete by value (first match)
.pop() → delete by index
.sort() → sort the list (works only if all items are same type or comparable)
.count() → count occurrences
.index() → find first index of item
'''