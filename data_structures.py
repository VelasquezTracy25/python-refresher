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