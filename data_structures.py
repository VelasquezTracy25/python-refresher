# Lists
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]

zeros = [0] * 5
print(zeros)

combined = zeros + letters
numbers = list(range(20))
chars =list("Hello World")
print(combined)
print(numbers)
print(len(chars))

# Accessing items
letters = ["a", "b", "c", "d"]
print(letters)
letters[0] = "A" 
print(letters[-1])
print (letters)
print(letters[::2])

numbers = list(range(20))
# return list in reverse order
print(numbers[::-1])
# return every other item in list - 2, 4 ,6, 8...
print(numbers[::2])

# List Unpacking

# Long way - not recommended
# numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# Unpacking option
numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)
# 1 2, 3

# Unpacking with longer lists
numbers = [1, 2, 3, 4, 4, 4, 4, 4]
# Other is a list of all the items after the first two items
first, second, *other = numbers
print(first, second, other)
# 1 2 [3, 4, 4, 4, 4, 4]

# Unpacking with other in the middle of list
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
# Other is a list of all the items after the first two items
first, *other, last = numbers
print(first, other, last)
# 1 [2, 3, 4, 4, 4, 4] 9

# Looping over lists
letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items
for letter in enumerate(letters):
    print (index, letter)

# Adding or Removing items   
letters = ["a", "b", "c"]

# Add
letters.append("d")
letters.insert(0, "-")
print(letters)

# Remove
letters.pop()
print(letters)

# Or 
letters.remove("b")
print(letters)

# Delete
del letters[0:3]
print(letters)

# Clear (delete all)
letters.clear()
print(letters)