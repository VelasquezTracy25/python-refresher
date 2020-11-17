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
guess = 0
answer = 5 
while answer != guess:
    guess = int(input("Guess: "))