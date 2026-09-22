def hello():
    print("Hello, World !")
hello()

#greet the name
def greet(name):
    print("My name is :"+name)
greet("Tejsvi")

#add two numbers
def add(a,b):
    return a+b
result = add(10,3)
print(result)

#square of the num
def square(a):
    return a*a
result = square(3)
print(result)

#odd-even
def num(n):
    if n%2 == 0:
        return "even"
    else:
        return "odd"
result = num(13)
print(result)

#find max
def max(a,b):
    return a if a>b else b
result = max(3,5)
print(result)

# Celsius to Fahrenheit
def celsius(n):
    return (n*9/5)+32
n=float(input("enter celsius:"))
result = celsius(n)
print(result)