#pos-neg-zero
num = int(input("Enter a number: ")) 
if num > 0: 
    print("Positive") 
elif num < 0: 
    print("Negative") 
else: 
    print("Zero")

#largest of three numbers
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
c = int(input("Enter third number: ")) 

if a >= b and a >= c: 
    print("Largest number is:", a) 
elif b >= a and b >= c: 
    print("Largest number is:", b) 
else: 
    print("Largest number is:", c)


#number is divisible by 5 and 11
num = int(input("Enter a number: ")) 
if num % 5 == 0 and num % 11 == 0: 
    print("The number is divisible by both 5 and 11") 
else: 
    print("The number is not divisible by both 5 and 11")