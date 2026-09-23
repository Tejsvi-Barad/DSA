# factorial number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

result = int(input("enter num :"))
print(factorial(result))
#print(factorial(5))

#pos-neg-zero
def num(n):
    if n >0:
        return "positive num"
    elif n<0:
        return "negative num"
    else:
        return "zero"
print(num(-10))

#count vovel in str
def vovel(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count
print(vovel("TejsviBarad"))

#prime-not prime
def prime(n):
    if n < 2:
        return "not prime num"
    for i in range(2,n):
        if n%i == 0:
            return "not prime num"
    return "prime num"
print(prime(6))

#A prime number is a natural number greater than 1 that has exactly two factors: 1 and itself.
#7 is prime because it can only be divided exactly by 1 and 7.
#6 is not prime because it can be divided by 1, 2, 3, and 6.

#return all prime numbers between two numbers
def all_prime(start,end):
    result = []
    for n in range(start,end+1):
        if n<2:
            continue
        is_prime = True
        for i in range(2,n):
            if n%i == 0:
                is_prime= False
                break

        if is_prime:
            result.append(n)
    return result
print(all_prime(1,10))
