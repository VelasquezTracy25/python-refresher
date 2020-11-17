# My solution

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input    
        
print(fizz_buzz(3))

# Shortcut

def fizz_buzz2(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input    
        
print(fizz_buzz2(3))
print(fizz_buzz2(5))
print(fizz_buzz2(15))

# Fizzbuzz loop exercise

def fizzBuzzLoop(max):
    for fizzbuzz in range(max):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)  

print("Fizzbuzz with Loop:")
print(fizzBuzzLoop(100))  