#Write a program that checks if a number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print("The number is postive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")    

#Create a program that prints all even numbers from 1 to 50.
for number in range(1, 51):
    if number % 2 == 0:  # Check if the number is even
        print(number)

# Function to calculate the factorial
def factorial(n):
    result = 1
    
    
    for i in range(1, n + 1):
        result *= i
    
    return result


number = int(input("Enter a number to find its factorial: "))


if number < 0:
    print("Input a positive number.")
else:
    # Call the factorial function and print the result
    print(f"The factorial of {number} is {factorial(number)}")


# Create a program that takes a user input and checks if it is a palindrome.
def a_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    
    
    return cleaned_string == cleaned_string[::-1]


user_input = input("Enter a word or phrase to check if it's a palindrome: ")


if a_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")

#Write a program for checking if the given number is even or odd.    

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))


result = check_even_odd(number)
print(f"The number {number} is {result}.")

#Write a program for finding the biggest number among 3 numbers
def find_biggest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

biggest = find_biggest_number(num1, num2, num3)
print(f"The biggest number is {biggest}.")
