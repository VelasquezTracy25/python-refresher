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
