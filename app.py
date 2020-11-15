# -*- coding: utf-8 -*-
# print("Hello World 🥰")
print("*" * 10)

# PEP 8 standards
x = 1

student_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(student_count)

course = "Python Programming"
message = """
Hi John, 

This is an email. 

Blah blah blah.

"""

# Strings and their indexes
print(len(course))
# Bracket Notation
print(course[0])
print(course[-1])
print(course[0:3])

# Escape Sequences
course = "Python \" Programming"
# OR
course = "Python \\ Programming"
print(course)

# Formatted Strings
first = "Tracy"
last = "Velasquez"
print(first)
# full = f"{len(first)} {last} {2+2}"
# print(full)

# String Methods
course = "    python programming"
print(course.upper())
print(course.lower())
print(course.title())
print (course.strip())
# will find, returns index of pro
print (course.find("pro")) 
# will not find
print (course.find("Pro"))
print(course.replace("p", "j"))
# checks to see if we have "pro" in course, returns Boolean
print("pro" in course)
print("swift" not in course)

# Numbers
x = 1 
# x = 1.1
# Complex numbers
# x = 1 + 2j # 1 + bi
print(10 + 3)
print(10 - 3)
print(10 * 3)
# returns with decimal
print(10 / 3)
# returns whole number
print(10 // 3)
# modulus - returns remainder
print(10 % 3)

x = 10
x = x + 3
x += 3

# Working with numbers
print(round(2.9))
print(abs(-2.9))
# Math module (import at the top, usually)
import math
print (math.ceil(2.2))
# search Python 3 math modules for more

# Type Conversion
# x = input("x : ")
y = x + 1
print(x)
# print(f"x: {x}, y:{y}")

print(type(course))

age: int = 20
# age: = "Python"
print(age)

#Immutable and Mutable Types
x = 1
print(id(x))

x = x + 1
print(id(x))

y = [1, 2, 3]
print(id(y))

print(y.append(4))
