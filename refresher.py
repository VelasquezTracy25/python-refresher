# Conditional Statements
age = 22
if age >= 18:
    print("Adult")
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

    print("All done!")        

# shortcut
# if x > 1:
#     # empty block
#     pass 
# else:
#     pass     

# logical operators
name = "Tracy"
if not name:
    print ("Name is empty")
elif name:
    print("not empty")

age = 22 
if age >= 18 and age < 65:
    print ("Eligible") 

if age >= 18 and age <65:
    print("shortcut:")
    print ("Eligible") 

#Ternary
newAge = 25
# message = age >= 18 ? "Eligible" : "Not Eligible"
message = "Elibile" if age >= 18 else "Not Eligible"

# For loops 
# for x in "Python":
# print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(5):
    print(x)    

for x in range(0, 5):
    print(x)     

for x in range(0, 10, 2):
    print(x)    

# For..else

# Long way
names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("found")
        found = True
        break
    if not found: 
        print("Not Found")

# Shortcut with for-else
names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("found")
        found = True
        break
    else:
        print("Not Found")

#While loops
# guess = 0
# answer = 5 
# while answer != guess:
#     guess = int(input("Guess: "))

#Functions

def increment(number, by):
    return (number, number + by)


print(increment(2,3))


def increment(number, by = 1):
    return (number, number + by)


print(increment(2))

def increment(number: int, by: int = 5) -> tuple:
    return (number, number + by)


print(increment(2))

# Arguments -xargs

# long way
# def multiply(list):
#    return a * b

# multiply([2,3,4,5])

# shortcut with * 
def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total

print(multiply(2, 3, 4, 5) )  

# Arguments -xxargs
def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])

save_user(id=1, name="admin")    