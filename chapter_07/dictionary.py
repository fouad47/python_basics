stuff = {"food": 15, "energy": 100, "enemies":3}
#stuff is a dictionary with keys ("food", "energy", "enemies") and their values (15, 100, 3).

print(stuff.get("food"))
'''
.get(key) returns the value of the key.
Output: 15.
Unlike stuff["food"], if the key doesn’t exist, .get() returns None instead of throwing an error.
'''
print(stuff.items())
'''
Returns all key-value pairs as a dict_items object.
'''
print(stuff.keys())
'''
Returns all keys.
Example: dict_keys(['food', 'energy', 'enemies']).
'''
print(stuff.popitem())
'''
Removes and returns the last inserted key-value pair (since Python 3.7+, dicts preserve insertion order).
Suppose it removes ("enemies", 3).
Now stuff = {"food": 15, "energy": 100}.
'''
print(stuff)
print(stuff.setdefault("food"))
'''
.setdefault(key, default) →
If the key exists → return its value (no change).
If it doesn’t exist → add it with the default value.
"food" already exists (15), so nothing changes.
Output: 15, and dict is still {"food": 15, "energy": 100}.
'''
print(stuff)
print(stuff.setdefault("friends", 123))
'''
"friends" doesn’t exist, so it gets added with value 123.
Dict becomes: {"food": 15, "energy": 100, "friends": 123}.
'''
print(stuff)


new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)
'''
.update() merges another dictionary.
Adds "rocks": 4, "arrows": 18.
'''


new_items = {"rocks": 2, "arrows":5}
stuff.update(new_items)
print(stuff)
'''
If keys already exist, .update() overwrites values.
"rocks": 4 → 2, "arrows": 18 → 5.
'''


up_new = {"food": 3, "webs":2}
stuff.update(up_new)
print(stuff)
'''
"food" exists → value changes 15 → 3.
"webs": 2 is added as new key.
'''

stuff.update(food = 450, cookies = 6)
print(stuff)
'''
Another way of updating: update(key=value, ...).
"food": 3 → 450, "cookies": 6 is added.
'''


'''
✅ Summary of Methods Used
.get(key) → Safe key access (returns None if not found).
.items() → View all key-value pairs.
.keys() → View all keys.
.popitem() → Remove + return last key-value.
.setdefault(key, default) → Get value if exists, else add with default.
.update(dict or kwargs) → Merge/overwrite dictionary values.
'''