# Understanding zip: what it can achieve and its limitations

# Using strings
str1 = 'TEST'
str2 = 'ZIPS'
# zip is an iterable object and can't be printed directly
print(zip(str1, str2)) # console out: <zip object at 0x000001B9BAD46088>
# zip always returns pairs as tuple values
print(list(zip(str1, str2))) # console out: [('T', 'Z'), ('E', 'I'), ('S', 'P'), ('T', 'S')]

# What happens if they aren't of the same length?
str1 = 'TEST'
str2 = 'ZIP'
# zip will stop at the shortest iterable.
print(list(zip(str1, str2))) # console out: [('T', 'Z'), ('E', 'I'), ('S', 'P')] (T) not included

# zip can be useful to join the next item with the current item using the slice operator
print(list(zip(str1, str1[1:]))) # console out: [('T', 'E'), ('E', 'S'), ('S', 'T')]
# or even in reversed order
# Pairs the characters of 'TEST' with its reverse 'TSET'.
print(list(zip(str1, str1[::-1]))) # console out: [('T', 'T'), ('E', 'S'), ('S', 'E'), ('T', 'T')]

# Using strings and numbers
str1 = 'TEST'
# Numbers don't support iteration, so they need to be transformed into strings
num1 = 1234

# Now zip works
print(list(zip(str1, str(num1)))) # console out: [('T', '1'), ('E', '2'), ('S', '3'), ('T', '4')]

# Using lists
employees = ["Jose C.", "Carlos R.", "Luis P."]
salaries = [100, 200, 300]

# Get a list of lists instead of tuples
print(list(map(list, zip(employees, salaries)))) # console out: [['Jose C.', 100], ['Carlos R.', 200], ['Luis P.', 300]]
# Convert to a dictionary Dict<employee, salary>
print(dict(zip(employees, salaries))) # console out: {'Jose C.': 100, 'Carlos R.': 200, 'Luis P.': 300}

# Using tuples gives the same results
employees = ("Jose C.", "Carlos R.", "Luis P.")
salaries = (100, 200, 300)
# zip always returns pairs as tuple values
print(list(zip(employees, salaries))) # console out: [('Jose C.', 100), ('Carlos R.', 200), ('Luis P.', 300)]
# Get a list of lists instead of tuples
print(list(map(list, zip(employees, salaries)))) # console out: [['Jose C.', 100], ['Carlos R.', 200], ['Luis P.', 300]]
# Convert two lists into a dictionary
print(dict(zip(employees, salaries))) # console out: {'Jose C.': 100, 'Carlos R.': 200, 'Luis P.': 300}

# Unzipping
str1 = 'TEST'
str2 = 'ZIPS'

zipped = list(zip(str1, str2))

uz_str1, uz_str2 = zip(*zipped)
# Remember, zip always returns tuples
print(uz_str1, uz_str2) # console out: ('T', 'E', 'S', 'T') ('Z', 'I', 'P', 'S')
# Parse as needed
print("".join(uz_str1), "".join(uz_str2)) # console out: TEST ZIPS

employees = ["Jose C.", "Carlos R.", "Luis P."]
salaries = [100, 200, 300]

zipped_lists = list(zip(employees, salaries))
uz_list1, uz_list2 = zip(*zipped_lists)
# Parse lists to get originals
print(list(uz_list1), list(uz_list2)) # console out: ['Jose C.', 'Carlos R.', 'Luis P.'] [100, 200, 300]

# Combining multiple iterables (more than two)
# zip works with any number of iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
locations = ["NY", "LA", "SF"]
print(list(zip(names, ages, locations))) # console out: [('Alice', 25, 'NY'), ('Bob', 30, 'LA'), ('Charlie', 35, 'SF')]

# zip objects are iterables, so they can be traversed with loops
for name, age, location in zip(names, ages, locations):
    print(f"{name} is {age} years old and lives in {location}.")

# zip with range and custom indices
# Useful for indexing or pairing with a generated sequence
letters = ["a", "b", "c"]
# range() in Python is exclusive at the end, meaning it generates numbers up to but not including the stop value.
# So we need to add 1
indices = range(1, len(letters) + 1)
print(list(zip(indices, letters))) # console out: [(1, 'a'), (2, 'b'), (3, 'c')]

# Summary
# zip() simplifies the process of pairing, unpacking, and traversing related iterables.
# Its versatility allows for working with lists, tuples, and strings in a clean and readable way.
# Keep in mind its limitation: it only pairs up to the shortest iterable length.
