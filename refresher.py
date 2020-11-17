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
    print("shortcut")
    print ("Eligible")           
