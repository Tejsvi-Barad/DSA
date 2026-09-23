#maximum of three number
def num(a,b,c):
    if a>b and a>c:
        return "a is max num"
    elif b>a and b>c:
        return "b is max num"
    else:
        return "c is big num"
print(num(12,13,10))

def maximum(a, b, c):
    return max(a, b, c)

print(maximum(10, 25, 15))

#sum of all elements in a list
def sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
print(sum([1,2,3,4,5]))

#find the largest element in a list
def big(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num 
    return largest
print(big([-1,-2,-3,-4,-5]))

#Find the second-largest number in a list
def sec_largest(n):
    n = list(set(n))
    n.sort()
    return n[-2]
print(sec_largest([1,2,6,7,8,10]))

num = [50,40,30,20,10]
num.sort()
print(num[::-1][1])

num = [50, 40, 30, 20, 10]
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]
print(num[1])

#remove duplicate elements from a list
def remove_duplicate(number):
    list = []
    for num in number:
        if num not in list:
            list.append(num)
    return list
print(remove_duplicate([1,2,2,3,4,4,5,5]))

#Merge two lists and remove duplicates
def merge(list1,list2):
    result = []
    for num in list1+list2:
        if num not in result:
            result.append(num)
    return result
print(merge([1,2,3],[2,3,4,5]))

#count how many times an element appears in a list
def count_number(number,n):
    count = 0
    for num in number:
        if num == n:
            count += 1
    return count
print(count_number([1,2,3,2,4,5],2))