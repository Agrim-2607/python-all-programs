# Enumerate() function adds a counter to each item in a list or any other iterable, and returns a list of tuples containing the
# index position and the element for each element of the iterable.
'''
a = ["Geeks", "for", "Geeks"]

# Iterating list using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Converting to a list of tuples
print(list(enumerate(a)))
'''
marks=[12,36,28,98,25]
for index,mark in enumerate(marks):
    if index==3:
        print("Agrim Awesome!!!")
    