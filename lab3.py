#Write a function add_numbers(a, b) that returns the sum of two numbers.
def add_numbers(a, b):
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add_numbers(num1, num2)
print(f"The sum  is {result}.")



##Create a function is_prime(n) that checks if a number is prime

def is_prime(n):
   
    if n <= 1:
        return False
    
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
    
    return True 
num = int(input("Enter a number to check if it's prime: "))

#Write a function that takes a list of numbers and returns the largest number in the list.

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


def find_largest_number(numbers):
    
    return max(numbers)


numbers_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))


largest_number = find_largest_number(numbers_list)
print(f"The largest number in the list is: {largest_number}")

#Develop a function fibonacci(n) that prints the Fibonacci sequence up to the nth term.
def fibonacci(n):
    
    a, b = 0, 1
    
    
    for _ in range(n):
        print(a, end=" ")
        
        a, b = b, a + b

\
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
print(fibonacci(n))

#Define a function max_of_three() that takes
# three numbers as arguments and returns the largest of them.
def max_of_three(a, b, c):
    # Use the built-in max() function to find the largest number
    return max(a, b, c)


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


largest = max_of_three(num1, num2, num3)
print(f"The largest number is {largest}.")

#Write a program which makes use of a function to display all such 
# numbers which are divisible by 7 but 
# are not a multiple of 5, between 1000 and 2000.
def divisible_by_7_not_5(start, end):
    
    for number in range(start, end + 1):
        
        if number % 7 == 0 and number % 5 != 0:
            print(number, end=" ")
print(divisible_by_7_not_5(1000, 2000))
