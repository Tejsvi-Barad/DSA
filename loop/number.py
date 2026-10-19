#Print 1 to 10 using a for loop
for i in range(1,11):
    print(i)

#Print 10 to 1 using a while loop
i=10
while i>=1:
    print(i)
    i-=1

#Print the multiplication table of a number
n=int(input("enter num:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#Find the sum of numbers from 1 to N
n=int(input("enter num:"))
total=0

for i in range(1,n+1):
    total+=i
print("sum:",total)

#Find the factorial of a number
n=int(input("enter num:"))
fact = 1
for i in range(1,n+1):
    fact*=i
print("factorial",fact)

#Print all even numbers between 1 and 100
for i in range(2,102,2):
    print(i,end=" ")

#Reverse a number using a loop
n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed number =", rev,end=" ")

#Count the digits of a number
n = int(input("Enter a number: "))
count = 0

if n == 0:
    count = 1
else:
    n = abs(n)
    while n > 0:
        count += 1
        n = n // 10
print("Number of digits =", count)

#Check whether a number is prime or not
n = int(input("Enter a number: "))
prime = True

if n <= 1:
    prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
if prime:
    print("Prime number")
else:
    print("Not a prime number")

#Print the Fibonacci series up to N terms
n = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b