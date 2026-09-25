num = int(input("Enter a number: ")) 
if num % 2 == 0:
     print("The number is even") 
else: 
    print("The number is odd")

#Find the largest of two numbers using comparison operators
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
if a > b: 
    print("Largest number is:", a) 
elif b > a: 
    print("Largest number is:", b) 
else: 
    print("Both numbers are equal")