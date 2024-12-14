#Write a Python program to print "Hello, World!".
print("Hello, World!")
#Write a Python program that calculates the area of a circle based on the radius entered by the user.
import math
r = int(input("Enter a radius: "))
user_input = r
A = (math.pi)*r**2
print(f"Area is: {A}")
#Create a program that asks the user for their name and age, then prints a message that includes both.
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print(f"{user_name} is {user_age}")
#Write a program that takes two numbers 
#as input from the user and prints their sum, difference, product, and quotient
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = num1 + num2
dif = num1 - num2
prod = num1 * num2
q = num1/num2
print(f"The sum is {sum}, The difference is {dif}, The product is {prod} and the quotient is {q}")

