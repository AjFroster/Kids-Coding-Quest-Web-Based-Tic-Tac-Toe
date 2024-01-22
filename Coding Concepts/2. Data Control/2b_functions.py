def add_numbers(a, b):
    return a + b

# Example of using the function
sum = add_numbers(5, 3)
print("5 + 3 =", sum)

def greet(name):
    return "Hello " + name + "!"

# Greeting a child
greeting = greet("Alice")
print(greeting)

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Finding the largest number
largest_number = find_largest([1, 9, 7, 3, 5])
print("The largest number is:", largest_number)

def count_down(start):
    print(start)
    if start > 0:
        count_down(start - 1)

# Starting the countdown
count_down(5)
